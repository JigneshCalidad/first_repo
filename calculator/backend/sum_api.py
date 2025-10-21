"""
Calculator API - Complete Calculator Service
==========================================

This module creates a comprehensive REST API using Flask that provides a full calculator service.
Supports addition, subtraction, multiplication, and division operations.

Author: Professional Calculator API
Date: 2024
"""

# Import Flask and related modules
from flask import Flask, request, jsonify
from flask_cors import CORS
import json

# Create Flask application instance
# __name__ tells Flask where to find resources (templates, static files, etc.)
app = Flask(__name__)

# Enable CORS for all origins on all routes
CORS(app)

# Enable JSON pretty printing for better readability
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True

@app.route('/calculate', methods=['GET', 'POST'])
def calculate():
    """
    Perform mathematical operations on two numbers.
    
    This endpoint accepts two parameters 'a' and 'b' plus an operation and returns the result.
    
    Methods supported:
    - GET: Parameters passed as query string (?a=5&b=3&operation=add)
    - POST: Parameters passed in JSON body {"a": 5, "b": 3, "operation": "add"}
    
    Supported operations:
    - add: Addition (a + b)
    - subtract: Subtraction (a - b)
    - multiply: Multiplication (a * b)
    - divide: Division (a / b)
    
    Returns:
        JSON response with the result or error message
    """
    try:
        # Handle both GET and POST requests
        if request.method == 'GET':
            # For GET requests, get parameters from query string
            a = request.args.get('a')
            b = request.args.get('b')
            operation = request.args.get('operation', 'add')
        else:  # POST request
            # For POST requests, get parameters from JSON body
            data = request.get_json()
            if not data:
                return jsonify({
                    'error': 'No JSON data provided',
                    'message': 'Please provide JSON data with "a", "b", and "operation" parameters'
                }), 400
            
            a = data.get('a')
            b = data.get('b')
            operation = data.get('operation', 'add')
        
        # Check if both parameters are provided
        if a is None or b is None:
            return jsonify({
                'error': 'Missing parameters',
                'message': 'Both "a" and "b" parameters are required',
                'example_get': '/calculate?a=5&b=3&operation=add',
                'example_post': '{"a": 5, "b": 3, "operation": "add"}'
            }), 400
        
        # Convert to numbers and validate
        try:
            a_num = float(a)
            b_num = float(b)
        except (ValueError, TypeError):
            return jsonify({
                'error': 'Invalid input type',
                'message': 'Both "a" and "b" must be valid numbers',
                'received': {'a': a, 'b': b}
            }), 400
        
        # Validate operation
        valid_operations = ['add', 'subtract', 'multiply', 'divide']
        if operation not in valid_operations:
            return jsonify({
                'error': 'Invalid operation',
                'message': f'Operation must be one of: {", ".join(valid_operations)}',
                'received': operation
            }), 400
        
        # Perform the calculation
        if operation == 'add':
            result = a_num + b_num
            operation_name = 'addition'
            symbol = '+'
        elif operation == 'subtract':
            result = a_num - b_num
            operation_name = 'subtraction'
            symbol = '-'
        elif operation == 'multiply':
            result = a_num * b_num
            operation_name = 'multiplication'
            symbol = '×'
        elif operation == 'divide':
            if b_num == 0:
                return jsonify({
                    'error': 'Division by zero',
                    'message': 'Cannot divide by zero',
                    'parameters': {'a': a_num, 'b': b_num}
                }), 400
            result = a_num / b_num
            operation_name = 'division'
            symbol = '÷'
        
        # Return successful response
        return jsonify({
            'operation': operation_name,
            'symbol': symbol,
            'parameters': {
                'a': a_num,
                'b': b_num
            },
            'expression': f'{a_num} {symbol} {b_num}',
            'result': result,
            'status': 'success'
        }), 200
        
    except Exception as e:
        # Handle any unexpected errors
        return jsonify({
            'error': 'Internal server error',
            'message': str(e),
            'status': 'error'
        }), 500

@app.route('/health', methods=['GET'])
def health_check():
    """
    Health check endpoint to verify the API is running.
    
    Returns:
        JSON response indicating API status
    """
    return jsonify({
        'status': 'healthy',
        'service': 'Calculator API',
        'version': '1.0.0'
    }), 200

@app.route('/', methods=['GET'])
def api_info():
    """
    Root endpoint providing API information and usage examples.
    
    Returns:
        JSON response with API documentation
    """
    return jsonify({
        'service': 'Professional Calculator API',
        'version': '2.0.0',
        'description': 'A comprehensive calculator API supporting all basic arithmetic operations',
        'endpoints': {
            '/calculate': {
                'methods': ['GET', 'POST'],
                'description': 'Perform mathematical operations on two numbers',
                'parameters': {
                    'a': 'First number',
                    'b': 'Second number',
                    'operation': 'Operation type (add, subtract, multiply, divide)'
                },
                'examples': {
                    'GET': '/calculate?a=5&b=3&operation=add',
                    'POST': '{"a": 5, "b": 3, "operation": "add"}'
                },
                'supported_operations': {
                    'add': 'Addition (a + b)',
                    'subtract': 'Subtraction (a - b)',
                    'multiply': 'Multiplication (a × b)',
                    'divide': 'Division (a ÷ b)'
                }
            },
            '/health': {
                'methods': ['GET'],
                'description': 'Check API health status'
            }
        }
    }), 200

# Error handlers for common HTTP errors
@app.errorhandler(404)
def not_found(error):
    """Handle 404 Not Found errors"""
    return jsonify({
        'error': 'Not Found',
        'message': 'The requested endpoint does not exist',
        'available_endpoints': ['/', '/sum', '/health']
    }), 404

@app.errorhandler(405)
def method_not_allowed(error):
    """Handle 405 Method Not Allowed errors"""
    return jsonify({
        'error': 'Method Not Allowed',
        'message': 'The HTTP method is not supported for this endpoint'
    }), 405

# Main execution block
if __name__ == '__main__':
    # Run the Flask development server
    print("🚀 Starting Professional Calculator API...")
    print("📊 Available endpoints:")
    print("   GET/POST /calculate - All calculator operations")
    print("   GET /health - Health check")
    print("   GET / - API information")
    print("\n🌐 Server will be available at: http://localhost:8000")
    print("📖 Example usage:")
    print("   curl 'http://localhost:8000/calculate?a=5&b=3&operation=add'")
    print("   curl -X POST -H 'Content-Type: application/json' -d '{\"a\":5,\"b\":3,\"operation\":\"add\"}' http://localhost:8000/calculate")
    
    # Start the server with debug mode enabled for development
    app.run(debug=True, host='0.0.0.0', port=8000)
