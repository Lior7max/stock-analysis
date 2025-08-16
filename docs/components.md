# Component Documentation

This document provides comprehensive documentation for all React components in the Stock Analysis project.

## Component Overview

The Stock Analysis frontend is built with React and TypeScript, using a component-based architecture for modularity and reusability.

## Core Components

### StockChart

A reusable chart component for displaying stock price data with technical indicators.

```tsx
import { StockChart } from '@/components/StockChart';

<StockChart
  data={chartData}
  indicators={['sma', 'ema', 'rsi']}
  height={400}
  width={800}
  theme="dark"
/>
```

**Props:**
- `data` (StockData[]): Array of stock price data points
- `indicators` (string[]): Array of technical indicators to display
- `height` (number): Chart height in pixels
- `width` (number): Chart width in pixels
- `theme` ('light' | 'dark'): Chart theme
- `onDataPointClick` (function): Callback when data point is clicked
- `showVolume` (boolean): Whether to show volume bars
- `timeframe` (string): Chart timeframe (1d, 1w, 1m, 3m, 1y)

**Example:**
```tsx
const chartData = [
  {
    date: '2024-01-15',
    open: 148.50,
    high: 151.20,
    low: 147.80,
    close: 150.25,
    volume: 45678900
  }
];

<StockChart
  data={chartData}
  indicators={['sma', 'ema']}
  height={400}
  width={800}
  theme="dark"
  showVolume={true}
  onDataPointClick={(point) => console.log('Clicked:', point)}
/>
```

### StockQuote

Displays real-time stock quote information with price changes and key metrics.

```tsx
import { StockQuote } from '@/components/StockQuote';

<StockQuote
  symbol="AAPL"
  quote={quoteData}
  showDetails={true}
  onRefresh={() => fetchQuote()}
/>
```

**Props:**
- `symbol` (string): Stock symbol
- `quote` (QuoteData): Quote data object
- `showDetails` (boolean): Whether to show detailed metrics
- `onRefresh` (function): Callback for manual refresh
- `autoRefresh` (boolean): Enable automatic refresh
- `refreshInterval` (number): Refresh interval in seconds

**QuoteData Interface:**
```typescript
interface QuoteData {
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
}
```

### PortfolioCard

Displays portfolio position information with gains/losses.

```tsx
import { PortfolioCard } from '@/components/PortfolioCard';

<PortfolioCard
  position={positionData}
  onEdit={() => editPosition()}
  onDelete={() => deletePosition()}
/>
```

**Props:**
- `position` (PositionData): Position data object
- `onEdit` (function): Edit position callback
- `onDelete` (function): Delete position callback
- `showActions` (boolean): Show edit/delete buttons
- `compact` (boolean): Compact view mode

**PositionData Interface:**
```typescript
interface PositionData {
  id: string;
  symbol: string;
  shares: number;
  averagePrice: number;
  currentPrice: number;
  marketValue: number;
  gain: number;
  gainPercent: number;
  purchaseDate: string;
}
```

### TechnicalIndicators

Displays technical analysis indicators for a stock.

```tsx
import { TechnicalIndicators } from '@/components/TechnicalIndicators';

<TechnicalIndicators
  symbol="AAPL"
  indicators={indicatorData}
  showChart={true}
/>
```

**Props:**
- `symbol` (string): Stock symbol
- `indicators` (IndicatorData): Technical indicators data
- `showChart` (boolean): Show indicator charts
- `selectedIndicators` (string[]): Indicators to display
- `onIndicatorChange` (function): Callback when indicators change

**IndicatorData Interface:**
```typescript
interface IndicatorData {
  rsi: {
    value: number;
    period: number;
    interpretation: string;
  };
  movingAverages: {
    sma: Record<number, number>;
    ema: Record<number, number>;
  };
  macd: {
    value: number;
    signal: number;
    histogram: number;
  };
  bollingerBands: {
    upper: number;
    middle: number;
    lower: number;
  };
}
```

### MarketSummary

Displays overall market summary with major indices.

```tsx
import { MarketSummary } from '@/components/MarketSummary';

<MarketSummary
  data={marketData}
  showDetails={true}
  autoRefresh={true}
/>
```

**Props:**
- `data` (MarketData): Market summary data
- `showDetails` (boolean): Show detailed market information
- `autoRefresh` (boolean): Enable automatic refresh
- `refreshInterval` (number): Refresh interval in seconds

