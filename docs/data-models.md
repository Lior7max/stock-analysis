# Data Models

This document provides comprehensive documentation for all data models, interfaces, and types used in the Stock Analysis project.

## Core Data Types

### Stock Data

#### StockQuote

Represents real-time stock quote information.

```typescript
interface StockQuote {
  symbol: string;
  companyName: string;
  currentPrice: number;
  change: number;
  changePercent: number;
  volume: number;
  marketCap: number;
  peRatio: number;
  dividendYield: number;
  timestamp: string;
  exchange: string;
  currency: string;
  previousClose: number;
  open: number;
  dayHigh: number;
  dayLow: number;
  yearHigh: number;
  yearLow: number;
  beta: number;
  eps: number;
  forwardPE: number;
  priceToBook: number;
  priceToSales: number;
  enterpriseValue: number;
  debtToEquity: number;
  returnOnEquity: number;
  returnOnAssets: number;
  profitMargin: number;
  operatingMargin: number;
  grossMargin: number;
}
```

#### StockData

Represents historical stock price data point.

```typescript
interface StockData {
  date: string;
  open: number;
  high: number;
  low: number;
  close: number;
  volume: number;
  adjustedClose?: number;
  dividendAmount?: number;
  splitCoefficient?: number;
}
```

#### StockInfo

Basic stock information.

```typescript
interface StockInfo {
  symbol: string;
  companyName: string;
  sector: string;
  industry: string;
  exchange: string;
  marketCap: number;
  employees: number;
  website: string;
  description: string;
  ceo: string;
  founded: number;
  headquarters: string;
  phone: string;
  email: string;
}
```

### Technical Analysis

#### MovingAverages

Moving average calculations.

```typescript
interface MovingAverages {
  sma: Record<number, number>; // Simple Moving Average
  ema: Record<number, number>; // Exponential Moving Average
  wma: Record<number, number>; // Weighted Moving Average
  vwap?: number; // Volume Weighted Average Price
}
```

#### RSI

Relative Strength Index data.

```typescript
interface RSI {
  value: number;
  period: number;
  interpretation: 'oversold' | 'neutral' | 'overbought';
  signal: 'buy' | 'sell' | 'hold';
  strength: number; // 0-100
}
```

#### MACD

Moving Average Convergence Divergence data.

```typescript
interface MACD {
  value: number;
  signal: number;
  histogram: number;
  interpretation: 'bullish' | 'bearish' | 'neutral';
  crossover: 'bullish' | 'bearish' | 'none';
}
```

#### BollingerBands

Bollinger Bands data.

```typescript
interface BollingerBands {
  upper: number;
  middle: number;
  lower: number;
  bandwidth: number;
  percentB: number;
  interpretation: 'squeeze' | 'expansion' | 'normal';
}
```

#### TechnicalIndicators

Complete technical analysis data.

```typescript
interface TechnicalIndicators {
  rsi: RSI;
  movingAverages: MovingAverages;
  macd: MACD;
  bollingerBands: BollingerBands;
  stochastic: Stochastic;
  williamsR: WilliamsR;
  adx: ADX;
  obv: number; // On-Balance Volume
  aroon: Aroon;
  cci: number; // Commodity Channel Index
  mfi: number; // Money Flow Index
  roc: number; // Rate of Change
}
```

#### Stochastic

Stochastic oscillator data.

```typescript
interface Stochastic {
  k: number;
  d: number;
  interpretation: 'oversold' | 'overbought' | 'neutral';
  signal: 'buy' | 'sell' | 'hold';
}
```

#### WilliamsR

Williams %R data.

```typescript
interface WilliamsR {
  value: number;
  interpretation: 'oversold' | 'overbought' | 'neutral';
  signal: 'buy' | 'sell' | 'hold';
}
```

#### ADX

Average Directional Index data.

```typescript
interface ADX {
  value: number;
  plusDI: number;
  minusDI: number;
  interpretation: 'strong_trend' | 'weak_trend' | 'no_trend';
  trendDirection: 'bullish' | 'bearish' | 'sideways';
}
```

