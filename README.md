# EEL6761: Cloud Computing - Resources for the Homework 2 Extension

For Python users, [print-requests.py](print-requests.py) contains functions to help you print your HTTP requests and responses.

Example usage:

```python
>>> response = requests.get("http://google.com")
>>> print_request_and_response(response)

---REQUEST---
GET / HTTP/1.1
User-Agent: python-requests/2.23.0
Accept-Encoding: gzip, deflate
Accept: */*
Connection: keep-alive
host: www.google.com

---RESPONSE---
HTTP/1.1 200 OK
Date: Thu, 03 Mar 2022 19:22:58 GMT
Expires: -1
Cache-Control: private, max-age=0
Content-Type: text/html; charset=ISO-8859-1
P3P: CP="This is not a P3P policy! See g.co/p3phelp for more info."
Content-Encoding: gzip
Server: gws
Content-Length: 6311
X-XSS-Protection: 0
X-Frame-Options: SAMEORIGIN
Set-Cookie: 1P_JAR=2022-03-03-19; expires=Sat, 02-Apr-2022 19:22:58 GMT; path=/; domain=.google.com; Secure, NID=511=Av3AtPB_SjmTLuQfTGOuLqrwUwOQ-kGR7qlyJvDzbUu740OSpfzZitwl9DSTeV7prt57_UcN9ZIN7wI0eeA_ZHuM0stN8dfmIyLqjdZqwdTVWLKAhN75CXs2fY_jOI4uCnp9qafna1k8KN-ar3NQc1-r-md1tfvULzUVuYNGevs; expires=Fri, 02-Sep-2022 19:22:58 GMT; path=/; domain=.google.com; HttpOnly

<!doctype html><html itemscope="" itemtype="http://schema.org/WebPage" lang="en" ...
```

For shell users, [save-messages.py](save-messages.py) parses the output of `awscurl --verbose 2>&1`' and saves the raw HTTP requests and responses to a file.

Example usage:

```bash
```
