# Examples and Usage Instructions

This document provides comprehensive examples and usage instructions for the Stock Analysis project APIs, components, and features.

## API Usage Examples

### JavaScript/Node.js SDK

#### Basic Setup

```javascript
import { StockAnalysisAPI } from 'stock-analysis-sdk';

// Initialize the API client
const api = new StockAnalysisAPI('YOUR_API_KEY');

// Set default options
api.setDefaultOptions({
  timeout: 10000,
  retries: 3,
  cache: true
});
```

#### Stock Data Examples

**Get Real-time Stock Quote**

```javascript
// Get current stock quote
const quote = await api.getStockQuote('AAPL');
console.log(`${quote.symbol}: $${quote.currentPrice} (${quote.changePercent}%)`);

// Get multiple stock quotes
const symbols = ['AAPL', 'GOOGL', 'MSFT', 'TSLA'];
const quotes = await api.getStockQuotes(symbols);

quotes.forEach(quote => {
  console.log(`${quote.symbol}: $${quote.currentPrice}`);
});
```

**Get Historical Data**

```javascript
// Get 1 year of daily data
const history = await api.getHistoricalData('AAPL', {
  period: '1y',
  interval: '1d'
});

// Process the data
const prices = history.data.map(point => ({
  date: point.date,
  close: point.close,
  volume: point.volume
}));

// Get intraday data (5-minute intervals)
const intraday = await api.getHistoricalData('AAPL', {
  period: '1d',
  interval: '5m'
});
```

**Get Company Information**

```javascript
const companyInfo = await api.getCompanyInfo('AAPL');
console.log(`${companyInfo.companyName} (${companyInfo.sector})`);
console.log(`Market Cap: $${(companyInfo.marketCap / 1e9).toFixed(2)}B`);
console.log(`Employees: ${companyInfo.employees.toLocaleString()}`);
```

#### Technical Analysis Examples

**Calculate Moving Averages**

```javascript
// Get moving averages for different periods
const indicators = await api.getTechnicalIndicators('AAPL', {
  indicators: ['sma', 'ema'],
  periods: [5, 10, 20, 50, 200]
});

console.log('Simple Moving Averages:');
Object.entries(indicators.movingAverages.sma).forEach(([period, value]) => {
  console.log(`SMA(${period}): $${value.toFixed(2)}`);
});

console.log('Exponential Moving Averages:');
Object.entries(indicators.movingAverages.ema).forEach(([period, value]) => {
  console.log(`EMA(${period}): $${value.toFixed(2)}`);
});
```

**Calculate RSI**

```javascript
const rsi = await api.getRSI('AAPL', { period: 14 });
console.log(`RSI: ${rsi.value.toFixed(2)}`);
console.log(`Interpretation: ${rsi.interpretation}`);
console.log(`Signal: ${rsi.signal}`);
```

**Calculate MACD**

```javascript
const macd = await api.getMACD('AAPL');
console.log(`MACD: ${macd.value.toFixed(2)}`);
console.log(`Signal: ${macd.signal.toFixed(2)}`);
console.log(`Histogram: ${macd.histogram.toFixed(2)}`);
console.log(`Interpretation: ${macd.interpretation}`);
```

**Get Multiple Indicators**

```javascript
const allIndicators = await api.getTechnicalIndicators('AAPL', {
  indicators: ['rsi', 'macd', 'bollinger_bands', 'stochastic']
});

// Analyze RSI
if (allIndicators.rsi.value < 30) {
  console.log('Stock is oversold - potential buy signal');
} else if (allIndicators.rsi.value > 70) {
  console.log('Stock is overbought - potential sell signal');
}

// Analyze Bollinger Bands
const bb = allIndicators.bollingerBands;
const currentPrice = await api.getStockQuote('AAPL');
if (currentPrice.currentPrice < bb.lower) {
  console.log('Price below lower Bollinger Band - potential buy');
} else if (currentPrice.currentPrice > bb.upper) {
  console.log('Price above upper Bollinger Band - potential sell');
}
```

