# API Reference

This document provides comprehensive documentation for all public APIs in the Stock Analysis project.

## Base URL

```
Production: https://api.stockanalysis.com/v1
Development: http://localhost:3000/api/v1
```

## Authentication

Most API endpoints require authentication. Include your API key in the request headers:

```http
Authorization: Bearer YOUR_API_KEY
```

## Rate Limits

- **Free Tier**: 100 requests per hour
- **Pro Tier**: 1000 requests per hour
- **Enterprise**: Custom limits

## Endpoints

### Stock Data

#### Get Stock Quote

Retrieves real-time stock quote information.

```http
GET /stocks/{symbol}/quote
```

**Parameters:**
- `symbol` (string, required): Stock symbol (e.g., AAPL, GOOGL)

**Response:**
```json
{
  "symbol": "AAPL",
  "companyName": "Apple Inc.",
  "currentPrice": 150.25,
  "change": 2.15,
  "changePercent": 1.45,
  "volume": 45678900,
  "marketCap": 2500000000000,
  "peRatio": 25.5,
  "dividendYield": 0.65,
  "timestamp": "2024-01-15T10:30:00Z"
}
```

**Example:**
```bash
curl -X GET "https://api.stockanalysis.com/v1/stocks/AAPL/quote" \
  -H "Authorization: Bearer YOUR_API_KEY"
```

#### Get Historical Data

Retrieves historical stock price data.

```http
GET /stocks/{symbol}/history
```

**Parameters:**
- `symbol` (string, required): Stock symbol
- `period` (string, optional): Time period (1d, 5d, 1mo, 3mo, 6mo, 1y, 2y, 5y, 10y, ytd, max)
- `interval` (string, optional): Data interval (1m, 2m, 5m, 15m, 30m, 60m, 90m, 1h, 1d, 5d, 1wk, 1mo, 3mo)

**Response:**
```json
{
  "symbol": "AAPL",
  "period": "1y",
  "interval": "1d",
  "data": [
    {
      "date": "2024-01-15",
      "open": 148.50,
      "high": 151.20,
      "low": 147.80,
      "close": 150.25,
      "volume": 45678900
    }
  ]
}
```

### Technical Analysis

#### Get Moving Averages

Calculates various moving averages for a stock.

```http
GET /stocks/{symbol}/indicators/moving-averages
```

**Parameters:**
- `symbol` (string, required): Stock symbol
- `periods` (array, optional): Array of periods [5, 10, 20, 50, 200]
- `type` (string, optional): Average type (sma, ema, wma)

**Response:**
```json
{
  "symbol": "AAPL",
  "indicators": {
    "sma": {
      "5": 149.20,
      "10": 148.75,
      "20": 147.30,
      "50": 145.80,
      "200": 140.25
    },
    "ema": {
      "12": 149.85,
      "26": 148.40
    }
  }
}
```

#### Get RSI (Relative Strength Index)

Calculates the RSI indicator.

```http
GET /stocks/{symbol}/indicators/rsi
```

**Parameters:**
- `symbol` (string, required): Stock symbol
- `period` (number, optional): RSI period (default: 14)

**Response:**
```json
{
  "symbol": "AAPL",
  "rsi": {
    "value": 65.5,
    "period": 14,
    "interpretation": "neutral"
  }
}
```

### Portfolio Management

#### Get Portfolio

Retrieves user portfolio information.

```http
GET /portfolio
```

**Response:**
```json
{
  "totalValue": 125000.50,
  "totalGain": 15250.25,
  "totalGainPercent": 13.9,
  "positions": [
    {
      "symbol": "AAPL",
      "shares": 100,
      "averagePrice": 135.50,
      "currentPrice": 150.25,
      "marketValue": 15025.00,
      "gain": 1475.00,
      "gainPercent": 10.9
    }
  ]
}
```

#### Add Position

Adds a new position to the portfolio.

```http
POST /portfolio/positions
```

**Request Body:**
```json
{
  "symbol": "GOOGL",
  "shares": 50,
  "purchasePrice": 2800.00,
  "purchaseDate": "2024-01-15"
}
```

**Response:**
```json
{
  "id": "pos_123456",
  "symbol": "GOOGL",
  "shares": 50,
  "purchasePrice": 2800.00,
  "purchaseDate": "2024-01-15",
  "createdAt": "2024-01-15T10:30:00Z"
}
```

### Market Data

#### Get Market Summary

Retrieves overall market summary data.

```http
GET /market/summary
```

**Response:**
```json
{
  "sp500": {
    "value": 4850.25,
    "change": 15.50,
    "changePercent": 0.32
  },
  "nasdaq": {
    "value": 15250.75,
    "change": 45.25,
    "changePercent": 0.30
  },
  "dow": {
    "value": 37500.50,
    "change": 125.75,
    "changePercent": 0.34
  },
  "vix": {
    "value": 12.5,
    "change": -0.5,
    "changePercent": -3.85
  }
}
```

#### Get Top Gainers/Losers

Retrieves top gaining and losing stocks.

```http
GET /market/top-movers
```

**Parameters:**
- `type` (string, optional): "gainers" or "losers" (default: both)

**Response:**
```json
{
  "gainers": [
    {
      "symbol": "TSLA",
      "companyName": "Tesla Inc.",
      "price": 250.75,
      "change": 25.50,
      "changePercent": 11.32
    }
  ],
  "losers": [
    {
      "symbol": "NFLX",
      "companyName": "Netflix Inc.",
      "price": 485.25,
      "change": -15.75,
      "changePercent": -3.14
    }
  ]
}
```

## Error Handling

All API endpoints return consistent error responses:

```json
{
  "error": {
    "code": "INVALID_SYMBOL",
    "message": "The provided stock symbol is invalid",
    "details": {
      "symbol": "INVALID"
    }
  }
}
```

### Common Error Codes

- `INVALID_API_KEY`: API key is missing or invalid
- `RATE_LIMIT_EXCEEDED`: Rate limit exceeded
- `INVALID_SYMBOL`: Stock symbol not found
- `INVALID_PARAMETER`: Request parameter is invalid
- `SERVER_ERROR`: Internal server error

## SDKs and Libraries

### JavaScript/Node.js

```bash
npm install stock-analysis-sdk
```

```javascript
import { StockAnalysisAPI } from 'stock-analysis-sdk';

const api = new StockAnalysisAPI('YOUR_API_KEY');

// Get stock quote
const quote = await api.getStockQuote('AAPL');

// Get historical data
const history = await api.getHistoricalData('AAPL', {
  period: '1y',
  interval: '1d'
});
```

### Python

```bash
pip install stock-analysis-python
```

```python
from stock_analysis import StockAnalysisAPI

api = StockAnalysisAPI('YOUR_API_KEY')

# Get stock quote
quote = api.get_stock_quote('AAPL')

# Get historical data
history = api.get_historical_data('AAPL', period='1y', interval='1d')
```

## Webhooks

Configure webhooks to receive real-time updates:

```http
POST /webhooks
```

**Request Body:**
```json
{
  "url": "https://your-app.com/webhook",
  "events": ["price_change", "volume_spike"],
  "symbols": ["AAPL", "GOOGL"]
}
```

**Webhook Payload:**
```json
{
  "event": "price_change",
  "symbol": "AAPL",
  "data": {
    "previousPrice": 149.50,
    "currentPrice": 150.25,
    "change": 0.75,
    "changePercent": 0.50
  },
  "timestamp": "2024-01-15T10:30:00Z"
}
```