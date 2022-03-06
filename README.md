# EEL6761: Cloud Computing - Resources for the Homework 2 Extension

  In the assignment, you are required to submit a log file named "messages.txt" containing the raw HTTP requests and responses sent to and from the AWS APIs. This repository provides scripts that will help you build that log. If you choose to build a shell script rather than a Python script, see [For Shell Users](#for-shell-users) below.

## For Python Users

[print_http.py](print_http.py) contains functions to help you print your HTTP requests and responses. When you send a request using Python's "requests" library, you will receive a response object. Use that response object as the parameter to the function `print_request_and_response(your_response_object)` as demonstrated below. Before your can import the function using `from print_http import print_request_and_response`, you must copy the files of this repository (specifically, "\_\_init\_\_.py" and "print_http.py") to the same directory as your script.

Example usage:

```python
import requests
from print_http import print_request_and_response
response = requests.get("http://google.com")
print_request_and_response(response)
```

Output:
```
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

You can print the request and response directly to a file by adding the file name as the second parameter:

```python
print_request_and_response(response, "messages.txt")
```

Note that this will append to the file, not overwrite it, so you can call this function multiple times on the same file to record a sequence of requests and responses.

## For Shell Users

[log.py](log.py) parses the output of `awscurl --verbose 2>&1`, saves the raw HTTP requests and responses to a file, then echoes the body of the response. Note that you MUST include the `--verbose` (or `-v`) flag and redirect stderr to stdout using `2>&1`.

Without log.py:

```
$ awscurl https://google.com
<HTML><HEAD><meta http-equiv="content-type" content="text/html;charset=utf-8">
<TITLE>301 Moved</TITLE></HEAD><BODY>
<H1>301 Moved</H1>
The document has moved
<A HREF="https://www.google.com/">here</A>.
</BODY></HTML>
```

With log.py:

```
$ awscurl --verbose http://google.com 2>&1 | python3 ./log.py messages.txt
<HTML><HEAD><meta http-equiv="content-type" content="text/html;charset=utf-8">
<TITLE>301 Moved</TITLE></HEAD><BODY>
<H1>301 Moved</H1>
The document has moved
<A HREF="http://www.google.com/">here</A>.
</BODY></HTML>
```

Which appends the HTTP request sent to google.com and google.com's response to the file `messages.txt`:

```
$ cat messages.txt
---REQUEST---
GET / HTTP/1.1
Accept: application/xml
Content-Type: application/json
Authorization: AWS4-HMAC-SHA256 Credential=AKIA4EMPUKHPUB4YEMEV/20220306/us-east-1/execute-api/aws4_request, SignedHeaders=host;x-amz-date, Signature=7f5cea1ac1a80d9479e52245c523628dc69ef0f2d25f99da5e2cd533d860bc2f
x-amz-date: 20220306T013828Z
x-amz-security-token: None
x-amz-content-sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
host: google.com

---RESPONSE---
HTTP/1.1 301 MOVED_PERMANENTLY
Location: http://www.google.com/
Content-Type: text/html; charset=UTF-8
Date: Sun, 06 Mar 2022 01:38:30 GMT
Expires: Tue, 05 Apr 2022 01:38:30 GMT
Cache-Control: public, max-age=2592000
Server: gws
Content-Length: 219
X-XSS-Protection: 0
X-Frame-Options: SAMEORIGIN

<HTML><HEAD><meta http-equiv="content-type" content="text/html;charset=utf-8">
<TITLE>301 Moved</TITLE></HEAD><BODY>
<H1>301 Moved</H1>
The document has moved
<A HREF="http://www.google.com/">here</A>.
</BODY></HTML>
```

If you run `log.py` multiple times, you will build a list of requests and responses:

```
$ awscurl --verbose http://google.com 2>&1 | python3 ./log.py messages.txt
<HTML><HEAD><meta http-equiv="content-type" content="text/html;charset=utf-8">
<TITLE>301 Moved</TITLE></HEAD><BODY>
<H1>301 Moved</H1>
The document has moved
<A HREF="http://www.google.com/">here</A>.
</BODY></HTML>

$ awscurl --verbose http://google.com 2>&1 | python3 ./log.py messages.txt
<HTML><HEAD><meta http-equiv="content-type" content="text/html;charset=utf-8">
<TITLE>301 Moved</TITLE></HEAD><BODY>
<H1>301 Moved</H1>
The document has moved
<A HREF="http://www.google.com/">here</A>.
</BODY></HTML>
```

Then find two pairs of requests and responses inside `messages.txt`:

```
$ cat messages.txt
---REQUEST---
GET / HTTP/1.1
Accept: application/xml
Content-Type: application/json
Authorization: AWS4-HMAC-SHA256 Credential=AKIA4EMPUKHPUB4YEMEV/20220306/us-east-1/execute-api/aws4_request, SignedHeaders=host;x-amz-date, Signature=7f5cea1ac1a80d9479e52245c523628dc69ef0f2d25f99da5e2cd533d860bc2f
x-amz-date: 20220306T013828Z
x-amz-security-token: None
x-amz-content-sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
host: google.com

---RESPONSE---
HTTP/1.1 301 MOVED_PERMANENTLY
Location: http://www.google.com/
Content-Type: text/html; charset=UTF-8
Date: Sun, 06 Mar 2022 01:38:30 GMT
Expires: Tue, 05 Apr 2022 01:38:30 GMT
Cache-Control: public, max-age=2592000
Server: gws
Content-Length: 219
X-XSS-Protection: 0
X-Frame-Options: SAMEORIGIN

<HTML><HEAD><meta http-equiv="content-type" content="text/html;charset=utf-8">
<TITLE>301 Moved</TITLE></HEAD><BODY>
<H1>301 Moved</H1>
The document has moved
<A HREF="http://www.google.com/">here</A>.
</BODY></HTML>

---REQUEST---
GET / HTTP/1.1
Accept: application/xml
Content-Type: application/json
Authorization: AWS4-HMAC-SHA256 Credential=AKIA4EMPUKHPUB4YEMEV/20220306/us-east-1/execute-api/aws4_request, SignedHeaders=host;x-amz-date, Signature=7f5cea1ac1a80d9479e52245c523628dc69ef0f2d25f99da5e2cd533d860bc2f
x-amz-date: 20220306T013828Z
x-amz-security-token: None
x-amz-content-sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
host: google.com

---RESPONSE---
HTTP/1.1 301 MOVED_PERMANENTLY
Location: http://www.google.com/
Content-Type: text/html; charset=UTF-8
Date: Sun, 06 Mar 2022 01:38:30 GMT
Expires: Tue, 05 Apr 2022 01:38:30 GMT
Cache-Control: public, max-age=2592000
Server: gws
Content-Length: 219
X-XSS-Protection: 0
X-Frame-Options: SAMEORIGIN

<HTML><HEAD><meta http-equiv="content-type" content="text/html;charset=utf-8">
<TITLE>301 Moved</TITLE></HEAD><BODY>
<H1>301 Moved</H1>
The document has moved
<A HREF="http://www.google.com/">here</A>.
</BODY></HTML>
```