#### Portfolio Management Examples

**Get Portfolio**

```javascript
const portfolio = await api.getPortfolio();
console.log(`Portfolio Value: $${portfolio.totalValue.toLocaleString()}`);
console.log(`Total Gain: $${portfolio.totalGain.toLocaleString()} (${portfolio.totalGainPercent}%)`);

// Display positions
portfolio.positions.forEach(position => {
  const gainColor = position.gain >= 0 ? 'green' : 'red';
  console.log(`${position.symbol}: ${position.shares} shares @ $${position.averagePrice}`);
  console.log(`  Current: $${position.currentPrice} | Gain: ${gainColor}${position.gainPercent}%`);
});
```

**Add Position**

```javascript
const newPosition = await api.addPosition({
  symbol: 'GOOGL',
  shares: 10,
  purchasePrice: 2800.00,
  purchaseDate: '2024-01-15'
});

console.log(`Added ${newPosition.shares} shares of ${newPosition.symbol}`);
```

**Update Position**

```javascript
const updatedPosition = await api.updatePosition('pos_123456', {
  shares: 15,
  purchasePrice: 2750.00
});

console.log(`Updated position: ${updatedPosition.shares} shares @ $${updatedPosition.purchasePrice}`);
```

**Delete Position**

```javascript
await api.deletePosition('pos_123456');
console.log('Position deleted successfully');
```

#### Market Data Examples

**Get Market Summary**

```javascript
const marketSummary = await api.getMarketSummary();
console.log('Market Summary:');
console.log(`S&P 500: ${marketSummary.sp500.value} (${marketSummary.sp500.changePercent}%)`);
console.log(`NASDAQ: ${marketSummary.nasdaq.value} (${marketSummary.nasdaq.changePercent}%)`);
console.log(`DOW: ${marketSummary.dow.value} (${marketSummary.dow.changePercent}%)`);
console.log(`VIX: ${marketSummary.vix.value} (${marketSummary.vix.changePercent}%)`);
```

**Get Top Movers**

```javascript
const topMovers = await api.getTopMovers();

console.log('Top Gainers:');
topMovers.gainers.slice(0, 5).forEach(stock => {
  console.log(`${stock.symbol}: +${stock.changePercent}%`);
});

console.log('Top Losers:');
topMovers.losers.slice(0, 5).forEach(stock => {
  console.log(`${stock.symbol}: ${stock.changePercent}%`);
});
```

#### News and Sentiment Examples

**Get News Articles**

```javascript
// Get news for a specific stock
const news = await api.getNews('AAPL', { limit: 10 });

news.forEach(article => {
  console.log(`${article.title} (${article.source})`);
  console.log(`Sentiment: ${article.sentiment} (${article.sentimentScore})`);
  console.log(`Published: ${new Date(article.publishedAt).toLocaleDateString()}`);
  console.log('---');
});
```

**Get Sentiment Analysis**

```javascript
const sentiment = await api.getSentimentAnalysis('AAPL');
console.log(`Overall Sentiment: ${sentiment.overallSentiment}`);
console.log(`Sentiment Score: ${sentiment.sentimentScore}`);
console.log(`Confidence: ${(sentiment.confidence * 100).toFixed(1)}%`);
```

#### Alert Management Examples

**Create Price Alert**

```javascript
const alert = await api.createAlert({
  symbol: 'AAPL',
  type: 'price_above',
  value: 160.00,
  notificationType: 'email',
  frequency: 'once'
});

console.log(`Alert created: ${alert.id}`);
```

**Create Technical Signal Alert**

```javascript
const technicalAlert = await api.createAlert({
  symbol: 'AAPL',
  type: 'technical_signal',
  value: 30, // RSI threshold
  conditions: [
    {
      field: 'rsi',
      operator: 'less_than',
      value: 30
    }
  ],
  notificationType: 'push',
  frequency: 'recurring'
});
```

**Get User Alerts**

