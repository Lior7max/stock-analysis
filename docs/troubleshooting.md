# Troubleshooting Guide

This guide helps you resolve common issues and problems you might encounter while using the Stock Analysis project.

## Common Issues

### API Issues

#### 1. API Key Errors

**Problem**: Getting "Invalid API key" or "API key not found" errors.

**Solutions**:

1. **Verify API Key**:
   ```bash
   # Check if API key is set in environment
   echo $API_KEY
   ```

2. **Check .env file**:
   ```bash
   # Ensure API key is properly set
   cat .env | grep API_KEY
   ```

3. **Regenerate API Key**:
   ```bash
   # If using the dashboard, regenerate your API key
   # Or contact support for a new key
   ```

4. **Check API Key Format**:
   ```javascript
   // Ensure API key is a valid string
   console.log(typeof process.env.API_KEY);
   console.log(process.env.API_KEY?.length);
   ```

#### 2. Rate Limit Exceeded

**Problem**: Getting "Rate limit exceeded" errors.

**Solutions**:

1. **Check Current Usage**:
   ```bash
   curl -H "Authorization: Bearer YOUR_API_KEY" \
        https://api.stockanalysis.com/v1/usage
   ```

2. **Implement Caching**:
   ```javascript
   // Cache API responses to reduce calls
   const cache = new Map();
   
   async function getStockQuote(symbol) {
     const cacheKey = `quote_${symbol}`;
     const cached = cache.get(cacheKey);
     
     if (cached && Date.now() - cached.timestamp < 5 * 60 * 1000) {
       return cached.data;
     }
     
     const quote = await api.getStockQuote(symbol);
     cache.set(cacheKey, { data: quote, timestamp: Date.now() });
     return quote;
   }
   ```

3. **Upgrade Plan**: Consider upgrading to a higher tier plan for increased rate limits.

#### 3. Network Timeout Errors

**Problem**: API requests timing out.

**Solutions**:

1. **Increase Timeout**:
   ```javascript
   const api = new StockAnalysisAPI('YOUR_API_KEY', {
     timeout: 30000 // 30 seconds
   });
   ```

2. **Implement Retry Logic**:
   ```javascript
   async function fetchWithRetry(fn, maxRetries = 3) {
     for (let i = 0; i < maxRetries; i++) {
       try {
         return await fn();
       } catch (error) {
         if (i === maxRetries - 1) throw error;
         await new Promise(resolve => setTimeout(resolve, 1000 * (i + 1)));
       }
     }
   }
   ```

3. **Check Network Connection**:
   ```bash
   # Test connectivity to API
   curl -I https://api.stockanalysis.com/v1/health
   ```

### Database Issues

#### 1. MongoDB Connection Errors

**Problem**: Cannot connect to MongoDB database.

**Solutions**:

1. **Check MongoDB Service**:
   ```bash
   # macOS
   brew services list | grep mongodb
   
   # Linux
   sudo systemctl status mongod
   
   # Windows
   sc query MongoDB
   ```

2. **Start MongoDB**:
   ```bash
   # macOS
   brew services start mongodb-community
   
   # Linux
   sudo systemctl start mongod
   
   # Windows
   net start MongoDB
   ```

3. **Check Connection String**:
   ```bash
   # Verify DATABASE_URL in .env
   echo $DATABASE_URL
   ```

4. **Test Connection**:
   ```bash
   # Test MongoDB connection
   mongo $DATABASE_URL --eval "db.runCommand('ping')"
   ```

#### 2. Redis Connection Issues

**Problem**: Cannot connect to Redis cache.

**Solutions**:

1. **Check Redis Service**:
   ```bash
   # macOS
   brew services list | grep redis
   
   # Linux
   sudo systemctl status redis
   ```

2. **Start Redis**:
   ```bash
   # macOS
   brew services start redis
   
   # Linux
   sudo systemctl start redis
   ```

3. **Test Redis Connection**:
   ```bash
   redis-cli ping
   ```

### Frontend Issues

#### 1. Build Errors

**Problem**: Application fails to build.

**Solutions**:

1. **Clear Cache**:
   ```bash
   # Clear Next.js cache
   rm -rf .next
   
   # Clear npm cache
   npm cache clean --force
   
   # Reinstall dependencies
   rm -rf node_modules package-lock.json
   npm install
   ```

2. **Check TypeScript Errors**:
   ```bash
   npm run type-check
   ```

3. **Fix ESLint Issues**:
   ```bash
   npm run lint:fix
   ```

#### 2. Component Rendering Issues

**Problem**: Components not rendering or displaying incorrectly.

**Solutions**:

1. **Check Console Errors**:
   ```javascript
   // Open browser developer tools
   // Check Console tab for errors
   ```

2. **Verify Props**:
   ```javascript
   // Add prop validation
   import PropTypes from 'prop-types';
   
   StockChart.propTypes = {
     data: PropTypes.array.isRequired,
     height: PropTypes.number,
     width: PropTypes.number,
   };
   ```

