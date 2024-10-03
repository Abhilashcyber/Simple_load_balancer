import requests

# Load balancer address (port 8080)
load_balancer_url = "http://localhost:8080"

# Simulate multiple client requests
for i in range(10):
    # Send a GET request to the load balancer
    response = requests.get(f"{load_balancer_url}/request_{i}")
    
    # Print the response from the load balancer (which is forwarded from a backend server)
    print(f"Client received: {response.text}")
