from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
from kivy.uix.scrollview import ScrollView
from kivy.uix.gridlayout import GridLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.popup import Popup
from kivy.core.window import Window
from kivy.clock import Clock
from kivy.network.urlrequest import UrlRequest
from kivy.properties import ObjectProperty, StringProperty
from kivy.lang import Builder
import json
import requests
from datetime import datetime

# Set window size for testing (remove for mobile)
Window.size = (400, 700)

# KV Language string for UI
KV = '''
#:import utils kivy.utils

<LoginScreen>:
    BoxLayout:
        orientation: 'vertical'
        padding: 20
        spacing: 20
        
        Label:
            text: 'מעקב מניות'
            font_size: '24sp'
            size_hint_y: None
            height: '50dp'
            color: 0.2, 0.6, 1, 1
        
        TextInput:
            id: username
            hint_text: 'שם משתמש'
            multiline: False
            size_hint_y: None
            height: '50dp'
            font_size: '16sp'
        
        TextInput:
            id: password
            hint_text: 'סיסמה'
            multiline: False
            password: True
            size_hint_y: None
            height: '50dp'
            font_size: '16sp'
        
        Button:
            text: 'התחבר'
            size_hint_y: None
            height: '50dp'
            background_color: 0.2, 0.6, 1, 1
            on_press: root.login()
        
        Button:
            text: 'הרשמה'
            size_hint_y: None
            height: '50dp'
            background_color: 0.3, 0.7, 0.3, 1
            on_press: root.show_register()
        
        Widget:
            size_hint_y: 1

<RegisterScreen>:
    BoxLayout:
        orientation: 'vertical'
        padding: 20
        spacing: 20
        
        Label:
            text: 'הרשמה'
            font_size: '24sp'
            size_hint_y: None
            height: '50dp'
            color: 0.2, 0.6, 1, 1
        
        TextInput:
            id: reg_username
            hint_text: 'שם משתמש'
            multiline: False
            size_hint_y: None
            height: '50dp'
            font_size: '16sp'
        
        TextInput:
            id: reg_email
            hint_text: 'אימייל'
            multiline: False
            size_hint_y: None
            height: '50dp'
            font_size: '16sp'
        
        TextInput:
            id: reg_password
            hint_text: 'סיסמה'
            multiline: False
            password: True
            size_hint_y: None
            height: '50dp'
            font_size: '16sp'
        
        Button:
            text: 'הירשם'
            size_hint_y: None
            height: '50dp'
            background_color: 0.2, 0.6, 1, 1
            on_press: root.register()
        
        Button:
            text: 'חזרה להתחברות'
            size_hint_y: None
            height: '50dp'
            background_color: 0.7, 0.7, 0.7, 1
            on_press: root.go_back()
        
        Widget:
            size_hint_y: 1

<DashboardScreen>:
    BoxLayout:
        orientation: 'vertical'
        padding: 10
        spacing: 10
        
        Label:
            text: 'לוח בקרה'
            font_size: '20sp'
            size_hint_y: None
            height: '40dp'
            color: 0.2, 0.6, 1, 1
        
        ScrollView:
            GridLayout:
                id: market_grid
                cols: 2
                spacing: 10
                size_hint_y: None
                height: self.minimum_height
                padding: 10
        
        Button:
            text: 'הוסף מניה'
            size_hint_y: None
            height: '50dp'
            background_color: 0.3, 0.7, 0.3, 1
            on_press: root.show_add_stock()
        
        Button:
            text: 'התנתק'
            size_hint_y: None
            height: '50dp'
            background_color: 0.8, 0.3, 0.3, 1
            on_press: root.logout()

<AddStockScreen>:
    BoxLayout:
        orientation: 'vertical'
        padding: 20
        spacing: 20
        
        Label:
            text: 'הוסף מניה חדשה'
            font_size: '20sp'
            size_hint_y: None
            height: '40dp'
            color: 0.2, 0.6, 1, 1
        
        TextInput:
            id: stock_symbol
            hint_text: 'סימול מניה (לדוגמה: AAPL)'
            multiline: False
            size_hint_y: None
            height: '50dp'
            font_size: '16sp'
        
        TextInput:
            id: stock_quantity
            hint_text: 'כמות מניות'
            multiline: False
            input_filter: 'float'
            size_hint_y: None
            height: '50dp'
            font_size: '16sp'
        
        TextInput:
            id: stock_price
            hint_text: 'מחיר ממוצע'
            multiline: False
            input_filter: 'float'
            size_hint_y: None
            height: '50dp'
            font_size: '16sp'
        
        Button:
            text: 'הוסף מניה'
            size_hint_y: None
            height: '50dp'
            background_color: 0.3, 0.7, 0.3, 1
            on_press: root.add_stock()
        
        Button:
            text: 'חזרה'
            size_hint_y: None
            height: '50dp'
            background_color: 0.7, 0.7, 0.7, 1
            on_press: root.go_back()
        
        Widget:
            size_hint_y: 1

<StockAnalysisScreen>:
    BoxLayout:
        orientation: 'vertical'
        padding: 10
        spacing: 10
        
        Label:
            text: 'ניתוח טכני'
            font_size: '20sp'
            size_hint_y: None
            height: '40dp'
            color: 0.2, 0.6, 1, 1
        
        ScrollView:
            GridLayout:
                id: analysis_grid
                cols: 1
                spacing: 10
                size_hint_y: None
                height: self.minimum_height
                padding: 10
        
        Button:
            text: 'חזרה'
            size_hint_y: None
            height: '50dp'
            background_color: 0.7, 0.7, 0.7, 1
            on_press: root.go_back()
'''

