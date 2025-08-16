from flask import Flask, render_template, request, jsonify, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
from werkzeug.security import generate_password_hash, check_password_hash
import yfinance as yf
import pandas as pd
import numpy as np
import plotly.graph_objects as go
import plotly.utils
import json
import requests
from datetime import datetime, timedelta
import ta
from bs4 import BeautifulSoup
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', 'your-secret-key-here')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///stocks.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

# Database Models
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(120), nullable=False)
    stocks = db.relationship('Stock', backref='user', lazy=True)

class Stock(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    symbol = db.Column(db.String(10), nullable=False)
    name = db.Column(db.String(100), nullable=False)
    quantity = db.Column(db.Float, default=0)
    avg_price = db.Column(db.Float, default=0)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    added_date = db.Column(db.DateTime, default=datetime.utcnow)

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# Stock Analysis Functions
def get_stock_data(symbol, period='1y'):
    """Get stock data from Yahoo Finance"""
    try:
        stock = yf.Ticker(symbol)
        data = stock.history(period=period)
        return data
    except Exception as e:
        print(f"Error fetching data for {symbol}: {e}")
        return None

def calculate_fibonacci_levels(data):
    """Calculate Fibonacci retracement levels"""
    high = data['High'].max()
    low = data['Low'].min()
    diff = high - low
    
    levels = {
        '0.0': low,
        '0.236': low + 0.236 * diff,
        '0.382': low + 0.382 * diff,
        '0.5': low + 0.5 * diff,
        '0.618': low + 0.618 * diff,
        '0.786': low + 0.786 * diff,
        '1.0': high
    }
    return levels

def calculate_technical_indicators(data):
    """Calculate various technical indicators"""
    indicators = {}
    
    # RSI
    indicators['rsi'] = ta.momentum.RSIIndicator(data['Close']).rsi()
    
    # MACD
    macd = ta.trend.MACD(data['Close'])
    indicators['macd'] = macd.macd()
    indicators['macd_signal'] = macd.macd_signal()
    
    # Bollinger Bands
    bb = ta.volatility.BollingerBands(data['Close'])
    indicators['bb_upper'] = bb.bollinger_hband()
    indicators['bb_lower'] = bb.bollinger_lband()
    indicators['bb_middle'] = bb.bollinger_mavg()
    
    # Moving Averages
    indicators['sma_20'] = ta.trend.SMAIndicator(data['Close'], window=20).sma_indicator()
    indicators['sma_50'] = ta.trend.SMAIndicator(data['Close'], window=50).sma_indicator()
    indicators['ema_12'] = ta.trend.EMAIndicator(data['Close'], window=12).ema_indicator()
    indicators['ema_26'] = ta.trend.EMAIndicator(data['Close'], window=26).ema_indicator()
    
    return indicators

def generate_trading_recommendation(data, indicators):
    """Generate buy/sell recommendation based on technical analysis"""
    current_price = data['Close'].iloc[-1]
    current_rsi = indicators['rsi'].iloc[-1]
    current_macd = indicators['macd'].iloc[-1]
    current_macd_signal = indicators['macd_signal'].iloc[-1]
    
    # Fibonacci levels
    fib_levels = calculate_fibonacci_levels(data)
    
    # Analysis logic
    signals = []
    strength = 0
    
    # RSI Analysis
    if current_rsi < 30:
        signals.append("RSI מצביע על קנייה (oversold)")
        strength += 2
    elif current_rsi > 70:
        signals.append("RSI מצביע על מכירה (overbought)")
        strength -= 2
    
    # MACD Analysis
    if current_macd > current_macd_signal:
        signals.append("MACD מצביע על מגמה חיובית")
        strength += 1
    else:
        signals.append("MACD מצביע על מגמה שלילית")
        strength -= 1
    
    # Price vs Moving Averages
    sma_20 = indicators['sma_20'].iloc[-1]
    sma_50 = indicators['sma_50'].iloc[-1]
    
    if current_price > sma_20 > sma_50:
        signals.append("מחיר מעל ממוצעים נעים - מגמה חיובית")
        strength += 1
    elif current_price < sma_20 < sma_50:
        signals.append("מחיר מתחת לממוצעים נעים - מגמה שלילית")
        strength -= 1
    
    # Fibonacci Analysis
    for level, price in fib_levels.items():
        if abs(current_price - price) / price < 0.02:  # Within 2% of level
            if level in ['0.236', '0.382']:
                signals.append(f"מחיר קרוב לרמת פיבונצי {level} - תמיכה")
                strength += 1
            elif level in ['0.618', '0.786']:
                signals.append(f"מחיר קרוב לרמת פיבונצי {level} - התנגדות")
                strength -= 1
    
    # Final recommendation
    if strength >= 2:
        recommendation = "קנייה"
        confidence = "גבוהה" if strength >= 3 else "בינונית"
    elif strength <= -2:
        recommendation = "מכירה"
        confidence = "גבוהה" if strength <= -3 else "בינונית"
    else:
        recommendation = "החזקה"
        confidence = "בינונית"
    
    return {
        'recommendation': recommendation,
        'confidence': confidence,
        'strength': strength,
        'signals': signals,
        'fibonacci_levels': fib_levels
    }

def get_market_overview():
    """Get US market overview"""
    try:
        # Major indices
        indices = ['^GSPC', '^DJI', '^IXIC', '^VIX']  # S&P 500, Dow Jones, NASDAQ, VIX
        market_data = {}
        
        for index in indices:
            ticker = yf.Ticker(index)
            info = ticker.info
            hist = ticker.history(period='2d')
            
            if not hist.empty:
                current_price = hist['Close'].iloc[-1]
                prev_price = hist['Close'].iloc[-2]
                change = current_price - prev_price
                change_percent = (change / prev_price) * 100
                
                market_data[index] = {
                    'name': info.get('longName', index),
                    'price': round(current_price, 2),
                    'change': round(change, 2),
                    'change_percent': round(change_percent, 2),
                    'volume': info.get('volume', 0)
                }
        
        return market_data
    except Exception as e:
        print(f"Error fetching market data: {e}")
        return {}

# Routes
@app.route('/')
def index():
    if current_user.is_authenticated:
        return redirect(url_for('dashboard'))
    return render_template('index.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        
        if User.query.filter_by(username=username).first():
            flash('שם משתמש כבר קיים')
            return redirect(url_for('register'))
        
        if User.query.filter_by(email=email).first():
            flash('אימייל כבר קיים')
            return redirect(url_for('register'))
        
        user = User(username=username, email=email, 
                   password_hash=generate_password_hash(password))
        db.session.add(user)
        db.session.commit()
        
        flash('הרשמה הושלמה בהצלחה!')
        return redirect(url_for('login'))
    
    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = User.query.filter_by(username=username).first()
        
        if user and check_password_hash(user.password_hash, password):
            login_user(user)
            return redirect(url_for('dashboard'))
        else:
            flash('שם משתמש או סיסמה שגויים')
    
    return render_template('login.html')

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('index'))

@app.route('/dashboard')
@login_required
def dashboard():
    user_stocks = Stock.query.filter_by(user_id=current_user.id).all()
    market_overview = get_market_overview()
    return render_template('dashboard.html', stocks=user_stocks, market=market_overview)

@app.route('/add_stock', methods=['POST'])
@login_required
def add_stock():
    symbol = request.form['symbol'].upper()
    quantity = float(request.form['quantity'])
    avg_price = float(request.form['avg_price'])
    
    # Get stock info from Yahoo Finance
    try:
        ticker = yf.Ticker(symbol)
        info = ticker.info
        name = info.get('longName', symbol)
    except:
        name = symbol
    
    stock = Stock(symbol=symbol, name=name, quantity=quantity, 
                 avg_price=avg_price, user_id=current_user.id)
    db.session.add(stock)
    db.session.commit()
    
    flash('מניה נוספה בהצלחה!')
    return redirect(url_for('dashboard'))

@app.route('/delete_stock/<int:stock_id>')
@login_required
def delete_stock(stock_id):
    stock = Stock.query.get_or_404(stock_id)
    if stock.user_id == current_user.id:
        db.session.delete(stock)
        db.session.commit()
        flash('מניה נמחקה בהצלחה!')
    return redirect(url_for('dashboard'))

@app.route('/analyze/<symbol>')
@login_required
def analyze_stock(symbol):
    data = get_stock_data(symbol)
    if data is None or data.empty:
        flash('לא ניתן לקבל נתונים עבור מניה זו')
        return redirect(url_for('dashboard'))
    
    indicators = calculate_technical_indicators(data)
    recommendation = generate_trading_recommendation(data, indicators)
    
    # Create interactive chart
    fig = go.Figure()
    
    # Candlestick chart
    fig.add_trace(go.Candlestick(
        x=data.index,
        open=data['Open'],
        high=data['High'],
        low=data['Low'],
        close=data['Close'],
        name='מחיר'
    ))
    
    # Moving averages
    fig.add_trace(go.Scatter(
        x=data.index,
        y=indicators['sma_20'],
        name='SMA 20',
        line=dict(color='orange')
    ))
    
    fig.add_trace(go.Scatter(
        x=data.index,
        y=indicators['sma_50'],
        name='SMA 50',
        line=dict(color='blue')
    ))
    
    # Bollinger Bands
    fig.add_trace(go.Scatter(
        x=data.index,
        y=indicators['bb_upper'],
        name='Bollinger Upper',
        line=dict(color='gray', dash='dash')
    ))
    
    fig.add_trace(go.Scatter(
        x=data.index,
        y=indicators['bb_lower'],
        name='Bollinger Lower',
        line=dict(color='gray', dash='dash'),
        fill='tonexty'
    ))
    
    fig.update_layout(
        title=f'ניתוח טכני - {symbol}',
        xaxis_title='תאריך',
        yaxis_title='מחיר',
        template='plotly_white'
    )
    
    chart_json = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    
    return render_template('analyze.html', 
                         symbol=symbol,
                         data=data,
                         indicators=indicators,
                         recommendation=recommendation,
                         chart_json=chart_json)

@app.route('/api/stock_data/<symbol>')
def api_stock_data(symbol):
    data = get_stock_data(symbol)
    if data is None:
        return jsonify({'error': 'לא ניתן לקבל נתונים'}), 400
    
    indicators = calculate_technical_indicators(data)
    recommendation = generate_trading_recommendation(data, indicators)
    
    return jsonify({
        'symbol': symbol,
        'current_price': float(data['Close'].iloc[-1]),
        'change': float(data['Close'].iloc[-1] - data['Close'].iloc[-2]),
        'change_percent': float(((data['Close'].iloc[-1] - data['Close'].iloc[-2]) / data['Close'].iloc[-2]) * 100),
        'volume': int(data['Volume'].iloc[-1]),
        'rsi': float(indicators['rsi'].iloc[-1]),
        'recommendation': recommendation
    })

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)