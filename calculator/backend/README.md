# Calculator API - Sum Endpoint

A simple REST API built with Flask that provides calculator functionality. This API accepts two integers and returns their sum.

## 🚀 Quick Start

### 1. Install Dependencies

```bash
# Navigate to the backend directory
cd calculator/backend

# Install required packages
pip install -r requirements.txt
```

### 2. Run the API

```bash
python sum_api.py
```

The API will start on `http://localhost:5000`

## 📚 API Documentation

### Endpoints

#### 1. Sum Calculation
- **URL**: `/sum`
- **Methods**: `GET`, `POST`
- **Description**: Calculate the sum of two integers

#### 2. Health Check
- **URL**: `/health`
- **Methods**: `GET`
- **Description**: Check if the API is running

#### 3. API Information
- **URL**: `/`
- **Methods**: `GET`
- **Description**: Get API documentation and usage examples

## 🔧 Usage Examples

### GET Request (Query Parameters)

```bash
# Using curl
curl "http://localhost:5000/sum?a=5&b=3"

# Response
{
  "operation": "addition",
  "parameters": {
    "a": 5,
    "b": 3
  },
  "result": 8,
  "status": "success"
}
```

### POST Request (JSON Body)

```bash
# Using curl
curl -X POST \
  -H "Content-Type: application/json" \
  -d '{"a": 10, "b": 20}' \
  http://localhost:5000/sum

# Response
{
  "operation": "addition",
  "parameters": {
    "a": 10,
    "b": 20
  },
  "result": 30,
  "status": "success"
}
```

### Python Example

```python
import requests

# GET request
response = requests.get('http://localhost:5000/sum', params={'a': 5, 'b': 3})
print(response.json())

# POST request
data = {'a': 10, 'b': 20}
response = requests.post('http://localhost:5000/sum', json=data)
print(response.json())
```

### JavaScript Example

```javascript
// GET request
fetch('http://localhost:5000/sum?a=5&b=3')
  .then(response => response.json())
  .then(data => console.log(data));

// POST request
fetch('http://localhost:5000/sum', {
  method: 'POST',
  headers: {
    'Content-Type': 'application/json',
  },
  body: JSON.stringify({a: 10, b: 20})
})
.then(response => response.json())
.then(data => console.log(data));
```

## 🧪 Testing the API

### 1. Test with curl

```bash
# Test GET request
curl "http://localhost:5000/sum?a=5&b=3"

# Test POST request
curl -X POST -H "Content-Type: application/json" -d '{"a":5,"b":3}' http://localhost:5000/sum

# Test health check
curl "http://localhost:5000/health"

# Test API info
curl "http://localhost:5000/"
```

### 2. Test Error Cases

```bash
# Missing parameters
curl "http://localhost:5000/sum"

# Invalid parameters
curl "http://localhost:5000/sum?a=abc&b=3"

# Non-existent endpoint
curl "http://localhost:5000/nonexistent"
```

## 🏗️ How It Works - Code Explanation

### 1. Flask Application Setup

```python
from flask import Flask, request, jsonify

app = Flask(__name__)
```

**What it does**: 
- Imports Flask framework and necessary modules
- Creates a Flask application instance
- `__name__` tells Flask where to find resources

**Why**: Flask is a lightweight web framework perfect for creating REST APIs quickly.

### 2. Route Decorators

```python
@app.route('/sum', methods=['GET', 'POST'])
def calculate_sum():
```

**What it does**: 
- `@app.route()` decorator maps URLs to functions
- `/sum` is the endpoint URL
- `methods=['GET', 'POST']` specifies which HTTP methods are allowed

**Why**: This creates a RESTful endpoint that can handle both GET and POST requests.

### 3. Request Handling

```python
if request.method == 'GET':
    a = request.args.get('a')
    b = request.args.get('b')
else:  # POST request
    data = request.get_json()
    a = data.get('a')
    b = data.get('b')
```

**What it does**: 
- For GET: Extracts parameters from query string (`?a=5&b=3`)
- For POST: Extracts parameters from JSON body

**Why**: Different HTTP methods have different ways of passing data, so we handle both.

### 4. Input Validation

```python
try:
    a_int = int(a)
    b_int = int(b)
except (ValueError, TypeError):
    return jsonify({'error': 'Invalid input type'}), 400
```

**What it does**: 
- Converts string inputs to integers
- Catches conversion errors and returns appropriate error message

**Why**: APIs should validate inputs and provide clear error messages.

### 5. JSON Response

```python
return jsonify({
    'operation': 'addition',
    'parameters': {'a': a_int, 'b': b_int},
    'result': result,
    'status': 'success'
}), 200
```

**What it does**: 
- Creates a structured JSON response
- Includes input parameters, result, and status
- Returns HTTP status code 200 (success)

**Why**: Consistent JSON responses make the API predictable and easy to use.

## 🔍 Error Handling

The API includes comprehensive error handling:

- **400 Bad Request**: Missing or invalid parameters
- **404 Not Found**: Non-existent endpoints
- **405 Method Not Allowed**: Unsupported HTTP methods
- **500 Internal Server Error**: Unexpected errors

## 🚀 Production Deployment

For production deployment, consider:

1. **Use a production WSGI server**:
   ```bash
   pip install gunicorn
   gunicorn -w 4 -b 0.0.0.0:5000 sum_api:app
   ```

2. **Add environment variables**:
   ```python
   import os
   port = int(os.environ.get('PORT', 5000))
   app.run(host='0.0.0.0', port=port)
   ```

3. **Add logging**:
   ```python
   import logging
   logging.basicConfig(level=logging.INFO)
   ```

## 📝 Next Steps

- Add more mathematical operations (subtract, multiply, divide)
- Implement authentication
- Add rate limiting
- Create API documentation with Swagger
- Add unit tests
- Implement database storage for calculation history

## 🤝 Contributing

Feel free to extend this API with additional features or improvements!
