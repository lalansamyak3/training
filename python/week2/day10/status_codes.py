import requests

r = requests.get("https://jsonplaceholder.typicode.com/posts/1")

print(r.status_code, r.reason)

print(r.text[:200])

if r.status_code == 200:
    print("success")
elif r.status_code == 404:
    print("not found")
else:
    print("other error")