class LoginScreen(Screen):
    def login(self):
        username = self.ids.username.text
        password = self.ids.password.text
        
        if not username or not password:
            self.show_popup('שגיאה', 'אנא מלא את כל השדות')
            return
        
        # For demo purposes, accept any login
        # In real app, you would validate against server
        App.get_running_app().current_user = username
        self.manager.current = 'dashboard'
    
    def show_register(self):
        self.manager.current = 'register'
    
    def show_popup(self, title, message):
        popup = Popup(title=title, content=Label(text=message), size_hint=(None, None), size=(300, 200))
        popup.open()

class RegisterScreen(Screen):
    def register(self):
        username = self.ids.reg_username.text
        email = self.ids.reg_email.text
        password = self.ids.reg_password.text
        
        if not username or not email or not password:
            self.show_popup('שגיאה', 'אנא מלא את כל השדות')
            return
        
        # For demo purposes, accept any registration
        self.show_popup('הצלחה', 'הרשמה הושלמה בהצלחה!')
        self.manager.current = 'login'
    
    def go_back(self):
        self.manager.current = 'login'
    
    def show_popup(self, title, message):
        popup = Popup(title=title, content=Label(text=message), size_hint=(None, None), size=(300, 200))
        popup.open()

class DashboardScreen(Screen):
    def on_enter(self):
        self.load_market_data()
        self.load_portfolio()
    
    def load_market_data(self):
        # Sample market data
        market_data = [
            {'name': 'S&P 500', 'price': '4,500.25', 'change': '+0.5%'},
            {'name': 'Dow Jones', 'price': '35,000.50', 'change': '+0.3%'},
            {'name': 'NASDAQ', 'price': '14,200.75', 'change': '+0.8%'},
            {'name': 'VIX', 'price': '18.50', 'change': '-2.1%'}
        ]
        
        self.ids.market_grid.clear_widgets()
        
        for data in market_data:
            # Market card
            card = BoxLayout(orientation='vertical', size_hint_y=None, height=100)
            card.add_widget(Label(text=data['name'], font_size='16sp', color=(0.2, 0.2, 0.2, 1)))
            card.add_widget(Label(text=f"${data['price']}", font_size='18sp', bold=True))
            
            color = (0.3, 0.7, 0.3, 1) if '+' in data['change'] else (0.8, 0.3, 0.3, 1)
            card.add_widget(Label(text=data['change'], font_size='14sp', color=color))
            
            self.ids.market_grid.add_widget(card)
    
    def load_portfolio(self):
        # Sample portfolio data
        portfolio = [
            {'symbol': 'AAPL', 'name': 'Apple Inc.', 'price': '$150.25', 'change': '+2.5%'},
            {'symbol': 'TSLA', 'name': 'Tesla Inc.', 'price': '$250.75', 'change': '-1.2%'},
            {'symbol': 'MSFT', 'name': 'Microsoft', 'price': '$320.50', 'change': '+0.8%'}
        ]
        
        for stock in portfolio:
            # Stock card
            card = BoxLayout(orientation='vertical', size_hint_y=None, height=120)
            card.add_widget(Label(text=stock['symbol'], font_size='18sp', bold=True))
            card.add_widget(Label(text=stock['name'], font_size='14sp'))
            card.add_widget(Label(text=stock['price'], font_size='16sp'))
            
            color = (0.3, 0.7, 0.3, 1) if '+' in stock['change'] else (0.8, 0.3, 0.3, 1)
            card.add_widget(Label(text=stock['change'], font_size='14sp', color=color))
            
            # Add analysis button
            btn = Button(text='ניתוח טכני', size_hint_y=None, height=30, background_color=(0.2, 0.6, 1, 1))
            btn.bind(on_press=lambda x, s=stock: self.show_analysis(s))
            card.add_widget(btn)
            
            self.ids.market_grid.add_widget(card)
    
    def show_add_stock(self):
        self.manager.current = 'add_stock'
    
    def show_analysis(self, stock):
        App.get_running_app().current_stock = stock
        self.manager.current = 'analysis'
    
    def logout(self):
        App.get_running_app().current_user = None
        self.manager.current = 'login'

