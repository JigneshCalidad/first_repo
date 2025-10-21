"""
Test Script for Calculator API
=============================

This script demonstrates how to test the calculator API using the requests library.
It includes examples of successful requests and error handling.

Run this script after starting the API server.
"""

import requests
import json

# API base URL
BASE_URL = "http://localhost:8000"

def test_api():
    """Test various API endpoints and scenarios"""
    
    print("🧪 Testing Calculator API")
    print("=" * 50)
    
    # Test 1: Health check
    print("\n1. Testing health check...")
    try:
        response = requests.get(f"{BASE_URL}/health")
        print(f"Status: {response.status_code}")
        print(f"Response: {json.dumps(response.json(), indent=2)}")
    except requests.exceptions.ConnectionError:
        print("❌ Error: Could not connect to API. Make sure the server is running!")
        return
    
    # Test 2: API information
    print("\n2. Testing API information...")
    response = requests.get(f"{BASE_URL}/")
    print(f"Status: {response.status_code}")
    print(f"Response: {json.dumps(response.json(), indent=2)}")
    
    # Test 3: GET request - addition
    print("\n3. Testing GET request (5 + 3)...")
    response = requests.get(f"{BASE_URL}/calculate", params={'a': 5, 'b': 3, 'operation': 'add'})
    print(f"Status: {response.status_code}")
    print(f"Response: {json.dumps(response.json(), indent=2)}")
    
    # Test 4: POST request - multiplication
    print("\n4. Testing POST request (10 × 20)...")
    data = {'a': 10, 'b': 20, 'operation': 'multiply'}
    response = requests.post(f"{BASE_URL}/calculate", json=data)
    print(f"Status: {response.status_code}")
    print(f"Response: {json.dumps(response.json(), indent=2)}")
    
    # Test 5: Division
    print("\n5. Testing division (15 ÷ 3)...")
    response = requests.get(f"{BASE_URL}/calculate", params={'a': 15, 'b': 3, 'operation': 'divide'})
    print(f"Status: {response.status_code}")
    print(f"Response: {json.dumps(response.json(), indent=2)}")
    
    # Test 6: Subtraction
    print("\n6. Testing subtraction (20 - 8)...")
    response = requests.get(f"{BASE_URL}/calculate", params={'a': 20, 'b': 8, 'operation': 'subtract'})
    print(f"Status: {response.status_code}")
    print(f"Response: {json.dumps(response.json(), indent=2)}")
    
    # Test 5: Error case - missing parameters
    print("\n5. Testing error case - missing parameters...")
    response = requests.get(f"{BASE_URL}/sum")
    print(f"Status: {response.status_code}")
    print(f"Response: {json.dumps(response.json(), indent=2)}")
    
    # Test 6: Error case - invalid parameters
    print("\n6. Testing error case - invalid parameters...")
    response = requests.get(f"{BASE_URL}/sum", params={'a': 'abc', 'b': 3})
    print(f"Status: {response.status_code}")
    print(f"Response: {json.dumps(response.json(), indent=2)}")
    
    # Test 7: Error case - non-existent endpoint
    print("\n7. Testing error case - non-existent endpoint...")
    response = requests.get(f"{BASE_URL}/nonexistent")
    print(f"Status: {response.status_code}")
    print(f"Response: {json.dumps(response.json(), indent=2)}")
    
    print("\n✅ All tests completed!")

def interactive_test():
    """Interactive testing function"""
    print("\n🎮 Interactive Testing")
    print("=" * 30)
    
    while True:
        try:
            print("\nEnter two numbers to add (or 'quit' to exit):")
            a = input("First number: ").strip()
            if a.lower() == 'quit':
                break
                
            b = input("Second number: ").strip()
            if b.lower() == 'quit':
                break
            
            # Convert to integers
            a_int = int(a)
            b_int = int(b)
            
            # Make API request
            response = requests.get(f"{BASE_URL}/sum", params={'a': a_int, 'b': b_int})
            
            if response.status_code == 200:
                result = response.json()
                print(f"✅ Result: {a_int} + {b_int} = {result['result']}")
            else:
                print(f"❌ Error: {response.json()}")
                
        except ValueError:
            print("❌ Please enter valid integers!")
        except KeyboardInterrupt:
            print("\n👋 Goodbye!")
            break
        except requests.exceptions.ConnectionError:
            print("❌ Error: Could not connect to API. Make sure the server is running!")
            break

if __name__ == "__main__":
    print("🚀 Calculator API Test Suite")
    print("Make sure the API server is running (python sum_api.py)")
    print("Press Enter to continue or Ctrl+C to exit...")
    
    try:
        input()
        test_api()
        
        # Ask if user wants interactive testing
        choice = input("\nWould you like to try interactive testing? (y/n): ").strip().lower()
        if choice in ['y', 'yes']:
            interactive_test()
            
    except KeyboardInterrupt:
        print("\n👋 Goodbye!")