**MarketData Interface:**
```typescript
interface MarketData {
  sp500: IndexData;
  nasdaq: IndexData;
  dow: IndexData;
  vix: IndexData;
  timestamp: string;
}

interface IndexData {
  value: number;
  change: number;
  changePercent: number;
}
```

### SearchBar

Search component for finding stocks and companies.

```tsx
import { SearchBar } from '@/components/SearchBar';

<SearchBar
  onSearch={(query) => searchStocks(query)}
  placeholder="Search stocks..."
  suggestions={suggestions}
  onSuggestionSelect={(suggestion) => selectStock(suggestion)}
/>
```

**Props:**
- `onSearch` (function): Search callback
- `placeholder` (string): Search placeholder text
- `suggestions` (Suggestion[]): Search suggestions
- `onSuggestionSelect` (function): Suggestion selection callback
- `debounceMs` (number): Debounce delay in milliseconds
- `minQueryLength` (number): Minimum query length for search

**Suggestion Interface:**
```typescript
interface Suggestion {
  symbol: string;
  companyName: string;
  exchange: string;
  type: 'stock' | 'etf' | 'index';
}
```

### Watchlist

Component for managing and displaying watchlist stocks.

```tsx
import { Watchlist } from '@/components/Watchlist';

<Watchlist
  stocks={watchlistData}
  onAddStock={(symbol) => addToWatchlist(symbol)}
  onRemoveStock={(symbol) => removeFromWatchlist(symbol)}
  onStockClick={(symbol) => navigateToStock(symbol)}
/>
```

**Props:**
- `stocks` (WatchlistStock[]): Watchlist stocks data
- `onAddStock` (function): Add stock callback
- `onRemoveStock` (function): Remove stock callback
- `onStockClick` (function): Stock click callback
- `maxStocks` (number): Maximum number of stocks to display
- `showAddButton` (boolean): Show add stock button

**WatchlistStock Interface:**
```typescript
interface WatchlistStock {
  symbol: string;
  companyName: string;
  currentPrice: number;
  change: number;
  changePercent: number;
  volume: number;
  marketCap: number;
}
```

### NewsFeed

Displays financial news related to stocks and markets.

```tsx
import { NewsFeed } from '@/components/NewsFeed';

<NewsFeed
  news={newsData}
  symbol="AAPL"
  onNewsClick={(article) => openArticle(article)}
/>
```

**Props:**
- `news` (NewsArticle[]): News articles data
- `symbol` (string): Filter news by stock symbol
- `onNewsClick` (function): News article click callback
- `maxArticles` (number): Maximum articles to display
- `showSource` (boolean): Show news source
- `showTimestamp` (boolean): Show article timestamp

**NewsArticle Interface:**
```typescript
interface NewsArticle {
  id: string;
  title: string;
  summary: string;
  url: string;
  source: string;
  publishedAt: string;
  sentiment: 'positive' | 'negative' | 'neutral';
  relatedSymbols: string[];
}
```

### AlertManager

Manages stock price alerts and notifications.

```tsx
import { AlertManager } from '@/components/AlertManager';

<AlertManager
  alerts={alertsData}
  onCreateAlert={(alert) => createAlert(alert)}
  onDeleteAlert={(id) => deleteAlert(id)}
  onEditAlert={(alert) => editAlert(alert)}
/>
```

**Props:**
- `alerts` (Alert[]): User alerts data
- `onCreateAlert` (function): Create alert callback
- `onDeleteAlert` (function): Delete alert callback
- `onEditAlert` (function): Edit alert callback
- `showCreateForm` (boolean): Show alert creation form

**Alert Interface:**
```typescript
interface Alert {
  id: string;
  symbol: string;
  type: 'price_above' | 'price_below' | 'percent_change';
  value: number;
  isActive: boolean;
  createdAt: string;
  triggeredAt?: string;
}
```

## Layout Components

### Dashboard

Main dashboard layout component.

```tsx
import { Dashboard } from '@/components/Dashboard';

<Dashboard
  sidebar={<Sidebar />}
  header={<Header />}
  content={<MainContent />}
  footer={<Footer />}
/>
```

**Props:**
- `sidebar` (ReactNode): Sidebar component
- `header` (ReactNode): Header component
- `content` (ReactNode): Main content
- `footer` (ReactNode): Footer component
- `sidebarCollapsed` (boolean): Sidebar collapsed state
- `onSidebarToggle` (function): Sidebar toggle callback

