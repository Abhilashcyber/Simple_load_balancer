import requests
import concurrent.futures

# Load balancer address
load_balancer_url = "http://localhost:8080"

def make_request(request_id):
    """
    Function to send a request to the load balancer and return the response.
    :param request_id: A unique identifier for the request.
    """
    try:
        # Send a GET request to the load balancer
        response = requests.get(f"{load_balancer_url}/request_{request_id}", timeout=10)
        return f"Request {request_id}: {response.text}"
    except Exception as e:
        return f"Request {request_id} failed: {e}"

if __name__ == "__main__":
    # Number of concurrent requests
    num_requests = 100

    # Use a ThreadPoolExecutor to handle parallel requests
    with concurrent.futures.ThreadPoolExecutor(max_workers=num_requests) as executor:
        # Submit 100 requests concurrently
        futures = [executor.submit(make_request, i) for i in range(num_requests)]

        # Wait for all the requests to complete and print their results
        for future in concurrent.futures.as_completed(futures):
            print(future.result())
