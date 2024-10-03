# server.py
from http.server import BaseHTTPRequestHandler, HTTPServer
import sys

# This class handles incoming HTTP GET requests
class SimpleServer(BaseHTTPRequestHandler):
    def do_GET(self):
        # Respond with an HTTP 200 OK status code
        self.send_response(200)
        
        # Set the response header to indicate HTML content
        self.send_header("Content-type", "text/html")
        self.end_headers()
        
        # Send the body of the response as bytes (text indicating which port the server is running on)
        self.wfile.write(bytes(f"Served from {sys.argv[1]}", "utf-8"))

if __name__ == "__main__":
    # Get the server port number from the command line argument (e.g., 8000, 8001)
    server_port = int(sys.argv[1])
    
    # Set the server address ('' means it will listen on all available IPs)
    server_address = ('', server_port)
    
    # Create the HTTP server instance with the specified port and handler class
    httpd = HTTPServer(server_address, SimpleServer)
    
    print(f"Starting server on port {server_port}")
    
    # Start the server, making it ready to handle incoming requests
    httpd.serve_forever()