### Sidebar

Navigation sidebar component.

```tsx
import { Sidebar } from '@/components/Sidebar';

<Sidebar
  items={navigationItems}
  activeItem="dashboard"
  onItemClick={(item) => navigate(item)}
  collapsed={false}
/>
```

**Props:**
- `items` (NavItem[]): Navigation items
- `activeItem` (string): Currently active item
- `onItemClick` (function): Item click callback
- `collapsed` (boolean): Sidebar collapsed state
- `showIcons` (boolean): Show navigation icons

**NavItem Interface:**
```typescript
interface NavItem {
  id: string;
  label: string;
  icon: string;
  path: string;
  badge?: number;
  children?: NavItem[];
}
```

## Utility Components

### LoadingSpinner

Reusable loading spinner component.

```tsx
import { LoadingSpinner } from '@/components/LoadingSpinner';

<LoadingSpinner
  size="medium"
  color="primary"
  text="Loading..."
/>
```

**Props:**
- `size` ('small' | 'medium' | 'large'): Spinner size
- `color` (string): Spinner color
- `text` (string): Loading text
- `showText` (boolean): Show loading text

### ErrorBoundary

Error boundary component for handling React errors.

```tsx
import { ErrorBoundary } from '@/components/ErrorBoundary';

<ErrorBoundary
  fallback={<ErrorFallback />}
  onError={(error, errorInfo) => logError(error, errorInfo)}
>
  <ComponentThatMightError />
</ErrorBoundary>
```

**Props:**
- `fallback` (ReactNode): Fallback UI component
- `onError` (function): Error callback
- `resetKeys` (any[]): Keys to reset error boundary

### Modal

Reusable modal component.

```tsx
import { Modal } from '@/components/Modal';

<Modal
  isOpen={isModalOpen}
  onClose={() => setIsModalOpen(false)}
  title="Stock Details"
  size="large"
>
  <ModalContent />
</Modal>
```

**Props:**
- `isOpen` (boolean): Modal open state
- `onClose` (function): Close modal callback
- `title` (string): Modal title
- `size` ('small' | 'medium' | 'large'): Modal size
- `closeOnOverlayClick` (boolean): Close on overlay click
- `showCloseButton` (boolean): Show close button

## Styling and Theming

All components support theming through CSS custom properties:

```css
:root {
  --primary-color: #007bff;
  --secondary-color: #6c757d;
  --success-color: #28a745;
  --danger-color: #dc3545;
  --warning-color: #ffc107;
  --info-color: #17a2b8;
  --light-color: #f8f9fa;
  --dark-color: #343a40;
  --border-radius: 4px;
  --box-shadow: 0 2px 4px rgba(0,0,0,0.1);
}
```

Components also support dark mode:

```css
[data-theme="dark"] {
  --bg-color: #1a1a1a;
  --text-color: #ffffff;
  --border-color: #333333;
}
```

## Component Testing

All components include unit tests using React Testing Library:

```tsx
import { render, screen, fireEvent } from '@testing-library/react';
import { StockQuote } from '@/components/StockQuote';

test('renders stock quote with correct data', () => {
  const mockQuote = {
    symbol: 'AAPL',
    currentPrice: 150.25,
    change: 2.15,
    changePercent: 1.45
  };

  render(<StockQuote symbol="AAPL" quote={mockQuote} />);
  
  expect(screen.getByText('AAPL')).toBeInTheDocument();
  expect(screen.getByText('$150.25')).toBeInTheDocument();
  expect(screen.getByText('+2.15 (1.45%)')).toBeInTheDocument();
});
```

## Performance Optimization

Components are optimized for performance using:

- React.memo for preventing unnecessary re-renders
- useMemo and useCallback for expensive calculations
- Lazy loading for large components
- Virtual scrolling for long lists
- Debounced search inputs

```tsx
const StockChart = React.memo(({ data, indicators, ...props }) => {
  const processedData = useMemo(() => processChartData(data), [data]);
  const handleDataPointClick = useCallback((point) => {
    onDataPointClick?.(point);
  }, [onDataPointClick]);

  return (
    <Chart
      data={processedData}
      indicators={indicators}
      onDataPointClick={handleDataPointClick}
      {...props}
    />
  );
});
```