```javascript
const alerts = await api.getAlerts();
alerts.forEach(alert => {
  console.log(`${alert.symbol} ${alert.type} ${alert.value} (${alert.isActive ? 'Active' : 'Inactive'})`);
});
```

### Python SDK

#### Basic Setup

```python
from stock_analysis import StockAnalysisAPI

# Initialize the API client
api = StockAnalysisAPI('YOUR_API_KEY')

# Set default options
api.set_default_options(
    timeout=10000,
    retries=3,
    cache=True
)
```

#### Stock Data Examples

**Get Real-time Stock Quote**

```python
# Get current stock quote
quote = api.get_stock_quote('AAPL')
print(f"{quote['symbol']}: ${quote['currentPrice']} ({quote['changePercent']}%)")

# Get multiple stock quotes
symbols = ['AAPL', 'GOOGL', 'MSFT', 'TSLA']
quotes = api.get_stock_quotes(symbols)

for quote in quotes:
    print(f"{quote['symbol']}: ${quote['currentPrice']}")
```

**Get Historical Data**

```python
# Get 1 year of daily data
history = api.get_historical_data('AAPL', period='1y', interval='1d')

# Process the data
prices = [
    {
        'date': point['date'],
        'close': point['close'],
        'volume': point['volume']
    }
    for point in history['data']
]

# Calculate simple statistics
close_prices = [p['close'] for p in prices]
avg_price = sum(close_prices) / len(close_prices)
print(f"Average closing price: ${avg_price:.2f}")
```

#### Technical Analysis Examples

**Calculate Moving Averages**

```python
import pandas as pd

# Get historical data
history = api.get_historical_data('AAPL', period='1y', interval='1d')
df = pd.DataFrame(history['data'])

# Calculate SMA manually
df['SMA_20'] = df['close'].rolling(window=20).mean()
df['SMA_50'] = df['close'].rolling(window=50).mean()

# Get technical indicators from API
indicators = api.get_technical_indicators('AAPL', indicators=['sma', 'ema'])

print("Simple Moving Averages:")
for period, value in indicators['movingAverages']['sma'].items():
    print(f"SMA({period}): ${value:.2f}")
```

**Calculate RSI**

```python
def calculate_rsi(prices, period=14):
    delta = prices.diff()
    gain = (delta.where(delta > 0, 0)).rolling(window=period).mean()
    loss = (-delta.where(delta < 0, 0)).rolling(window=period).mean()
    rs = gain / loss
    rsi = 100 - (100 / (1 + rs))
    return rsi

# Get historical data and calculate RSI
history = api.get_historical_data('AAPL', period='1y', interval='1d')
df = pd.DataFrame(history['data'])
df['RSI'] = calculate_rsi(df['close'])

# Get RSI from API
rsi_data = api.get_rsi('AAPL', period=14)
print(f"RSI: {rsi_data['value']:.2f}")
print(f"Interpretation: {rsi_data['interpretation']}")
```

### React Component Examples

#### StockChart Component