#### Aroon

Aroon indicator data.

```typescript
interface Aroon {
  up: number;
  down: number;
  oscillator: number;
  interpretation: 'bullish' | 'bearish' | 'neutral';
  signal: 'buy' | 'sell' | 'hold';
}
```

### Portfolio Management

#### Position

Portfolio position data.

```typescript
interface Position {
  id: string;
  symbol: string;
  shares: number;
  averagePrice: number;
  currentPrice: number;
  marketValue: number;
  gain: number;
  gainPercent: number;
  purchaseDate: string;
  lastUpdated: string;
  sector: string;
  industry: string;
  weight: number; // Percentage of portfolio
  costBasis: number;
  unrealizedGain: number;
  realizedGain: number;
  dividends: number;
  totalReturn: number;
}
```

#### Portfolio

Complete portfolio data.

```typescript
interface Portfolio {
  id: string;
  name: string;
  totalValue: number;
  totalCost: number;
  totalGain: number;
  totalGainPercent: number;
  positions: Position[];
  cash: number;
  lastUpdated: string;
  performance: PortfolioPerformance;
  allocation: PortfolioAllocation;
  riskMetrics: RiskMetrics;
}
```

#### PortfolioPerformance

Portfolio performance metrics.

```typescript
interface PortfolioPerformance {
  dailyReturn: number;
  weeklyReturn: number;
  monthlyReturn: number;
  yearlyReturn: number;
  totalReturn: number;
  benchmarkReturn: number;
  alpha: number;
  beta: number;
  sharpeRatio: number;
  sortinoRatio: number;
  maxDrawdown: number;
  volatility: number;
  trackingError: number;
  informationRatio: number;
}
```

#### PortfolioAllocation

Portfolio allocation breakdown.

```typescript
interface PortfolioAllocation {
  bySector: Record<string, number>;
  byIndustry: Record<string, number>;
  byMarketCap: {
    large: number;
    mid: number;
    small: number;
  };
  byAssetClass: {
    stocks: number;
    bonds: number;
    cash: number;
    alternatives: number;
  };
  topHoldings: Array<{
    symbol: string;
    weight: number;
  }>;
}
```

#### RiskMetrics

Portfolio risk metrics.

```typescript
interface RiskMetrics {
  var95: number; // Value at Risk (95%)
  var99: number; // Value at Risk (99%)
  expectedShortfall: number;
  downsideDeviation: number;
  correlation: number;
  diversificationRatio: number;
  concentrationRisk: number;
  sectorRisk: number;
  currencyRisk: number;
  interestRateRisk: number;
}
```

### Market Data

#### MarketIndex

Market index data.

```typescript
interface MarketIndex {
  symbol: string;
  name: string;
  value: number;
  change: number;
  changePercent: number;
  volume: number;
  timestamp: string;
  components: number;
  description: string;
}
```

#### MarketSummary

Overall market summary.

```typescript
interface MarketSummary {
  sp500: MarketIndex;
  nasdaq: MarketIndex;
  dow: MarketIndex;
  vix: MarketIndex;
  timestamp: string;
  marketStatus: 'open' | 'closed' | 'pre_market' | 'after_hours';
  tradingVolume: number;
  advancingStocks: number;
  decliningStocks: number;
  unchangedStocks: number;
}
```

#### TopMovers

Top gaining and losing stocks.

```typescript
interface TopMovers {
  gainers: StockQuote[];
  losers: StockQuote[];
  mostActive: StockQuote[];
  timestamp: string;
}
```

### News and Sentiment

#### NewsArticle

Financial news article.

```typescript
interface NewsArticle {
  id: string;
  title: string;
  summary: string;
  content: string;
  url: string;
  source: string;
  author: string;
  publishedAt: string;
  updatedAt: string;
  sentiment: 'positive' | 'negative' | 'neutral';
  sentimentScore: number; // -1 to 1
  relatedSymbols: string[];
  tags: string[];
  category: string;
  imageUrl?: string;
  readTime: number; // in minutes
}
```

#### SentimentAnalysis

Sentiment analysis data.

