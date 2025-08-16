# Stock Analysis Project

A comprehensive stock market analysis platform providing real-time data, technical indicators, portfolio management, and advanced analytics.

## 🚀 Features

- **Real-time Stock Data**: Live quotes, historical data, and market information
- **Technical Analysis**: RSI, MACD, Bollinger Bands, Moving Averages, and more
- **Portfolio Management**: Track positions, calculate gains/losses, and analyze performance
- **Advanced Charts**: Interactive charts with multiple timeframes and indicators
- **News & Sentiment**: Financial news integration with sentiment analysis
- **Alerts & Notifications**: Price alerts, technical signals, and custom notifications
- **API Access**: RESTful API with SDKs for JavaScript and Python
- **Webhooks**: Real-time data delivery via webhooks

## 📚 Documentation

Comprehensive documentation is available in the [`docs/`](./docs/) directory:

- **[Getting Started](./docs/getting-started.md)** - Quick setup and installation guide
- **[API Reference](./docs/api-reference.md)** - Complete API documentation with examples
- **[Component Documentation](./docs/components.md)** - React component library and usage
- **[Data Models](./docs/data-models.md)** - TypeScript interfaces and data structures
- **[Configuration](./docs/configuration.md)** - Environment variables and setup options
- **[Examples](./docs/examples.md)** - Code examples and usage patterns
- **[Troubleshooting](./docs/troubleshooting.md)** - Common issues and solutions

## 🛠️ Quick Start

### Prerequisites

- Node.js 16+ 
- npm or yarn
- MongoDB
- Redis (optional, for caching)

### Installation

```bash
# Clone the repository
git clone https://github.com/your-username/stock-analysis.git
cd stock-analysis

# Install dependencies
npm install

# Set up environment variables
cp .env.example .env
# Edit .env with your configuration

# Start development server
npm run dev
```

Visit `http://localhost:3000` to see the application.

## 🔧 API Usage

### JavaScript/Node.js

```javascript
import { StockAnalysisAPI } from 'stock-analysis-sdk';

const api = new StockAnalysisAPI('YOUR_API_KEY');

// Get stock quote
const quote = await api.getStockQuote('AAPL');
console.log(`${quote.symbol}: $${quote.currentPrice}`);

// Get historical data
const history = await api.getHistoricalData('AAPL', {
  period: '1y',
  interval: '1d'
});

// Get technical indicators
const indicators = await api.getTechnicalIndicators('AAPL', {
  indicators: ['rsi', 'macd', 'bollinger_bands']
});
```

### Python

```python
from stock_analysis import StockAnalysisAPI

api = StockAnalysisAPI('YOUR_API_KEY')

# Get stock quote
quote = api.get_stock_quote('AAPL')
print(f"{quote['symbol']}: ${quote['currentPrice']}")

# Get historical data
history = api.get_historical_data('AAPL', period='1y', interval='1d')
```

## 🏗️ Architecture

The project follows a modern, scalable architecture:

- **Frontend**: React with TypeScript, Next.js, and Tailwind CSS
- **Backend**: Node.js with Express, MongoDB, and Redis
- **Charts**: Recharts and D3.js for data visualization
- **Testing**: Jest, React Testing Library, and Cypress
- **Deployment**: Docker and Docker Compose support

## 📊 Key Components

### StockChart
Interactive charts with technical indicators and multiple timeframes.

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

### Portfolio Management
Track and analyze your investment portfolio.

```tsx
import { PortfolioCard } from '@/components/PortfolioCard';

<PortfolioCard
  position={positionData}
  onEdit={() => editPosition()}
  onDelete={() => deletePosition()}
/>
```

### Technical Indicators
Comprehensive technical analysis tools.

```tsx
import { TechnicalIndicators } from '@/components/TechnicalIndicators';

<TechnicalIndicators
  symbol="AAPL"
  indicators={indicatorData}
  showChart={true}
/>
```

## 🔌 API Endpoints

### Stock Data
- `GET /api/v1/stocks/{symbol}/quote` - Real-time stock quote
- `GET /api/v1/stocks/{symbol}/history` - Historical price data
- `GET /api/v1/stocks/{symbol}/indicators` - Technical indicators

### Portfolio
- `GET /api/v1/portfolio` - Get user portfolio
- `POST /api/v1/portfolio/positions` - Add position
- `PUT /api/v1/portfolio/positions/{id}` - Update position
- `DELETE /api/v1/portfolio/positions/{id}` - Delete position

### Market Data
- `GET /api/v1/market/summary` - Market summary
- `GET /api/v1/market/top-movers` - Top gainers/losers

### Alerts
- `GET /api/v1/alerts` - Get user alerts
- `POST /api/v1/alerts` - Create alert
- `PUT /api/v1/alerts/{id}` - Update alert
- `DELETE /api/v1/alerts/{id}` - Delete alert

## 🧪 Testing

```bash
# Run unit tests
npm test

# Run tests with coverage
npm run test:coverage

# Run end-to-end tests
npm run test:e2e

# Run tests in watch mode
npm run test:watch
```

## 🚀 Deployment

### Docker

```bash
# Build and run with Docker Compose
docker-compose up -d

# Or build manually
docker build -t stock-analysis .
docker run -p 3000:3000 stock-analysis
```

### Environment Variables

Required environment variables:

```env
# API Configuration
API_KEY=your_api_key_here
DATABASE_URL=mongodb://localhost:27017/stock-analysis
REDIS_URL=redis://localhost:6379

# External APIs
ALPHA_VANTAGE_API_KEY=your_alpha_vantage_key
YAHOO_FINANCE_API_KEY=your_yahoo_finance_key
NEWS_API_KEY=your_news_api_key

# Security
JWT_SECRET=your_jwt_secret_here
```

## 🤝 Contributing

We welcome contributions! Please see our [Contributing Guidelines](./docs/contributing.md) for details.

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🆘 Support

- **Documentation**: Check the [docs](./docs/) directory
- **Issues**: [GitHub Issues](https://github.com/your-username/stock-analysis/issues)
- **Discussions**: [GitHub Discussions](https://github.com/your-username/stock-analysis/discussions)
- **Email**: support@stockanalysis.com

## 🔗 Links

- [Live Demo](https://stockanalysis.com)
- [API Documentation](https://api.stockanalysis.com/docs)
- [SDK Downloads](https://github.com/your-username/stock-analysis/releases)
- [Changelog](./CHANGELOG.md)

---

Built with ❤️ by the Stock Analysis Team
