from datetime import datetime, timedelta

def rate_limit(N, R, timestamps):
    # Define time window = 1 hour
    time_window = timedelta(hours=1)
    allowed_requests = R # Rate limit (request/hours)
    accepted_requests = [] # List to store the results
    time_queue = [] # List to keep track of timestamps within the current time window

    # Iterate through the timestamps of requests
    for timestamp in timestamps:
        # Convert the ISO-8601 timestamp to a datetime object
        current_time = datetime.fromisoformat(timestamp.replace("Z", "+00:00"))
        
        # Remove timestamps from the queue that are outside the 1-hour window
        time_queue = [t for t in time_queue if current_time - t < time_window]
        
        # Check if the number of requests in the current time window is within the allowed limit
        if len(time_queue) < allowed_requests:
            # Accept the request: add the current timestamp to the queue
            time_queue.append(current_time)
            accepted_requests.append(True)
        else:
            # Reject the request: rate limit exceeded
            accepted_requests.append(False)
    
    # Return the list of results (True/False for each request)
    return accepted_requests

if __name__ == "__main__":
    # Get values from input: N (number of requests), R (rate limit / hours)
    first_line = input().strip()
    N, R = map(int, first_line.split())  # Parse values from input

    # Store the incoming request timestamps
    timestamps = []
    for _ in range(N):
        # Read each timestamp line and add to the list
        line = input().strip()
        if line:
            timestamps.append(line)

    # Process rate limiting function
    results = rate_limit(N, R, timestamps)
    # Output the results for each request
    for result in results:
        print(result)
