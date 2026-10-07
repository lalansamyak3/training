from urllib.parse import urlparse, parse_qs

url = "https://api.example.com:443/v1/users/42?active=true&limit=10#section"
p = urlparse(url)

print(p.scheme)  # https
print(p.netloc)  # api.example.com:443
print(p.path)  # /v1/users/42
print(parse_qs(p.query))  # {'active': ['true'], 'limit': ['10']}
print(p.fragment)  # section