```tsx
import React, { useState, useEffect } from 'react';
import { StockChart } from '@/components/StockChart';
import { StockAnalysisAPI } from 'stock-analysis-sdk';

const StockChartExample: React.FC = () => {
  const [chartData, setChartData] = useState([]);
  const [loading, setLoading] = useState(true);
  const [selectedIndicators, setSelectedIndicators] = useState(['sma', 'ema']);

  const api = new StockAnalysisAPI('YOUR_API_KEY');

  useEffect(() => {
    const fetchData = async () => {
      try {
        const history = await api.getHistoricalData('AAPL', {
          period: '1y',
          interval: '1d'
        });
        setChartData(history.data);
      } catch (error) {
        console.error('Error fetching data:', error);
      } finally {
        setLoading(false);
      }
    };

    fetchData();
  }, []);

  const handleDataPointClick = (point: any) => {
    console.log('Clicked data point:', point);
  };

  if (loading) {
    return <div>Loading chart data...</div>;
  }

  return (
    <div>
      <h2>AAPL Stock Chart</h2>
      <StockChart
        data={chartData}
        indicators={selectedIndicators}
        height={400}
        width={800}
        theme="dark"
        showVolume={true}
        onDataPointClick={handleDataPointClick}
      />
      
      <div>
        <label>
          <input
            type="checkbox"
            checked={selectedIndicators.includes('sma')}
            onChange={(e) => {
              if (e.target.checked) {
                setSelectedIndicators([...selectedIndicators, 'sma']);
              } else {
                setSelectedIndicators(selectedIndicators.filter(i => i !== 'sma'));
              }
            }}
          />
          Show SMA
        </label>
        
        <label>
          <input
            type="checkbox"
            checked={selectedIndicators.includes('ema')}
            onChange={(e) => {
              if (e.target.checked) {
                setSelectedIndicators([...selectedIndicators, 'ema']);
              } else {
                setSelectedIndicators(selectedIndicators.filter(i => i !== 'ema'));
              }
            }}
          />
          Show EMA
        </label>
      </div>
    </div>
  );
};

export default StockChartExample;
```

#### Portfolio Dashboard

```tsx
import React, { useState, useEffect } from 'react';
import { PortfolioCard } from '@/components/PortfolioCard';
import { StockQuote } from '@/components/StockQuote';
import { StockAnalysisAPI } from 'stock-analysis-sdk';

const PortfolioDashboard: React.FC = () => {
  const [portfolio, setPortfolio] = useState(null);
  const [loading, setLoading] = useState(true);
  const [selectedPosition, setSelectedPosition] = useState(null);

  const api = new StockAnalysisAPI('YOUR_API_KEY');

  useEffect(() => {
    const fetchPortfolio = async () => {
      try {
        const data = await api.getPortfolio();
        setPortfolio(data);
      } catch (error) {
        console.error('Error fetching portfolio:', error);
      } finally {
        setLoading(false);
      }
    };

    fetchPortfolio();
  }, []);

  const handlePositionClick = (position: any) => {
    setSelectedPosition(position);
  };

  const handleEditPosition = async (positionId: string) => {
    // Open edit modal or navigate to edit page
    console.log('Edit position:', positionId);
  };

  const handleDeletePosition = async (positionId: string) => {
    if (window.confirm('Are you sure you want to delete this position?')) {
      try {
        await api.deletePosition(positionId);
        // Refresh portfolio data
        const updatedPortfolio = await api.getPortfolio();
        setPortfolio(updatedPortfolio);
      } catch (error) {
        console.error('Error deleting position:', error);
      }
    }
  };

  if (loading) {
    return <div>Loading portfolio...</div>;
  }

  return (
    <div className="portfolio-dashboard">
      <div className="portfolio-summary">
        <h2>Portfolio Summary</h2>
        <div className="summary-stats">
          <div className="stat">
            <label>Total Value:</label>
            <span>${portfolio.totalValue.toLocaleString()}</span>
          </div>
          <div className="stat">
            <label>Total Gain:</label>
            <span className={portfolio.totalGain >= 0 ? 'positive' : 'negative'}>
              ${portfolio.totalGain.toLocaleString()} ({portfolio.totalGainPercent}%)
            </span>
          </div>
          <div className="stat">
            <label>Cash:</label>
            <span>${portfolio.cash.toLocaleString()}</span>
          </div>
        </div>
      </div>

      <div className="positions-grid">
        {portfolio.positions.map((position) => (
          <PortfolioCard
            key={position.id}
            position={position}
            onEdit={() => handleEditPosition(position.id)}
            onDelete={() => handleDeletePosition(position.id)}
            onClick={() => handlePositionClick(position)}
          />
        ))}
      </div>

      {selectedPosition && (
        <div className="position-detail">
          <h3>{selectedPosition.symbol} Details</h3>
          <StockQuote
            symbol={selectedPosition.symbol}
            quote={{
              symbol: selectedPosition.symbol,
              currentPrice: selectedPosition.currentPrice,
              change: 0, // You would fetch this from API
              changePercent: 0,
              volume: 0,
              marketCap: 0,
              peRatio: 0,
              dividendYield: 0,
              timestamp: new Date().toISOString()
            }}
            showDetails={true}
          />
        </div>
      )}
    </div>
  );
};

export default PortfolioDashboard;
```

