# Pipes the output of "awscurl --verbose" into this script to print the HTTP request and
# response to a file. Echos the response to stdout. For awscurl, be sure to redirect
# stderr to stdout using 2>&1 (see example below).
#
# Usage:
#   python save-requests.py FILE
# e.g.,
#   awscurl --verbose http://google.com 2>&1 | python ./save-requests.py messages.txt

MAX_BYTES_TO_READ = 1048576

import sys
import re
import ast
from urllib.parse import urlsplit
from functools import reduce
from collections import namedtuple
from print_http import print_request_and_response

lines = [line.rstrip() for line in sys.stdin.readlines(MAX_BYTES_TO_READ)]

def find(lines, pattern, fallback):
    return next((match[1] for match in filter(None, (re.search(pattern, line) for line in lines))), fallback)

request_index = next((i for (i, line) in enumerate(lines) if line.find("HEADERS+") >= 0), None)
response_index = next((i for (i, line) in enumerate(lines) if line.find("RESPONSE+") >= 0), None)
url = find(lines, "Request URL = ([^']*)", "")
split_url = urlsplit(url)
path_url = split_url.path + split_url.query + split_url.fragment

assert request_index != None, "Couldn't find request headers in awscurl's output"
assert response_index != None, "Couldn't find response headers in awscurl's output"

request = {
    "method": find(lines, r"CANONICAL REQUEST = ([^\\]*)", "GET"),
    "url": url,
    "path_url": path_url if path_url.startswith("/") else "/" + path_url,
    "headers": ast.literal_eval(lines[request_index + 1]),
    "body": None
}
request =  namedtuple("ReconstructedRequest", request.keys())(*request.values())

if request.path_url == "": request.path_url = "/"

response = {
    "status_code": int(find(lines, "Response code: ([0-9]*)", None)),
    "headers": ast.literal_eval(lines[response_index + 2]),
    "content": bytes("\n".join(lines[response_index + 4:]), "utf-8"),
    "request": request
}
response =  namedtuple("ReconstructedResponse", response.keys())(*response.values())

# Echo response
print(response.content.decode("utf-8", "ignore"))

# Append request and response to a file
assert len(sys.argv) >=2, "You must specify a file to save the HTTP request and response to"
assert len(sys.argv) == 2, "Too many arguments provided for " + sys.argv[0]

file_name = sys.argv[1]
with open(file_name, 'a') as file:
    sys.stdout = file
    print_request_and_response(response)
    print()