3. **Check Data Format**:
   ```javascript
   // Ensure data is in correct format
   console.log('Chart data:', data);
   console.log('Data type:', typeof data);
   console.log('Data length:', data?.length);
   ```

#### 3. Chart Display Issues

**Problem**: Charts not displaying or showing incorrect data.

**Solutions**:

1. **Verify Data Structure**:
   ```javascript
   // Ensure data has required fields
   const requiredFields = ['date', 'open', 'high', 'low', 'close', 'volume'];
   const isValidData = data.every(point => 
     requiredFields.every(field => point.hasOwnProperty(field))
   );
   console.log('Data valid:', isValidData);
   ```

2. **Check Chart Dimensions**:
   ```javascript
   // Ensure chart has proper dimensions
   console.log('Chart dimensions:', { width, height });
   ```

3. **Verify Chart Library**:
   ```bash
   # Check if chart library is installed
   npm list recharts
   npm list d3
   ```

### Authentication Issues

#### 1. JWT Token Errors

**Problem**: Authentication failing with JWT errors.

**Solutions**:

1. **Check JWT Secret**:
   ```bash
   # Verify JWT_SECRET is set
   echo $JWT_SECRET
   ```

2. **Check Token Expiration**:
   ```javascript
   // Decode JWT token to check expiration
   const token = 'your-jwt-token';
   const payload = JSON.parse(atob(token.split('.')[1]));
   console.log('Token expires:', new Date(payload.exp * 1000));
   ```

3. **Refresh Token**:
   ```javascript
   // Implement token refresh logic
   async function refreshToken() {
     const response = await fetch('/api/auth/refresh', {
       method: 'POST',
       headers: { 'Authorization': `Bearer ${refreshToken}` }
     });
     const { accessToken } = await response.json();
     return accessToken;
   }
   ```

#### 2. Login Issues

**Problem**: Users cannot log in.

**Solutions**:

1. **Check User Credentials**:
   ```javascript
   // Verify user exists in database
   const user = await User.findOne({ email: email });
   console.log('User found:', !!user);
   ```

2. **Check Password Hashing**:
   ```javascript
   // Verify password comparison
   const isValidPassword = await bcrypt.compare(password, user.password);
   console.log('Password valid:', isValidPassword);
   ```

3. **Check Email Verification**:
   ```javascript
   // Ensure email is verified
   console.log('Email verified:', user.emailVerified);
   ```

### Performance Issues

#### 1. Slow API Responses

**Problem**: API endpoints responding slowly.

**Solutions**:

1. **Implement Caching**:
   ```javascript
   // Add Redis caching
   const cacheKey = `stock_${symbol}`;
   const cached = await redis.get(cacheKey);
   
   if (cached) {
     return JSON.parse(cached);
   }
   
   const data = await fetchStockData(symbol);
   await redis.setex(cacheKey, 300, JSON.stringify(data)); // 5 minutes
   return data;
   ```

2. **Database Indexing**:
   ```javascript
   // Add indexes to frequently queried fields
   await Stock.createIndex({ symbol: 1 });
   await Stock.createIndex({ date: -1 });
   ```

3. **Optimize Queries**:
   ```javascript
   // Use projection to limit returned fields
   const stocks = await Stock.find({}, { symbol: 1, price: 1, date: 1 });
   ```

#### 2. Memory Leaks

**Problem**: Application consuming too much memory.

**Solutions**:

1. **Check Memory Usage**:
   ```bash
   # Monitor memory usage
   top -p $(pgrep node)
   ```

2. **Implement Memory Management**:
   ```javascript
   // Clear intervals and timeouts
   useEffect(() => {
     const interval = setInterval(fetchData, 5000);
     return () => clearInterval(interval);
   }, []);
   ```

3. **Optimize Data Structures**:
   ```javascript
   // Use more efficient data structures
   const stockMap = new Map(stocks.map(s => [s.symbol, s]));
   ```

### Deployment Issues

#### 1. Build Failures

**Problem**: Application fails to build in production.

**Solutions**:

1. **Check Environment Variables**:
   ```bash
   # Verify all required env vars are set
   cat .env.production
   ```

2. **Check Node Version**:
   ```bash
   # Ensure correct Node.js version
   node --version
   npm --version
   ```

3. **Check Dependencies**:
   ```bash
   # Install production dependencies
   npm ci --only=production
   ```

#### 2. Docker Issues

**Problem**: Docker container not starting or running.

**Solutions**:

1. **Check Docker Logs**:
   ```bash
   docker logs <container-id>
   ```

2. **Verify Dockerfile**:
   ```dockerfile
   # Ensure proper base image and dependencies
   FROM node:18-alpine
   WORKDIR /app
   COPY package*.json ./
   RUN npm ci --only=production
   COPY . .
   EXPOSE 3000
   CMD ["npm", "start"]
   ```

3. **Check Port Binding**:
   ```bash
   # Verify port is not already in use
   lsof -i :3000
   ```

## Debugging Tools

### 1. Logging

