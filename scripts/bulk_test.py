import time
import requests
from concurrent.futures import ThreadPoolExecutor
import os

api_endpoint = "http://localhost:8000/v1/embeddings"
valid_models = [
    "bge-base-en",
    "gte-base",
    "all-MiniLM-L6-v2",
]

response_code_counts = {
    200: 0,
    400: 0,
    401: 0,
    403: 0,
    404: 0,
    429: 0,
    500: 0,
    503: 0,
}


def post_request():
    rand_str = os.urandom(128).hex()
    rand_model = valid_models[os.urandom(1)[0] % len(valid_models)]
    data = {
        "model": rand_model,
        "input": "Hey, is this API working? Here's a random string to prevent caching:"
        + rand_str,
    }
    response = requests.post(api_endpoint, json=data)
    response_code_counts[response.status_code] = (
        response_code_counts.get(response.status_code, 0) + 1
    )


def load_test():
    num_threads = os.cpu_count()
    seconds = 120
    print(
        "Running load test with {} threads for {} seconds.".format(num_threads, seconds)
    )
    start_time = time.time()
    total_reqs = 0
    with ThreadPoolExecutor(max_workers=num_threads) as executor:
        while time.time() - start_time < seconds:
            executor.submit(post_request)
            total_reqs += 1
            time.sleep(0.05)

    print("Finished! Sent {} total requests.".format(total_reqs))
    print("Response code counts:")
    print(response_code_counts)


if __name__ == "__main__":
    load_test()