#### Watchlist Component

```tsx
import React, { useState, useEffect } from 'react';
import { Watchlist } from '@/components/Watchlist';
import { SearchBar } from '@/components/SearchBar';
import { StockAnalysisAPI } from 'stock-analysis-sdk';

const WatchlistExample: React.FC = () => {
  const [watchlist, setWatchlist] = useState([]);
  const [suggestions, setSuggestions] = useState([]);
  const [loading, setLoading] = useState(true);

  const api = new StockAnalysisAPI('YOUR_API_KEY');

  useEffect(() => {
    const fetchWatchlist = async () => {
      try {
        const data = await api.getWatchlist();
        setWatchlist(data);
      } catch (error) {
        console.error('Error fetching watchlist:', error);
      } finally {
        setLoading(false);
      }
    };

    fetchWatchlist();
  }, []);

  const handleSearch = async (query: string) => {
    if (query.length < 2) {
      setSuggestions([]);
      return;
    }

    try {
      const results = await api.searchStocks(query);
      setSuggestions(results.slice(0, 5));
    } catch (error) {
      console.error('Error searching stocks:', error);
    }
  };

  const handleSuggestionSelect = async (suggestion: any) => {
    try {
      await api.addToWatchlist(suggestion.symbol);
      // Refresh watchlist
      const updatedWatchlist = await api.getWatchlist();
      setWatchlist(updatedWatchlist);
      setSuggestions([]);
    } catch (error) {
      console.error('Error adding to watchlist:', error);
    }
  };

  const handleRemoveStock = async (symbol: string) => {
    try {
      await api.removeFromWatchlist(symbol);
      // Refresh watchlist
      const updatedWatchlist = await api.getWatchlist();
      setWatchlist(updatedWatchlist);
    } catch (error) {
      console.error('Error removing from watchlist:', error);
    }
  };

  const handleStockClick = (symbol: string) => {
    // Navigate to stock detail page
    window.location.href = `/stock/${symbol}`;
  };

  if (loading) {
    return <div>Loading watchlist...</div>;
  }

  return (
    <div className="watchlist-container">
      <h2>My Watchlist</h2>
      
      <div className="search-section">
        <SearchBar
          onSearch={handleSearch}
          placeholder="Search stocks to add..."
          suggestions={suggestions}
          onSuggestionSelect={handleSuggestionSelect}
          debounceMs={300}
          minQueryLength={2}
        />
      </div>

      <Watchlist
        stocks={watchlist}
        onAddStock={handleSuggestionSelect}
        onRemoveStock={handleRemoveStock}
        onStockClick={handleStockClick}
        maxStocks={20}
        showAddButton={false}
      />
    </div>
  );
};

export default WatchlistExample;
```

#### Alert Manager