```javascript
// Add comprehensive logging
const logger = require('./config/logger');

logger.info('API request started', { 
  endpoint: '/api/stocks/AAPL',
  timestamp: new Date().toISOString()
});

try {
  const result = await api.getStockQuote('AAPL');
  logger.info('API request successful', { result });
} catch (error) {
  logger.error('API request failed', { error: error.message });
}
```

### 2. Error Monitoring

```javascript
// Implement error tracking
process.on('uncaughtException', (error) => {
  logger.error('Uncaught Exception:', error);
  process.exit(1);
});

process.on('unhandledRejection', (reason, promise) => {
  logger.error('Unhandled Rejection at:', promise, 'reason:', reason);
});
```

### 3. Performance Monitoring

```javascript
// Add performance monitoring
const startTime = Date.now();

// Your code here

const endTime = Date.now();
logger.info('Operation completed', { 
  duration: endTime - startTime,
  operation: 'stockQuote'
});
```

## Testing Issues

### 1. Test Failures

**Problem**: Tests failing unexpectedly.

**Solutions**:

1. **Check Test Environment**:
   ```bash
   # Ensure test environment is properly set
   NODE_ENV=test npm test
   ```

2. **Mock External Dependencies**:
   ```javascript
   // Mock API calls in tests
   jest.mock('stock-analysis-sdk', () => ({
     StockAnalysisAPI: jest.fn().mockImplementation(() => ({
       getStockQuote: jest.fn().mockResolvedValue({
         symbol: 'AAPL',
         currentPrice: 150.25
       })
     }))
   }));
   ```

3. **Clean Test Database**:
   ```javascript
   // Clean database before each test
   beforeEach(async () => {
     await mongoose.connection.dropDatabase();
   });
   ```

### 2. E2E Test Issues

**Problem**: End-to-end tests failing.

**Solutions**:

1. **Check Application State**:
   ```javascript
   // Ensure app is running before tests
   before(() => {
     cy.visit('http://localhost:3000');
   });
   ```

2. **Add Wait Conditions**:
   ```javascript
   // Wait for elements to load
   cy.get('[data-testid="stock-chart"]').should('be.visible');
   ```

3. **Handle Async Operations**:
   ```javascript
   // Wait for API responses
   cy.intercept('GET', '/api/stocks/*').as('getStock');
   cy.wait('@getStock');
   ```

## Getting Help

### 1. Check Documentation

- Review the [API Reference](./api-reference.md)
- Check [Component Documentation](./components.md)
- Read [Configuration Guide](./configuration.md)

### 2. Search Issues

- Check existing [GitHub Issues](https://github.com/your-username/stock-analysis/issues)
- Search for similar problems in the issue tracker

### 3. Create Detailed Bug Report

When reporting an issue, include:

```markdown
## Bug Report

### Environment
- OS: [e.g., macOS 12.0]
- Node.js: [e.g., v18.0.0]
- npm: [e.g., v8.0.0]

### Steps to Reproduce
1. [Step 1]
2. [Step 2]
3. [Step 3]

### Expected Behavior
[What you expected to happen]

### Actual Behavior
[What actually happened]

### Error Messages
```
[Paste error messages here]
```

### Additional Context
[Any other relevant information]
```

### 4. Contact Support

- **Email**: support@stockanalysis.com
- **Discord**: [Join our Discord server](https://discord.gg/stockanalysis)
- **GitHub Discussions**: [Create a discussion](https://github.com/your-username/stock-analysis/discussions)

## Prevention Tips

### 1. Regular Maintenance

```bash
# Update dependencies regularly
npm update

# Check for security vulnerabilities
npm audit

# Fix security issues
npm audit fix
```

### 2. Monitoring

```javascript
// Implement health checks
app.get('/health', async (req, res) => {
  const health = {
    database: await checkDatabase(),
    redis: await checkRedis(),
    externalApi: await checkExternalApi()
  };
  
  const isHealthy = Object.values(health).every(h => h.status === 'ok');
  res.status(isHealthy ? 200 : 503).json(health);
});
```

### 3. Error Boundaries

```javascript
// Add React error boundaries
class ErrorBoundary extends React.Component {
  constructor(props) {
    super(props);
    this.state = { hasError: false };
  }

  static getDerivedStateFromError(error) {
    return { hasError: true };
  }

  componentDidCatch(error, errorInfo) {
    logger.error('React Error Boundary:', { error, errorInfo });
  }

  render() {
    if (this.state.hasError) {
      return <h1>Something went wrong.</h1>;
    }

    return this.props.children;
  }
}
```

### 4. Backup and Recovery

```javascript
// Implement data backup
async function backupDatabase() {
  const timestamp = new Date().toISOString();
  const backupPath = `./backups/backup-${timestamp}.json`;
  
  const data = await mongoose.connection.db.collections();
  await fs.writeFile(backupPath, JSON.stringify(data));
  
  logger.info('Database backup created', { backupPath });
}
```

This troubleshooting guide should help you resolve most common issues. If you're still experiencing problems, please reach out to our support team with detailed information about your specific issue.