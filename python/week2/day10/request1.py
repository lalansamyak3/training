import requests

r = requests.get("https://jsonplaceholder.typicode.com/posts/1", timeout=10)
print(r.status_code)
print(r.text[:200])
print(r.elapsed)
print(r.json())  # convert json to python list of dicts
print(r.text)
print(r.content)
print(r.encoding)
print(r.headers)
print(r.request.headers)
print(r.request.url)
print(r.request.headers)
print(r.request)
print(r.ok)

r = requests.get("https://httpbin.org/image/png", timeout=10)
r.raise_for_status()

with open("pic.png", "wb") as f:
    """wrute binary sata to the di"""
    f.write(r.content)


"""query parameter normla query with special character and = may break the url so we 
can use params to send query parameter in key value form"""

params = {"userId": 1, "_limit": 5}
r = requests.get(
    "https://jsonplaceholder.typicode.com/posts", params=params, timeout=10
)

print(r.url)
# https://jsonplaceholder.typicode.com/posts?userId=1&_limit=5


r = requests.get(
    "https://httpbin.org/get", params={"tag": ["python", "api"]}, timeout=10
)
print(r.url)  # https://httpbin.org/get?tag=python&tag=api


with open("hello.txt", "w") as f:
    f.write("hello from my script")

with open("hello.txt", "rb") as f:
    r = requests.post("https://httpbin.org/post", files={"file": f}, timeout=30)

print(r.json()["files"])  # {'file': 'hello from my script'}
