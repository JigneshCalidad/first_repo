#!/usr/bin/env python3
"""
Frontend Server for Professional Calculator
==========================================

A simple HTTP server to serve the calculator frontend.
This allows the frontend to make API calls without CORS issues.

Usage:
    python server.py

The frontend will be available at: http://localhost:3000
"""

import http.server
import socketserver
import os
import sys
from pathlib import Path

# Configuration
PORT = 3001
HOST = 'localhost'

class CustomHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    """Custom handler to serve files with proper MIME types"""
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=os.path.dirname(os.path.abspath(__file__)), **kwargs)
    
    def end_headers(self):
        # Add CORS headers for API calls
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')
        super().end_headers()
    
    def do_OPTIONS(self):
        """Handle preflight requests"""
        self.send_response(200)
        self.end_headers()
    
    def guess_type(self, path):
        """Override to set correct MIME types"""
        mimetype, encoding = super().guess_type(path)
        
        # Ensure JavaScript files are served with correct MIME type
        if path.endswith('.js'):
            return 'application/javascript'
        elif path.endswith('.css'):
            return 'text/css'
        elif path.endswith('.html'):
            return 'text/html'
        
        return mimetype

def start_server():
    """Start the HTTP server"""
    try:
        with socketserver.TCPServer((HOST, PORT), CustomHTTPRequestHandler) as httpd:
            print("🚀 Starting Professional Calculator Frontend Server...")
            print(f"📱 Frontend available at: http://{HOST}:{PORT}")
            print(f"🔗 Make sure the backend API is running on port 8000")
            print("\n📖 Usage:")
            print("   1. Start backend: cd ../backend && python sum_api.py")
            print("   2. Start frontend: python server.py")
            print("   3. Open browser: http://localhost:3001")
            print("\n⏹️  Press Ctrl+C to stop the server")
            
            httpd.serve_forever()
            
    except KeyboardInterrupt:
        print("\n👋 Server stopped!")
    except OSError as e:
        if e.errno == 48:  # Address already in use
            print(f"❌ Error: Port {PORT} is already in use!")
            print("   Try using a different port or stop the process using this port.")
        else:
            print(f"❌ Error starting server: {e}")
        sys.exit(1)

if __name__ == '__main__':
    start_server()
