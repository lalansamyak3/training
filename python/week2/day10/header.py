import requests

url = "https://httpbin.org/headers"

headers = {"Accept": "application/json", "User-Agent": "MyPythonApp/1.0"}

response = requests.get(url, headers=headers)

# Request details
print("----- REQUEST -----")
print("Method:", response.request.method)
print("URL:", response.request.url)
"""what client is sending to the server and method used for sending the request """
print("Headers:", response.request.headers)

"""response status too see the kind of response in 200,201..."""
print("\n----- RESPONSE -----")
print("Status Code:", response.status_code)
"""response header is what server is sending the client """
print("Response Headers:", response.headers)
"""response body kya returjn karr rahi h"""
print("Response Body:", response.text)

# JSON response
print("\n----- JSON -----")
print(response.json())

# ============================================================
# HTTP HEADERS
# ============================================================
#
# Header = metadata/information about an HTTP request or response.
#
# Format:
#
# Header-Name: value
#
# Example:
#
# Accept: application/json
#
# Header names are case-insensitive:
#
# Content-Type
# content-type
# CONTENT-TYPE
#
# They refer to the same header.
#
#
# ============================================================
# REQUEST HEADERS
# ============================================================
#
# Request headers are mainly sent:
#
# Client  --------------------->  Server
#
#
# ------------------------------------------------------------
# 1. Host
# ------------------------------------------------------------
#
# Tells the server which host/domain the client wants to access.
#
# Example:
#
# Host: api.example.com
#
# Situation:
# Client wants to access:
# https://api.example.com/users
#
# Host: api.example.com
#
# Remember:
# Host = "Which host/domain am I talking to?"
#
# Host is required in HTTP/1.1 requests.
#
#
# ------------------------------------------------------------
# 2. Accept
# ------------------------------------------------------------
#
# Tells the server which response media types the client
# is willing to receive/prefer.
#
# Example:
#
# Accept: application/json
#
# Means:
# "I want/prefer JSON as the response format."
#
# Another example:
#
# Accept: application/xml
#
# Means:
# "I want/prefer XML as the response format."
#
# IMPORTANT:
#
# Accept = What format the CLIENT wants to RECEIVE.
#
# Content-Type = What format is actually being SENT.
#
#
# Example:
#
# GET /users
# Accept: application/json
#
# Server:
#
# Content-Type: application/json
#
# Response body:
#
# {
#     "name": "Samyak"
# }
#
#
# ------------------------------------------------------------
# Content Negotiation
# ------------------------------------------------------------
#
# If an API supports both JSON and XML:
#
# Client:
#
# Accept: application/xml
#
# Server can return:
#
# Content-Type: application/xml
#
# If client sends:
#
# Accept: application/json
#
# Server can return:
#
# Content-Type: application/json
#
#
# If the client requests XML:
#
# Accept: application/xml
#
# but the API only supports JSON:
#
# 406 Not Acceptable
#
# because the server cannot provide an acceptable representation.
#
#
# ------------------------------------------------------------
# 3. Content-Type
# ------------------------------------------------------------
#
# Tells the receiver the media type/format of the message body.
#
# Example:
#
# Content-Type: application/json
#
# Means:
# "The body I'm sending is JSON."
#
# Example:
#
# POST /users
# Content-Type: application/json
#
# {
#     "name": "Samyak",
#     "age": 22
# }
#
# IMPORTANT:
#
# Content-Type = What format am I SENDING?
#
# Accept = What format do I WANT BACK?
#
#
# ------------------------------------------------------------
# 4. Authorization
# ------------------------------------------------------------
#
# Used to send authentication credentials/token.
#
# Common example:
#
# Authorization: Bearer <token>
#
# Example:
#
# GET /profile
# Authorization: Bearer eyJhbGciOi...
#
# Situation:
#
# User logs in
#       ↓
# Server gives token
#       ↓
# Client stores token
#       ↓
# Client sends token with protected requests
#
# If authentication is required but credentials are missing
# or invalid, the API may return:
#
# 401 Unauthorized
#
#
# Common types:
#
# Authorization: Bearer <token>
#
# Authorization: Basic <credentials>
#
#
# ------------------------------------------------------------
# 5. User-Agent
# ------------------------------------------------------------
#
# Identifies the client/software making the request.
#
# Example:
#
# User-Agent: Mozilla/5.0
#
# Another example:
#
# User-Agent: my-app/1.0
#
# Another example:
#
# User-Agent: Python/3.12
#
# Situation:
# Server may want to know whether the request came from:
#
# - Browser
# - Mobile application
# - Python application
# - Bot/crawler
# - Custom application
#
#
# ------------------------------------------------------------
# 6. Accept-Encoding
# ------------------------------------------------------------
#
# Tells the server which content encodings/compression formats
# the client supports.
#
# Example:
#
# Accept-Encoding: gzip, deflate
#
# Means:
# "You can compress the response using formats I support."
#
# Without compression:
#
# Server
#   ↓
# Large response
#   ↓
# Client
#
# With compression:
#
# Server
#   ↓
# gzip compressed response
#   ↓
# Client
#
# This can reduce the amount of data transferred.
#
#
# ------------------------------------------------------------
# 7. If-None-Match
# ------------------------------------------------------------
#
# Used for conditional requests and caching.
#
# Usually works together with the ETag response header.
#
# First response from server:
#
# ETag: "abc123"
#
# Client stores the resource and ETag.
#
# Later client sends:
#
# If-None-Match: "abc123"
#
# Means:
# "Has the resource changed since the version I have?"
#
# If it has NOT changed:
#
# 304 Not Modified
#
# Client can use its cached copy.
#
#
# ------------------------------------------------------------
# 8. Cookie
# ------------------------------------------------------------
#
# Sends cookies from the client to the server.
#
# Example:
#
# Cookie: session=xyz123
#
# Situation:
#
# Server previously sent:
#
# Set-Cookie: session=xyz123
#
# Browser stores it.
#
# Later browser sends:
#
# Cookie: session=xyz123
#
# Server can use the cookie to identify the session.
#
# Remember:
#
# Server → Set-Cookie
# Client → Cookie
#
#
# ============================================================
# RESPONSE HEADERS
# ============================================================
#
# Response headers are mainly sent:
#
# Client  <---------------------  Server
#
#
# ------------------------------------------------------------
# 9. Content-Type
# ------------------------------------------------------------
#
# Tells the client the format/media type of the response body.
#
# Example:
#
# Content-Type: application/json
#
# Body:
#
# {
#     "name": "Samyak"
# }
#
# Another example:
#
# Content-Type: application/xml
#
# Body:
#
# <user>
#     <name>Samyak</name>
# </user>
#
# Remember:
#
# Request Content-Type:
# "What format am I sending?"
#
# Response Content-Type:
# "What format am I returning?"
#
#
# ------------------------------------------------------------
# 10. Content-Length
# ------------------------------------------------------------
#
# Tells the client the size of the message body in bytes.
#
# Example:
#
# Content-Length: 120
#
# Means:
# The body contains 120 bytes.
#
#
# ------------------------------------------------------------
# 11. Location
# ------------------------------------------------------------
#
# Tells the client a URL/location associated with the response.
#
# Common situations:
#
# 1. Redirect
#
# HTTP/1.1 301 Moved Permanently
# Location: https://example.com/new-page
#
# Client can follow the new location.
#
#
# 2. Resource created
#
# HTTP/1.1 201 Created
# Location: /users/123
#
# Means:
# The newly created user is available at /users/123.
#
#
# ------------------------------------------------------------
# 12. Set-Cookie
# ------------------------------------------------------------
#
# Sent by the server to tell the client/browser to store a cookie.
#
# Example:
#
# Set-Cookie: session=xyz123
#
# Client stores it.
#
# Later:
#
# Cookie: session=xyz123
#
# Remember:
#
# Server → Set-Cookie
# Client → Cookie
#
#
# ------------------------------------------------------------
# 13. Cache-Control
# ------------------------------------------------------------
#
# Controls caching behavior.
#
# Example:
#
# Cache-Control: max-age=3600
#
# Means:
# The response can be considered fresh for 3600 seconds.
#
#
# Another example:
#
# Cache-Control: no-store
#
# Means:
# Do not store the response in cache.
#
# Common situation:
#
# Sensitive/private information:
#
# Cache-Control: no-store
#
# Cacheable public content:
#
# Cache-Control: max-age=3600
#
#
# ------------------------------------------------------------
# 14. ETag
# ------------------------------------------------------------
#
# Identifies a particular version of a resource.
#
# Example:
#
# ETag: "abc123"
#
# Think of ETag as a version/fingerprint of the resource.
#
# First response:
#
# ETag: "abc123"
#
# Later client sends:
#
# If-None-Match: "abc123"
#
# Server checks whether the resource changed.
#
# If unchanged:
#
# 304 Not Modified
#
# If changed:
# Server sends the new resource and a new ETag.
#
# Remember:
#
# ETag
#     ↓
# Server tells client the resource version.
#
# If-None-Match
#     ↓
# Client asks whether that version is still current.
#
#
# ------------------------------------------------------------
# 15. Retry-After
# ------------------------------------------------------------
#
# Tells the client how long it should wait before retrying.
#
# Commonly used with:
#
# 429 Too Many Requests
# 503 Service Unavailable
#
# Example:
#
# HTTP/1.1 429 Too Many Requests
# Retry-After: 60
#
# Means:
# Wait approximately 60 seconds before retrying.
#
#
# Another example:
#
# HTTP/1.1 503 Service Unavailable
# Retry-After: 120
#
# Means:
# Try again after about 120 seconds.
#
#
# ------------------------------------------------------------
# 16. Link
# ------------------------------------------------------------
#
# Provides links related to the current resource/response.
#
# A common API use is pagination.
#
# Example concept:
#
# Current page:
# /users?page=1
#
# Next page:
# /users?page=2
#
# A Link header can communicate the next/previous related URLs.
#
# Common in APIs that support pagination.
#
#
# ------------------------------------------------------------
# 17. X-RateLimit-Remaining
# ------------------------------------------------------------
#
# A common/custom convention used by APIs to tell the client
# how many requests remain in the current rate-limit window.
#
# Example:
#
# X-RateLimit-Remaining: 42
#
# Means:
# Approximately 42 requests remain under the applicable limit.
#
# You may also see:
#
# X-RateLimit-Limit
# X-RateLimit-Remaining
# X-RateLimit-Reset
#
# Example:
#
# X-RateLimit-Limit: 100
# X-RateLimit-Remaining: 42
#
#
# ------------------------------------------------------------
# 18. Access-Control-Allow-Origin
# ------------------------------------------------------------
#
# Related to CORS:
# Cross-Origin Resource Sharing.
#
# Mainly important for browsers.
#
# Example:
#
# Access-Control-Allow-Origin: http://localhost:3000
#
# Means the server allows browser requests from that origin,
# subject to the server's CORS configuration.
#
# Example:
#
# Frontend:
# http://localhost:3000
#
# API:
# http://localhost:8000
#
# These are different origins.
#
# The API can specify which origins are allowed.
#
# IMPORTANT:
# CORS is primarily a browser security mechanism.
#
#
# ============================================================
# MOST IMPORTANT DIFFERENCES
# ============================================================
#
#
# Accept
#     ↓
# What response format does the client want/accept?
#
# Content-Type
#     ↓
# What format is the body being sent/returned in?
#
#
# Example:
#
# POST /users
# Accept: application/json
# Content-Type: application/json
#
# Meaning:
#
# "I am sending JSON."
# "I want JSON back."
#
#
# ============================================================
# COOKIE vs SET-COOKIE
# ============================================================
#
# Set-Cookie:
# Server → Client
#
# Cookie:
# Client → Server
#
#
# ============================================================
# ETAG vs IF-NONE-MATCH
# ============================================================
#
# ETag:
# Server → Client
#
# "This is the version/fingerprint of this resource."
#
# If-None-Match:
# Client → Server
#
# "Is this version still current?"
#
#
# ============================================================
# IMPORTANT STATUS CODE CONNECTIONS
# ============================================================
#
#
# Accept problem:
#
# Client:
# Accept: application/xml
#
# API supports only JSON
#
# → 406 Not Acceptable
#
#
# Content-Type problem:
#
# Client sends:
# Content-Type: application/xml
#
# But API does not support/accept XML request bodies.
#
# → 415 Unsupported Media Type
#
#
# Authentication problem:
#
# Authorization missing/invalid
#
# → 401 Unauthorized
#
#
# Permission problem:
#
# User is authenticated but doesn't have permission.
#
# → 403 Forbidden
#
#
# Rate limit exceeded:
#
# → 429 Too Many Requests
#
#
# Temporary server unavailable:
#
# → 503 Service Unavailable
#
#
# ============================================================
# QUICK REVISION
# ============================================================
#
# Host
# → Which host/domain?
#
# Accept
# → What response format do I want?
#
# Content-Type
# → What format is the body?
#
# Authorization
# → Who am I / what credentials am I providing?
#
# User-Agent
# → What client/software is calling?
#
# Accept-Encoding
# → What compression can I understand?
#
# If-None-Match
# → Has my cached version changed?
#
# Cookie
# → Which stored cookies am I sending?
#
# Content-Length
# → How many bytes are in the body?
#
# Location
# → Where is the resource / where should I go?
#
# Set-Cookie
# → Store this cookie.
#
# Cache-Control
# → How should this response be cached?
#
# ETag
# → What version/fingerprint is this resource?
#
# Retry-After
# → When should I try again?
#
# Link
# → Related resource/URL links.
#
# X-RateLimit-Remaining
# → How many requests remain?
#
# Access-Control-Allow-Origin
# → Which browser origins are allowed by CORS?
#
#
# ============================================================
# SIMPLE REQUEST → RESPONSE EXAMPLE
# ============================================================
#
# CLIENT
#
# GET /users HTTP/1.1
# Host: api.example.com
# Accept: application/json
# Authorization: Bearer abc123
# User-Agent: my-app/1.0
#
#
# SERVER
#
# HTTP/1.1 200 OK
# Content-Type: application/json
# Content-Length: 120
# Cache-Control: max-age=3600
# ETag: "abc123"
#
# {
#     "id": 1,
#     "name": "Samyak"
# }
#
#
# ============================================================
# MAIN MEMORY TRICK
# ============================================================
#
# Host
#     → WHERE am I sending?
#
# Accept
#     → WHAT do I want BACK?
#
# Content-Type
#     → WHAT am I sending/returning?
#
# Authorization
#     → WHO am I / what credentials do I have?
#
# User-Agent
#     → WHO/WHAT is making the request?
#
# Cookie
#     → WHAT stored session information am I sending?
#
# Set-Cookie
#     → WHAT cookie should I store?
#
# Location
#     → WHERE is the resource / redirect?
#
# Cache-Control
#     → HOW should this be cached?
#
# ETag
#     → WHICH VERSION is this?
#
# If-None-Match
#     → HAS MY VERSION CHANGED?
#
# Retry-After
#     → WHEN should I TRY AGAIN?
#
# ============================================================
