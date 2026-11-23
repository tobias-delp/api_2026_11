# /// script
# requires-python = ">=3.12"
# dependencies = [
#   "httpx",
# ]
# ///

import httpx


def main() -> None:
    url = "https://jsonplaceholder.typicode.com/todos/1"
    print(f"Sende GET-Request an {url} ...\n")

    response = httpx.get(url, timeout=10.0)

    print(f"Status Code:  {response.status_code}")
    print(f"Content-Type: {response.headers.get('content-type')}")
    print("Response Body (JSON):")
    print(response.json())


if __name__ == "__main__":
    main()
