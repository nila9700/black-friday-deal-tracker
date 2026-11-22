# Black Friday Deal Tracker

A full-stack web application for tracking and comparing Black Friday deals across multiple stores. Built with FastAPI, featuring real-time price comparison, deal legitimacy checking, and comprehensive CI/CD automation.


## Features

### Core Functionality
- **Multi-Store Price Comparison**: Compare prices across multiple retailers for the same product
- **Real-Time Countdown**: Live countdown timer to Black Friday 2026
- **Deal Legitimacy Checker**: AI-powered system to identify potentially fake deals
- **Price History Tracking**: 30-day price history visualization with interactive charts
- **Advanced Search**: Search deals by name, category, or subcategory
- **Category Filtering**: Browse deals by product categories and subcategories
- **Top Stores Ranking**: Discover stores with the best average discounts
- **Responsive Design**: Beautiful dark-themed UI that works on all devices

### Technical Features
- **RESTful API**: Well-documented API with 15+ endpoints
- **Docker Support**: Fully containerized application
- **Automated Testing**: Comprehensive test suite with 20+ test cases
- **CI/CD Pipeline**: Automated testing, building, and deployment with GitHub Actions
- **Health Checks**: Built-in health monitoring endpoints
- **Artifact Management**: Automatic archival of test results and logs

## Tech Stack

**Backend:**
- FastAPI 0.115.6 - Modern Python web framework
- Uvicorn 0.32.1 - ASGI server
- Pydantic - Data validation

**Frontend:**
- HTML5, CSS3, JavaScript (ES6+)
- Chart.js - Price history visualization
- Google Fonts (Inter) - Typography

**DevOps:**
- Docker - Containerization
- GitHub Actions - CI/CD automation
- pytest 8.3.4 - Testing framework
- Ruff 0.8.2 - Fast Python linter

**Testing:**
- pytest - Unit and integration testing
- httpx 0.28.1 - Async HTTP client for testing
- FastAPI TestClient - API testing

## Installation

### Prerequisites
- Python 3.12 or higher
- Docker and Docker Compose (optional)
- Git

### Local Setup

1. **Clone the repository:**
```bash
git clone https://github.com/YOUR_USERNAME/YOUR_REPO.git
cd YOUR_REPO
```

2. **Create and activate virtual environment:**
```bash
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. **Install dependencies:**
```bash
pip install -r requirements.txt
```

4. **Run the application:**
```bash
uvicorn app.main:app --host 0.0.0.0 --port 8000
```

5. **Open your browser:**
Navigate to `http://localhost:8000`

### Docker Setup

1. **Build the Docker image:**
```bash
docker build -t deal-tracker .
```

2. **Run the container:**
```bash
docker run -d -p 8000:8000 --name deal-app deal-tracker
```

3. **Access the application:**
Navigate to `http://localhost:8000`

4. **Stop the container:**
```bash
docker stop deal-app
docker rm deal-app
```

## API Documentation

Once the application is running, access the interactive API documentation:

- **Swagger UI**: http://localhost:8000/docs
- **ReDoc**: http://localhost:8000/redoc

### Key Endpoints

#### Deals Management
- `GET /deals` - Get all deals
- `GET /deals/best` - Get deals sorted by best savings
- `GET /deals/{deal_id}` - Get specific deal by ID
- `POST /deals` - Add a new deal
- `GET /deals/search?q={query}` - Search deals

#### Filtering & Comparison
- `GET /deals/category/{category}` - Filter deals by category
- `GET /deals/category/{category}?subcategory={sub}` - Filter by subcategory
- `POST /deals/compare` - Compare multiple deals

#### Utilities
- `GET /health` - Health check endpoint
- `GET /countdown` - Get countdown to Black Friday
- `GET /categories` - Get all categories
- `GET /deals/{deal_id}/legit` - Check deal legitimacy

### Example API Request

```bash
# Get all deals
curl http://localhost:8000/deals

# Search for Nike products
curl http://localhost:8000/deals/search?q=nike

# Check if a deal is legitimate
curl http://localhost:8000/deals/1/legit

# Health check
curl http://localhost:8000/health
```

## Testing

### Run Tests Locally

```bash
# Run all tests
pytest

# Run with verbose output
pytest -v

# Run specific test file
pytest tests/test_api.py

# Generate test coverage
pytest --cov=app tests/
```

### Test Coverage

The project includes comprehensive tests covering:
- ✅ All API endpoints (20+ test cases)
- ✅ Data validation and error handling
- ✅ Business logic (savings calculation, deal comparison)
- ✅ Edge cases and invalid inputs
- ✅ Integration testing with TestClient

## CI/CD Pipeline

The project uses GitHub Actions for automated CI/CD:

### Pipeline Stages

1. **Test Stage**
   - Checkout code
   - Set up Python 3.12
   - Install dependencies
   - Run linting with Ruff
   - Execute pytest test suite
   - Upload test results as artifacts