```tsx
import React, { useState, useEffect } from 'react';
import { AlertManager } from '@/components/AlertManager';
import { Modal } from '@/components/Modal';
import { StockAnalysisAPI } from 'stock-analysis-sdk';

const AlertManagerExample: React.FC = () => {
  const [alerts, setAlerts] = useState([]);
  const [showCreateForm, setShowCreateForm] = useState(false);
  const [loading, setLoading] = useState(true);

  const api = new StockAnalysisAPI('YOUR_API_KEY');

  useEffect(() => {
    const fetchAlerts = async () => {
      try {
        const data = await api.getAlerts();
        setAlerts(data);
      } catch (error) {
        console.error('Error fetching alerts:', error);
      } finally {
        setLoading(false);
      }
    };

    fetchAlerts();
  }, []);

  const handleCreateAlert = async (alertData: any) => {
    try {
      const newAlert = await api.createAlert(alertData);
      setAlerts([...alerts, newAlert]);
      setShowCreateForm(false);
    } catch (error) {
      console.error('Error creating alert:', error);
    }
  };

  const handleEditAlert = async (alert: any) => {
    try {
      const updatedAlert = await api.updateAlert(alert.id, alert);
      setAlerts(alerts.map(a => a.id === alert.id ? updatedAlert : a));
    } catch (error) {
      console.error('Error updating alert:', error);
    }
  };

  const handleDeleteAlert = async (alertId: string) => {
    try {
      await api.deleteAlert(alertId);
      setAlerts(alerts.filter(a => a.id !== alertId));
    } catch (error) {
      console.error('Error deleting alert:', error);
    }
  };

  if (loading) {
    return <div>Loading alerts...</div>;
  }

  return (
    <div className="alert-manager">
      <div className="alert-header">
        <h2>Price Alerts</h2>
        <button 
          className="btn btn-primary"
          onClick={() => setShowCreateForm(true)}
        >
          Create New Alert
        </button>
      </div>

      <AlertManager
        alerts={alerts}
        onCreateAlert={handleCreateAlert}
        onEditAlert={handleEditAlert}
        onDeleteAlert={handleDeleteAlert}
        showCreateForm={showCreateForm}
      />

      <Modal
        isOpen={showCreateForm}
        onClose={() => setShowCreateForm(false)}
        title="Create Price Alert"
        size="medium"
      >
        <AlertCreateForm
          onSubmit={handleCreateAlert}
          onCancel={() => setShowCreateForm(false)}
        />
      </Modal>
    </div>
  );
};

// Alert Create Form Component
const AlertCreateForm: React.FC<{
  onSubmit: (alert: any) => void;
  onCancel: () => void;
}> = ({ onSubmit, onCancel }) => {
  const [formData, setFormData] = useState({
    symbol: '',
    type: 'price_above',
    value: '',
    notificationType: 'email',
    frequency: 'once'
  });

  const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault();
    onSubmit({
      ...formData,
      value: parseFloat(formData.value)
    });
  };

  return (
    <form onSubmit={handleSubmit}>
      <div className="form-group">
        <label>Stock Symbol:</label>
        <input
          type="text"
          value={formData.symbol}
          onChange={(e) => setFormData({...formData, symbol: e.target.value.toUpperCase()})}
          placeholder="AAPL"
          required
        />
      </div>

      <div className="form-group">
        <label>Alert Type:</label>
        <select
          value={formData.type}
          onChange={(e) => setFormData({...formData, type: e.target.value})}
        >
          <option value="price_above">Price Above</option>
          <option value="price_below">Price Below</option>
          <option value="percent_change">Percent Change</option>
        </select>
      </div>

      <div className="form-group">
        <label>Value:</label>
        <input
          type="number"
          value={formData.value}
          onChange={(e) => setFormData({...formData, value: e.target.value})}
          placeholder="150.00"
          step="0.01"
          required
        />
      </div>

      <div className="form-group">
        <label>Notification Type:</label>
        <select
          value={formData.notificationType}
          onChange={(e) => setFormData({...formData, notificationType: e.target.value})}
        >
          <option value="email">Email</option>
          <option value="push">Push Notification</option>
          <option value="sms">SMS</option>
        </select>
      </div>

      <div className="form-actions">
        <button type="button" onClick={onCancel} className="btn btn-secondary">
          Cancel
        </button>
        <button type="submit" className="btn btn-primary">
          Create Alert
        </button>
      </div>
    </form>
  );
};

export default AlertManagerExample;
```

## Webhook Integration Examples

### Setting up Webhooks

```javascript
// Create webhook subscription
const webhook = await api.createWebhook({
  url: 'https://your-app.com/webhook',
  events: ['price_change', 'volume_spike', 'technical_signal'],
  symbols: ['AAPL', 'GOOGL', 'MSFT']
});

console.log(`Webhook created: ${webhook.id}`);
```