```typescript
interface SentimentAnalysis {
  symbol: string;
  overallSentiment: 'positive' | 'negative' | 'neutral';
  sentimentScore: number; // -1 to 1
  confidence: number; // 0 to 1
  sources: {
    news: number;
    social: number;
    analyst: number;
  };
  breakdown: {
    positive: number;
    negative: number;
    neutral: number;
  };
  trends: {
    day: number;
    week: number;
    month: number;
  };
  timestamp: string;
}
```

### Alerts and Notifications

#### Alert

Price alert configuration.

```typescript
interface Alert {
  id: string;
  userId: string;
  symbol: string;
  type: 'price_above' | 'price_below' | 'percent_change' | 'volume_spike' | 'technical_signal';
  value: number;
  isActive: boolean;
  createdAt: string;
  triggeredAt?: string;
  notificationType: 'email' | 'push' | 'sms' | 'webhook';
  frequency: 'once' | 'recurring';
  conditions?: AlertCondition[];
  metadata?: Record<string, any>;
}
```

#### AlertCondition

Alert condition configuration.

```typescript
interface AlertCondition {
  field: string;
  operator: 'equals' | 'greater_than' | 'less_than' | 'contains' | 'not_equals';
  value: any;
  logicalOperator?: 'and' | 'or';
}
```

#### Notification

Notification data.

```typescript
interface Notification {
  id: string;
  userId: string;
  type: 'alert' | 'news' | 'system' | 'portfolio';
  title: string;
  message: string;
  data?: Record<string, any>;
  isRead: boolean;
  createdAt: string;
  readAt?: string;
  priority: 'low' | 'medium' | 'high' | 'urgent';
  category: string;
}
```

### User and Authentication

#### User

User account data.

```typescript
interface User {
  id: string;
  email: string;
  username: string;
  firstName: string;
  lastName: string;
  avatar?: string;
  preferences: UserPreferences;
  subscription: Subscription;
  createdAt: string;
  updatedAt: string;
  lastLoginAt: string;
  isActive: boolean;
  emailVerified: boolean;
  twoFactorEnabled: boolean;
}
```

#### UserPreferences

User preferences and settings.

```typescript
interface UserPreferences {
  theme: 'light' | 'dark' | 'auto';
  currency: string;
  timezone: string;
  language: string;
  notifications: NotificationSettings;
  dashboard: DashboardSettings;
  charts: ChartSettings;
  privacy: PrivacySettings;
}
```

#### NotificationSettings

Notification preferences.

```typescript
interface NotificationSettings {
  email: {
    enabled: boolean;
    frequency: 'immediate' | 'daily' | 'weekly';
    types: string[];
  };
  push: {
    enabled: boolean;
    types: string[];
  };
  sms: {
    enabled: boolean;
    types: string[];
  };
  webhook: {
    enabled: boolean;
    url?: string;
    events: string[];
  };
}
```

#### Subscription

User subscription data.

```typescript
interface Subscription {
  plan: 'free' | 'basic' | 'pro' | 'enterprise';
  status: 'active' | 'inactive' | 'cancelled' | 'expired';
  startDate: string;
  endDate?: string;
  features: string[];
  limits: {
    apiCalls: number;
    portfolioSize: number;
    alerts: number;
    historicalData: number;
  };
  billing: {
    amount: number;
    currency: string;
    interval: 'monthly' | 'yearly';
    nextBillingDate: string;
  };
}
```

### API Response Types

#### ApiResponse

Standard API response wrapper.

```typescript
interface ApiResponse<T> {
  success: boolean;
  data?: T;
  error?: ApiError;
  meta?: ApiMeta;
  timestamp: string;
}
```

#### ApiError

API error information.

```typescript
interface ApiError {
  code: string;
  message: string;
  details?: Record<string, any>;
  timestamp: string;
  requestId: string;
}
```

#### ApiMeta

API response metadata.

```typescript
interface ApiMeta {
  pagination?: {
    page: number;
    limit: number;
    total: number;
    totalPages: number;
  };
  rateLimit?: {
    limit: number;
    remaining: number;
    resetAt: string;
  };
  cache?: {
    cached: boolean;
    ttl: number;
    expiresAt: string;
  };
}
```

