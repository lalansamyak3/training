import requests

BASE = "https://jsonplaceholder.typicode.com"

# READ
r = requests.get(f"{BASE}/posts/1")
"""r is just holding the data coming after hitting the api"""
# CREATE
print(r.status_code, r.reason)
r = requests.post(f"{BASE}/posts", json={"title": "Hi", "body": "text", "userId": 1})

# REPLACE
r = requests.put(
    f"{BASE}/posts/1", json={"id": 1, "title": "New", "body": "x", "userId": 1}
)
print(r.status_code, r.reason)
print(r.status_code, r.reason)
# PARTIAL UPDATE
r = requests.patch(f"{BASE}/posts/1", json={"title": "Only title changed"})
print(r.status_code, r.reason)
# DELETE
r = requests.delete(f"{BASE}/posts/1")
print(r.status_code, r.reason)
# HEAD (headers only, no body downloaded)
r = requests.head(f"{BASE}/posts/1")
print(r.headers["Content-Type"])
"""this is the reposne header of the post request that is end """

# OPTIONS
r = requests.options(f"{BASE}/posts")
print(r.headers.get("Allow"))