### Webhook Endpoint Handler

```javascript
// Express.js webhook handler
app.post('/webhook', (req, res) => {
  const { event, symbol, data, timestamp } = req.body;

  switch (event) {
    case 'price_change':
      handlePriceChange(symbol, data);
      break;
    case 'volume_spike':
      handleVolumeSpike(symbol, data);
      break;
    case 'technical_signal':
      handleTechnicalSignal(symbol, data);
      break;
  }

  res.status(200).json({ received: true });
});

function handlePriceChange(symbol, data) {
  console.log(`${symbol} price changed: ${data.previousPrice} -> ${data.currentPrice}`);
  
  // Send notification to user
  if (data.changePercent > 5) {
    sendNotification(`Large price movement detected for ${symbol}`);
  }
}

function handleVolumeSpike(symbol, data) {
  console.log(`${symbol} volume spike: ${data.volume} (${data.percentChange}% increase)`);
}

function handleTechnicalSignal(symbol, data) {
  console.log(`${symbol} technical signal: ${data.signal} (${data.indicator})`);
}
```

## Error Handling Examples

### Comprehensive Error Handling

```javascript
class StockAnalysisClient {
  constructor(apiKey) {
    this.api = new StockAnalysisAPI(apiKey);
  }

  async getStockQuote(symbol) {
    try {
      const quote = await this.api.getStockQuote(symbol);
      return quote;
    } catch (error) {
      if (error.code === 'INVALID_SYMBOL') {
        throw new Error(`Invalid stock symbol: ${symbol}`);
      } else if (error.code === 'RATE_LIMIT_EXCEEDED') {
        throw new Error('Rate limit exceeded. Please try again later.');
      } else if (error.code === 'API_KEY_INVALID') {
        throw new Error('Invalid API key. Please check your credentials.');
      } else {
        throw new Error(`Failed to fetch stock quote: ${error.message}`);
      }
    }
  }

  async getHistoricalData(symbol, options = {}) {
    try {
      const data = await this.api.getHistoricalData(symbol, options);
      return data;
    } catch (error) {
      console.error('Error fetching historical data:', error);
      
      // Retry logic for transient errors
      if (error.code === 'TIMEOUT' || error.code === 'NETWORK_ERROR') {
        return this.retry(() => this.api.getHistoricalData(symbol, options), 3);
      }
      
      throw error;
    }
  }

  async retry(fn, maxRetries) {
    for (let i = 0; i < maxRetries; i++) {
      try {
        return await fn();
      } catch (error) {
        if (i === maxRetries - 1) throw error;
        await new Promise(resolve => setTimeout(resolve, 1000 * (i + 1)));
      }
    }
  }
}
```

## Performance Optimization Examples

### Caching Implementation

```javascript
class CachedStockAnalysisAPI {
  constructor(apiKey) {
    this.api = new StockAnalysisAPI(apiKey);
    this.cache = new Map();
    this.cacheTimeout = 5 * 60 * 1000; // 5 minutes
  }

  async getStockQuote(symbol) {
    const cacheKey = `quote_${symbol}`;
    const cached = this.cache.get(cacheKey);
    
    if (cached && Date.now() - cached.timestamp < this.cacheTimeout) {
      return cached.data;
    }

    const quote = await this.api.getStockQuote(symbol);
    this.cache.set(cacheKey, {
      data: quote,
      timestamp: Date.now()
    });

    return quote;
  }

  async getHistoricalData(symbol, options = {}) {
    const cacheKey = `history_${symbol}_${JSON.stringify(options)}`;
    const cached = this.cache.get(cacheKey);
    
    if (cached && Date.now() - cached.timestamp < this.cacheTimeout) {
      return cached.data;
    }

    const data = await this.api.getHistoricalData(symbol, options);
    this.cache.set(cacheKey, {
      data: data,
      timestamp: Date.now()
    });

    return data;
  }

  clearCache() {
    this.cache.clear();
  }
}
```

### Batch Processing