### Database Models

#### DatabaseStock

Database stock model.

```typescript
interface DatabaseStock {
  _id: string;
  symbol: string;
  companyName: string;
  sector: string;
  industry: string;
  exchange: string;
  marketCap: number;
  employees: number;
  website: string;
  description: string;
  ceo: string;
  founded: number;
  headquarters: string;
  phone: string;
  email: string;
  isActive: boolean;
  createdAt: string;
  updatedAt: string;
  lastPriceUpdate: string;
}
```

#### DatabasePrice

Database price data model.

```typescript
interface DatabasePrice {
  _id: string;
  symbol: string;
  date: string;
  open: number;
  high: number;
  low: number;
  close: number;
  volume: number;
  adjustedClose: number;
  dividendAmount: number;
  splitCoefficient: number;
  createdAt: string;
  updatedAt: string;
}
```

## Type Guards and Utilities

### Type Guards

```typescript
// Check if object is a valid StockQuote
function isStockQuote(obj: any): obj is StockQuote {
  return (
    typeof obj === 'object' &&
    typeof obj.symbol === 'string' &&
    typeof obj.currentPrice === 'number' &&
    typeof obj.change === 'number' &&
    typeof obj.changePercent === 'number'
  );
}

// Check if object is a valid Position
function isPosition(obj: any): obj is Position {
  return (
    typeof obj === 'object' &&
    typeof obj.id === 'string' &&
    typeof obj.symbol === 'string' &&
    typeof obj.shares === 'number' &&
    typeof obj.averagePrice === 'number'
  );
}

// Check if object is a valid Portfolio
function isPortfolio(obj: any): obj is Portfolio {
  return (
    typeof obj === 'object' &&
    typeof obj.id === 'string' &&
    typeof obj.name === 'string' &&
    typeof obj.totalValue === 'number' &&
    Array.isArray(obj.positions)
  );
}
```

### Data Transformers

```typescript
// Transform API response to StockQuote
function transformToStockQuote(apiData: any): StockQuote {
  return {
    symbol: apiData.symbol,
    companyName: apiData.companyName,
    currentPrice: parseFloat(apiData.currentPrice),
    change: parseFloat(apiData.change),
    changePercent: parseFloat(apiData.changePercent),
    volume: parseInt(apiData.volume),
    marketCap: parseFloat(apiData.marketCap),
    peRatio: parseFloat(apiData.peRatio),
    dividendYield: parseFloat(apiData.dividendYield),
    timestamp: apiData.timestamp,
    exchange: apiData.exchange,
    currency: apiData.currency,
    previousClose: parseFloat(apiData.previousClose),
    open: parseFloat(apiData.open),
    dayHigh: parseFloat(apiData.dayHigh),
    dayLow: parseFloat(apiData.dayLow),
    yearHigh: parseFloat(apiData.yearHigh),
    yearLow: parseFloat(apiData.yearLow),
    beta: parseFloat(apiData.beta),
    eps: parseFloat(apiData.eps),
    forwardPE: parseFloat(apiData.forwardPE),
    priceToBook: parseFloat(apiData.priceToBook),
    priceToSales: parseFloat(apiData.priceToSales),
    enterpriseValue: parseFloat(apiData.enterpriseValue),
    debtToEquity: parseFloat(apiData.debtToEquity),
    returnOnEquity: parseFloat(apiData.returnOnEquity),
    returnOnAssets: parseFloat(apiData.returnOnAssets),
    profitMargin: parseFloat(apiData.profitMargin),
    operatingMargin: parseFloat(apiData.operatingMargin),
    grossMargin: parseFloat(apiData.grossMargin)
  };
}

// Transform API response to Position
function transformToPosition(apiData: any): Position {
  return {
    id: apiData.id,
    symbol: apiData.symbol,
    shares: parseFloat(apiData.shares),
    averagePrice: parseFloat(apiData.averagePrice),
    currentPrice: parseFloat(apiData.currentPrice),
    marketValue: parseFloat(apiData.marketValue),
    gain: parseFloat(apiData.gain),
    gainPercent: parseFloat(apiData.gainPercent),
    purchaseDate: apiData.purchaseDate,
    lastUpdated: apiData.lastUpdated,
    sector: apiData.sector,
    industry: apiData.industry,
    weight: parseFloat(apiData.weight),
    costBasis: parseFloat(apiData.costBasis),
    unrealizedGain: parseFloat(apiData.unrealizedGain),
    realizedGain: parseFloat(apiData.realizedGain),
    dividends: parseFloat(apiData.dividends),
    totalReturn: parseFloat(apiData.totalReturn)
  };
}
```

