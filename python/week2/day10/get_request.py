import requests
from requests.exceptions import HTTPError, ConnectionError, Timeout, RequestException

url = "https://jsonplaceholder.typicode.com/posts"
params = {"userId": 1, "_limit": 3}  # becomes ?userId=1&_limit=3
headers = {
    "Accept": "application/json",
    "User-Agent": "study-script/1.0",
}

try:
    """sending the request with uirl,peram in key value form and header"""
    response = requests.get(url, params=params, headers=headers, timeout=10)
    response.raise_for_status()  # raises an error for 4xx/5xx

    # RECEIVE and SEE the output
    print("request sendd")
    print("Method :", response.request.method)
    print("URL    :", response.request.url)
    print("Headers:", dict(response.request.headers))

    print("\nresponse ")
    print("Status code :", response.status_code, response.reason)
    print("Content-Type:", response.headers["Content-Type"])
    print("Time taken  :", response.elapsed.total_seconds(), "seconds")

    print("\n raw response to get 200 characters")
    print(response.text[:200])
    """    slicing op[erator top see first 200 characters"""

    print("\n PARSED JSON")
    """reponse was in json format so we can use .json() to convert it into python list of dicts"""
    data = response.json()
    for post in data:
        print(f"Post {post['id']}: {post['title'][:40]}")

except Timeout:
    print("Server too slow")
except ConnectionError:
    print("Network problem / wrong domain")
except HTTPError as e:
    print("Bad status:", e.response.status_code)
except ValueError:
    print("Response was not valid JSON")
except RequestException as e:
    print("Something else went wrong:", e)