```javascript
class BatchStockAnalysisAPI {
  constructor(apiKey) {
    this.api = new StockAnalysisAPI(apiKey);
    this.batchSize = 10;
    this.batchDelay = 100; // ms between batches
  }

  async getStockQuotesBatch(symbols) {
    const results = [];
    
    for (let i = 0; i < symbols.length; i += this.batchSize) {
      const batch = symbols.slice(i, i + this.batchSize);
      
      try {
        const batchResults = await this.api.getStockQuotes(batch);
        results.push(...batchResults);
      } catch (error) {
        console.error(`Error fetching batch ${i / this.batchSize + 1}:`, error);
        // Add null values for failed requests
        results.push(...new Array(batch.length).fill(null));
      }
      
      // Add delay between batches to respect rate limits
      if (i + this.batchSize < symbols.length) {
        await new Promise(resolve => setTimeout(resolve, this.batchDelay));
      }
    }
    
    return results;
  }
}
```

## Testing Examples

### Unit Tests

```javascript
import { render, screen, fireEvent, waitFor } from '@testing-library/react';
import { StockQuote } from '@/components/StockQuote';

describe('StockQuote Component', () => {
  const mockQuote = {
    symbol: 'AAPL',
    companyName: 'Apple Inc.',
    currentPrice: 150.25,
    change: 2.15,
    changePercent: 1.45,
    volume: 45678900,
    marketCap: 2500000000000,
    peRatio: 25.5,
    dividendYield: 0.65,
    timestamp: '2024-01-15T10:30:00Z'
  };

  test('renders stock quote with correct data', () => {
    render(<StockQuote symbol="AAPL" quote={mockQuote} />);
    
    expect(screen.getByText('AAPL')).toBeInTheDocument();
    expect(screen.getByText('$150.25')).toBeInTheDocument();
    expect(screen.getByText('+2.15 (1.45%)')).toBeInTheDocument();
    expect(screen.getByText('Apple Inc.')).toBeInTheDocument();
  });

  test('handles refresh button click', async () => {
    const mockRefresh = jest.fn();
    render(<StockQuote symbol="AAPL" quote={mockQuote} onRefresh={mockRefresh} />);
    
    const refreshButton = screen.getByRole('button', { name: /refresh/i });
    fireEvent.click(refreshButton);
    
    expect(mockRefresh).toHaveBeenCalledTimes(1);
  });

  test('shows loading state when quote is null', () => {
    render(<StockQuote symbol="AAPL" quote={null} />);
    
    expect(screen.getByText(/loading/i)).toBeInTheDocument();
  });
});
```

### Integration Tests

```javascript
import { StockAnalysisAPI } from 'stock-analysis-sdk';

describe('Stock Analysis API Integration', () => {
  let api;

  beforeAll(() => {
    api = new StockAnalysisAPI(process.env.TEST_API_KEY);
  });

  test('fetches stock quote successfully', async () => {
    const quote = await api.getStockQuote('AAPL');
    
    expect(quote).toHaveProperty('symbol', 'AAPL');
    expect(quote).toHaveProperty('currentPrice');
    expect(quote).toHaveProperty('change');
    expect(quote).toHaveProperty('changePercent');
    expect(typeof quote.currentPrice).toBe('number');
  });

  test('fetches historical data successfully', async () => {
    const history = await api.getHistoricalData('AAPL', {
      period: '1mo',
      interval: '1d'
    });
    
    expect(history).toHaveProperty('symbol', 'AAPL');
    expect(history).toHaveProperty('data');
    expect(Array.isArray(history.data)).toBe(true);
    expect(history.data.length).toBeGreaterThan(0);
    
    const firstDataPoint = history.data[0];
    expect(firstDataPoint).toHaveProperty('date');
    expect(firstDataPoint).toHaveProperty('close');
    expect(firstDataPoint).toHaveProperty('volume');
  });

  test('handles invalid symbol gracefully', async () => {
    await expect(api.getStockQuote('INVALID')).rejects.toThrow();
  });
});
```