#!/usr/bin/env python3
"""
Simple HTTP Server for Calculator Frontend
========================================

A simple HTTP server to serve the calculator files.
"""

import http.server
import socketserver
import os

# Configuration
PORT = 3001
HOST = 'localhost'

# Change to the directory containing the files
os.chdir(os.path.dirname(os.path.abspath(__file__)))

class MyHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        # Add CORS headers
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')
        super().end_headers()

def main():
    print("🚀 Starting Simple Calculator Server...")
    print(f"📱 Server will be available at: http://{HOST}:{PORT}")
    print("⏹️  Press Ctrl+C to stop the server")
    
    try:
        with socketserver.TCPServer((HOST, PORT), MyHTTPRequestHandler) as httpd:
            httpd.serve_forever()
    except KeyboardInterrupt:
        print("\n👋 Server stopped!")
    except Exception as e:
        print(f"❌ Error: {e}")

if __name__ == '__main__':
    main()
