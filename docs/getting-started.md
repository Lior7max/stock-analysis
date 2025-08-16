# Getting Started

Welcome to the Stock Analysis project! This guide will help you get up and running quickly.

## Prerequisites

Before you begin, make sure you have the following installed:

- **Node.js** (version 16 or higher)
- **npm** or **yarn**
- **Git**

## Installation

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/stock-analysis.git
cd stock-analysis
```

### 2. Install Dependencies

```bash
npm install
# or
yarn install
```

### 3. Environment Setup

Create a `.env` file in the root directory:

```bash
cp .env.example .env
```

Edit the `.env` file with your configuration:

```env
# API Configuration
API_KEY=your_api_key_here
API_BASE_URL=https://api.stockanalysis.com/v1

# Database Configuration
DATABASE_URL=mongodb://localhost:27017/stock-analysis
DATABASE_NAME=stock-analysis

# Redis Configuration (for caching)
REDIS_URL=redis://localhost:6379

# JWT Configuration
JWT_SECRET=your_jwt_secret_here
JWT_EXPIRES_IN=7d

# Email Configuration
SMTP_HOST=smtp.gmail.com
SMTP_PORT=587
SMTP_USER=your_email@gmail.com
SMTP_PASS=your_email_password

# External APIs
ALPHA_VANTAGE_API_KEY=your_alpha_vantage_key
YAHOO_FINANCE_API_KEY=your_yahoo_finance_key
NEWS_API_KEY=your_news_api_key

# Application Settings
NODE_ENV=development
PORT=3000
CORS_ORIGIN=http://localhost:3000
```

### 4. Database Setup

#### MongoDB

If you're using MongoDB locally:

```bash
# Install MongoDB (macOS with Homebrew)
brew install mongodb-community

# Start MongoDB service
brew services start mongodb-community

# Or run MongoDB manually
mongod --dbpath /usr/local/var/mongodb
```

#### Redis (for caching)

```bash
# Install Redis (macOS with Homebrew)
brew install redis

# Start Redis service
brew services start redis

# Or run Redis manually
redis-server
```

### 5. Run Database Migrations

```bash
npm run migrate
# or
yarn migrate
```

### 6. Seed Initial Data (Optional)

```bash
npm run seed
# or
yarn seed
```

## Running the Application

### Development Mode

```bash
# Start the development server
npm run dev
# or
yarn dev
```

The application will be available at `http://localhost:3000`

### Production Mode

```bash
# Build the application
npm run build
# or
yarn build

# Start the production server
npm start
# or
yarn start
```

## API Key Setup

To use the Stock Analysis API, you'll need to obtain API keys from the following services:

### 1. Alpha Vantage

1. Visit [Alpha Vantage](https://www.alphavantage.co/support/#api-key)
2. Sign up for a free account
3. Get your API key
4. Add it to your `.env` file

### 2. Yahoo Finance

1. Visit [Yahoo Finance API](https://finance.yahoo.com/)
2. Sign up for API access
3. Get your API key
4. Add it to your `.env` file

### 3. News API

1. Visit [News API](https://newsapi.org/)
2. Sign up for a free account
3. Get your API key
4. Add it to your `.env` file

## Project Structure

```
stock-analysis/
├── src/
│   ├── components/          # React components
│   ├── pages/              # Page components
│   ├── hooks/              # Custom React hooks
│   ├── utils/              # Utility functions
│   ├── services/           # API services
│   ├── types/              # TypeScript type definitions
│   ├── styles/             # CSS/SCSS files
│   └── tests/              # Test files
├── public/                 # Static assets
├── docs/                   # Documentation
├── scripts/                # Build and deployment scripts
├── package.json
├── tsconfig.json
├── tailwind.config.js
└── README.md
```

## Quick Start Examples

### 1. Get a Stock Quote

```javascript
import { StockAnalysisAPI } from 'stock-analysis-sdk';

const api = new StockAnalysisAPI('YOUR_API_KEY');

// Get real-time stock quote
const quote = await api.getStockQuote('AAPL');
console.log(`${quote.symbol}: $${quote.currentPrice}`);
```

### 2. Create a Simple Chart

```tsx
import React from 'react';
import { StockChart } from '@/components/StockChart';

function App() {
  const [data, setData] = useState([]);

  useEffect(() => {
    // Fetch stock data
    const fetchData = async () => {
      const response = await fetch('/api/stocks/AAPL/history?period=1y');
      const stockData = await response.json();
      setData(stockData.data);
    };

    fetchData();
  }, []);

  return (
    <div>
      <h1>AAPL Stock Chart</h1>
      <StockChart
        data={data}
        height={400}
        width={800}
        theme="dark"
      />
    </div>
  );
}
```

### 3. Set up a Portfolio

```javascript
// Add a position to your portfolio
const position = await api.addPosition({
  symbol: 'GOOGL',
  shares: 10,
  purchasePrice: 2800.00,
  purchaseDate: '2024-01-15'
});

// Get portfolio summary
const portfolio = await api.getPortfolio();
console.log(`Portfolio Value: $${portfolio.totalValue}`);
```

## Development Workflow

### 1. Code Style

The project uses ESLint and Prettier for code formatting:

```bash
# Check code style
npm run lint

# Fix code style issues
npm run lint:fix

# Format code
npm run format
```

### 2. Testing

```bash
# Run all tests
npm test

# Run tests in watch mode
npm run test:watch

# Run tests with coverage
npm run test:coverage

# Run specific test file
npm test -- --testPathPattern=StockChart.test.tsx
```

### 3. Building

```bash
# Build for development
npm run build:dev

# Build for production
npm run build

# Build and analyze bundle
npm run build:analyze
```

## Troubleshooting

### Common Issues

#### 1. API Key Errors

If you're getting API key errors:

- Verify your API keys are correctly set in the `.env` file
- Check that the API keys are valid and have sufficient quota
- Ensure the environment variables are being loaded correctly

#### 2. Database Connection Issues

If you can't connect to the database:

- Verify MongoDB is running: `brew services list | grep mongodb`
- Check the database URL in your `.env` file
- Ensure the database exists and is accessible

#### 3. Build Errors

If you encounter build errors:

- Clear node_modules and reinstall: `rm -rf node_modules && npm install`
- Clear build cache: `npm run clean`
- Check for TypeScript errors: `npm run type-check`

#### 4. Port Already in Use

If port 3000 is already in use:

- Change the port in your `.env` file: `PORT=3001`
- Or kill the process using the port: `lsof -ti:3000 | xargs kill -9`

### Getting Help

If you're still having issues:

1. Check the [Troubleshooting Guide](./troubleshooting.md)
2. Search existing [GitHub Issues](https://github.com/your-username/stock-analysis/issues)
3. Create a new issue with detailed information about your problem

## Next Steps

Now that you have the application running, you can:

1. **Explore the API**: Check out the [API Reference](./api-reference.md)
2. **Learn about Components**: Read the [Component Documentation](./components.md)
3. **View Examples**: See [Usage Examples](./examples.md)
4. **Understand Data Models**: Review the [Data Models](./data-models.md)

## Contributing

We welcome contributions! Please see our [Contributing Guidelines](./contributing.md) for details on how to:

- Report bugs
- Request features
- Submit pull requests
- Follow our coding standards

## Support

For support and questions:

- **Documentation**: Check the docs folder
- **Issues**: [GitHub Issues](https://github.com/your-username/stock-analysis/issues)
- **Discussions**: [GitHub Discussions](https://github.com/your-username/stock-analysis/discussions)
- **Email**: support@stockanalysis.com

## License

This project is licensed under the MIT License - see the [LICENSE](../LICENSE) file for details.