2. **Docker Stage**
   - Build Docker image
   - Run container
   - Wait for application startup
   - Verify deployment with health checks
   - Upload verification logs

### Artifacts

The pipeline automatically saves:
- **test-results.xml** - JUnit-formatted test results
- **verify-log.txt** - Deployment verification logs

Access artifacts from the Actions tab in your GitHub repository.

### Triggering the Pipeline

The CI/CD pipeline runs automatically on:
- Push to `main` branch
- Pull requests targeting `main` branch

## Deployment

### Manual Deployment

```bash
# Build and tag the image
docker build -t deal-tracker:latest .

# Tag previous version for rollback
docker tag deal-tracker:latest deal-tracker:previous

# Run the new version
docker run -d -p 8000:8000 --name deal-app deal-tracker:latest

# Verify deployment
bash scripts/verify.sh
```

### Rollback

If something goes wrong, use the rollback script:

```bash
bash scripts/rollback_local.sh
```

This will:
1. Stop the current container
2. Remove the failed container
3. Start the previous version
4. Verify the rollback was successful

## Project Structure

```
.
├── app/
│   ├── __init__.py
│   ├── main.py              # FastAPI application and routes
│   ├── deals.py             # Business logic and data models
│   └── static/
│       └── index.html       # Frontend application
├── tests/
│   ├── __init__.py
│   ├── test_api.py          # API endpoint tests
│   └── test_deals.py        # Business logic tests
├── scripts/
│   ├── verify.sh            # Deployment verification script
│   └── rollback_local.sh    # Rollback script
├── .github/
│   └── workflows/
│       └── ci.yml           # GitHub Actions CI/CD pipeline
├── Dockerfile               # Docker container configuration
├── requirements.txt         # Python dependencies
├── .gitignore              # Git ignore rules
└── README.md               # This file
```

## Application Architecture

### Backend (FastAPI)
- **main.py**: API routes, request/response models, error handling
- **deals.py**: Core business logic, data management, calculations

### Frontend
- Single-page application with vanilla JavaScript
- Real-time search and filtering
- Modal-based product detail views
- Interactive price history charts
- Responsive design with CSS Grid and Flexbox

### Data Model

Each deal contains:
- Product information (name, description, category)
- Multiple store listings with prices and stock status
- 30-day price history
- Calculated savings (amount and percentage)
- Best price identification across stores

## Deal Legitimacy Checker

The application includes an intelligent deal verification system:

| Discount | Status | Message |
|----------|--------|---------|
| > 80% | Suspicious (Red) | Likely fake - discounts over 80% are extremely rare |
| 50-80% | Check (Yellow) | Verify carefully - double-check original price |
| < 50% | Legit (Green) | Reasonable for Black Friday |

## Development

### Code Style

The project uses Ruff for linting and code formatting:

```bash
# Check code style
ruff check .

# Format code
ruff format .
```

### Adding New Features

1. Create a feature branch
2. Implement your changes
3. Add tests for new functionality
4. Run tests locally: `pytest -v`
5. Ensure linting passes: `ruff check .`
6. Submit a pull request

## Environment Variables

The application can be configured using environment variables:

| Variable | Description | Default |
|----------|-------------|---------|
| `HOST` | Server host | 0.0.0.0 |
| `PORT` | Server port | 8000 |
| `LOG_LEVEL` | Logging level | info |

## Performance

- API response time: < 100ms for most endpoints
- Docker image size: ~150MB (Python 3.12-slim base)
- Application startup time: ~2-3 seconds
- Test execution time: ~1-2 seconds

## Browser Support

- Chrome 90+
- Firefox 88+
- Safari 14+
- Edge 90+

## Security

- Input validation using Pydantic models
- CORS configuration for production deployment
- SQL injection prevention (not using SQL database)
- XSS protection through proper HTML escaping

## Troubleshooting

### Application won't start
```bash
# Check if port 8000 is already in use
netstat -tuln | grep 8000

# Kill the process using the port
kill -9 $(lsof -ti:8000)
```

### Docker container fails to start
```bash
# Check container logs
docker logs deal-app

# Remove old containers and images
docker rm $(docker ps -aq)
docker rmi deal-tracker
```

### Tests failing
```bash
# Clean pytest cache
pytest --cache-clear

# Reinstall dependencies
pip install --force-reinstall -r requirements.txt
```

## Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

Please ensure:
- All tests pass
- Code follows the project style (use Ruff)
- Documentation is updated
- Commit messages are clear and descriptive

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- [FastAPI](https://fastapi.tiangolo.com/) - Modern web framework
- [Chart.js](https://www.chartjs.org/) - Beautiful charts
- [Unsplash](https://unsplash.com/) - Product images
- [Google Fonts](https://fonts.google.com/) - Inter font family

## Contact

For questions, issues, or suggestions, please open an issue on GitHub.

---

**Note**: This is an educational project demonstrating modern DevOps practices including Docker, CI/CD, automated testing, and deployment automation. The deals and prices are fictional and for demonstration purposes only.