## Validation Schemas

### Joi Validation Schemas

```typescript
import Joi from 'joi';

// Stock Quote validation schema
const stockQuoteSchema = Joi.object({
  symbol: Joi.string().required().max(10),
  companyName: Joi.string().required().max(100),
  currentPrice: Joi.number().positive().required(),
  change: Joi.number().required(),
  changePercent: Joi.number().required(),
  volume: Joi.number().integer().positive().required(),
  marketCap: Joi.number().positive().required(),
  peRatio: Joi.number().allow(null),
  dividendYield: Joi.number().min(0).allow(null),
  timestamp: Joi.date().iso().required()
});

// Position validation schema
const positionSchema = Joi.object({
  id: Joi.string().required(),
  symbol: Joi.string().required().max(10),
  shares: Joi.number().positive().required(),
  averagePrice: Joi.number().positive().required(),
  currentPrice: Joi.number().positive().required(),
  marketValue: Joi.number().positive().required(),
  gain: Joi.number().required(),
  gainPercent: Joi.number().required(),
  purchaseDate: Joi.date().iso().required()
});

// Portfolio validation schema
const portfolioSchema = Joi.object({
  id: Joi.string().required(),
  name: Joi.string().required().max(100),
  totalValue: Joi.number().positive().required(),
  totalCost: Joi.number().positive().required(),
  totalGain: Joi.number().required(),
  totalGainPercent: Joi.number().required(),
  positions: Joi.array().items(positionSchema).required(),
  cash: Joi.number().min(0).required()
});
```

## Constants and Enums

```typescript
// Stock exchanges
export enum Exchange {
  NYSE = 'NYSE',
  NASDAQ = 'NASDAQ',
  AMEX = 'AMEX',
  OTC = 'OTC',
  TSX = 'TSX',
  LSE = 'LSE',
  TSE = 'TSE'
}

// Alert types
export enum AlertType {
  PRICE_ABOVE = 'price_above',
  PRICE_BELOW = 'price_below',
  PERCENT_CHANGE = 'percent_change',
  VOLUME_SPIKE = 'volume_spike',
  TECHNICAL_SIGNAL = 'technical_signal'
}

// Notification types
export enum NotificationType {
  ALERT = 'alert',
  NEWS = 'news',
  SYSTEM = 'system',
  PORTFOLIO = 'portfolio'
}

// Subscription plans
export enum SubscriptionPlan {
  FREE = 'free',
  BASIC = 'basic',
  PRO = 'pro',
  ENTERPRISE = 'enterprise'
}

// Chart timeframes
export enum Timeframe {
  ONE_DAY = '1d',
  FIVE_DAYS = '5d',
  ONE_MONTH = '1mo',
  THREE_MONTHS = '3mo',
  SIX_MONTHS = '6mo',
  ONE_YEAR = '1y',
  TWO_YEARS = '2y',
  FIVE_YEARS = '5y',
  TEN_YEARS = '10y',
  YTD = 'ytd',
  MAX = 'max'
}

// Technical indicators
export enum TechnicalIndicator {
  SMA = 'sma',
  EMA = 'ema',
  RSI = 'rsi',
  MACD = 'macd',
  BOLLINGER_BANDS = 'bollinger_bands',
  STOCHASTIC = 'stochastic',
  WILLIAMS_R = 'williams_r',
  ADX = 'adx',
  AROON = 'aroon'
}
```