class AddStockScreen(Screen):
    def add_stock(self):
        symbol = self.ids.stock_symbol.text.upper()
        quantity = self.ids.stock_quantity.text
        price = self.ids.stock_price.text
        
        if not symbol or not quantity or not price:
            self.show_popup('שגיאה', 'אנא מלא את כל השדות')
            return
        
        try:
            float(quantity)
            float(price)
        except ValueError:
            self.show_popup('שגיאה', 'אנא הכנס מספרים תקינים')
            return
        
        self.show_popup('הצלחה', f'מניה {symbol} נוספה בהצלחה!')
        self.manager.current = 'dashboard'
    
    def go_back(self):
        self.manager.current = 'dashboard'
    
    def show_popup(self, title, message):
        popup = Popup(title=title, content=Label(text=message), size_hint=(None, None), size=(300, 200))
        popup.open()

class StockAnalysisScreen(Screen):
    def on_enter(self):
        stock = App.get_running_app().current_stock
        if not stock:
            return
        
        self.ids.analysis_grid.clear_widgets()
        
        # Stock info
        self.ids.analysis_grid.add_widget(Label(text=f"ניתוח טכני - {stock['symbol']}", font_size='18sp', bold=True))
        self.ids.analysis_grid.add_widget(Label(text=f"מחיר נוכחי: {stock['price']}", font_size='16sp'))
        self.ids.analysis_grid.add_widget(Label(text=f"שינוי: {stock['change']}", font_size='16sp'))
        
        # Technical indicators
        indicators = [
            ('RSI', '45.2', 'ניטרלי'),
            ('MACD', '0.25', 'חיובי'),
            ('SMA 20', '$148.50', 'מעל המחיר'),
            ('SMA 50', '$145.75', 'מעל המחיר'),
            ('פיבונצי 38.2%', '$147.25', 'תמיכה'),
            ('פיבונצי 61.8%', '$152.75', 'התנגדות')
        ]
        
        for name, value, status in indicators:
            indicator = BoxLayout(orientation='horizontal', size_hint_y=None, height=40)
            indicator.add_widget(Label(text=name, size_hint_x=0.4))
            indicator.add_widget(Label(text=value, size_hint_x=0.3))
            indicator.add_widget(Label(text=status, size_hint_x=0.3))
            self.ids.analysis_grid.add_widget(indicator)
        
        # Recommendation
        recommendation = "קנייה" if '+' in stock['change'] else "החזקה"
        color = (0.3, 0.7, 0.3, 1) if recommendation == "קנייה" else (0.8, 0.8, 0.3, 1)
        
        self.ids.analysis_grid.add_widget(Label(text="המלצה:", font_size='16sp', bold=True))
        self.ids.analysis_grid.add_widget(Label(text=recommendation, font_size='18sp', color=color, bold=True))
    
    def go_back(self):
        self.manager.current = 'dashboard'

class StockTrackerApp(App):
    current_user = None
    current_stock = None
    
    def build(self):
        Builder.load_string(KV)
        
        sm = ScreenManager()
        sm.add_widget(LoginScreen(name='login'))
        sm.add_widget(RegisterScreen(name='register'))
        sm.add_widget(DashboardScreen(name='dashboard'))
        sm.add_widget(AddStockScreen(name='add_stock'))
        sm.add_widget(StockAnalysisScreen(name='analysis'))
        
        return sm

if __name__ == '__main__':
    StockTrackerApp().run()