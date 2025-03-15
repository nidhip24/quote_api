# Quotes API

A FastAPI-based RESTful API service for managing and generating quotes. This application provides endpoints to retrieve all quotes, get random quotes, and search quotes by author or keyword.

## Features

- Get all available quotes
- Generate random quotes
- Search quotes by author
- Search quotes by keyword
- JSON-based storage
- Comprehensive test coverage
- Docker support for containerization

## Prerequisites

- Python 3.8 or higher
- pip (Python package installer)
- Docker (optional, for containerized deployment)

## Installation

### Local Installation

1. Clone the repository:
```bash
git clone https://github.com/aagamjhaveri/prog8860-w25-cicd.git
cd quote_api
```

2. Create and activate a virtual environment (optional but recommended):
```bash
python -m venv venv
# On Windows
venv\Scripts\activate
# On macOS/Linux
source venv/bin/activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

## Running the Application

### Local Development
Start the application using uvicorn:
```bash
uvicorn main:app --reload
```

The API will be available at `http://localhost:8000`

### Docker Container
```bash
# Build the image
docker build -t quote_api:latest .

# Run the container
docker run -d -p 8080:8080 quote_api:latest

# View logs
docker logs [container_id|name]

# Stop the container
docker stop [container_id|name]
```

## Docker Configuration

The application includes a Dockerfile with the following features:
- Based on Python 3.9 slim image for minimal size
- Proper caching of dependencies
- Exposed port 8080
- Configured for production deployment

### Docker Commands

Common Docker commands for managing the application:
```bash
# Stop container
docker stop [contanier_id|name]

# Remove container
docker rm [contanier_id|name]

# List containers
docker ps

# View container logs
docker logs -f 

# Shell access to container
docker exec -it [contanier_id|name] /bin/bash
```

## API Endpoints

- `GET /`: Welcome message
- `GET /quotes`: Retrieve all quotes
- `GET /quotes/random`: Get a random quote
- `GET /quotes/search`: Search quotes with query parameters
  - Optional parameters:
    - `author`: Search by author name
    - `keyword`: Search by keyword in quote text

## Testing

Run the test suite using pytest:
```bash
pytest test_main.py
```

## API Documentation

Once the application is running, you can access the automatic API documentation at:
- Swagger UI: `http://localhost:8000/docs` (or `http://localhost:8080/docs` if using Docker)
- ReDoc: `http://localhost:8000/redoc` (or `http://localhost:8080/redoc` if using Docker)

## Example Usage

### Get all quotes
```bash
curl http://localhost:8080/quotes
```

### Get a random quote
```bash
curl http://localhost:8080/quotes/random
```

### Search quotes by author
```bash
curl http://localhost:8080/quotes/search?author=Einstein
```


### Search quotes by keyword
```bash
curl http://localhost:8080/quotes/search?keyword=life
```
