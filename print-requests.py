# Functions for building raw HTTP requests and responses when using Python's
# requests library.
#
# e.g.,
#   response = requests.get("http://google.com")
#   print_request_and_response(response)

def print_request_and_response(response):
    print("---REQUEST---")
    print(get_raw_request(response.request))
    print("\n---RESPONSE---")
    print(get_raw_response(response))

# Don't use this except for debugging purposes
def get_raw_request(prepared_request):
    from urllib.parse import urlsplit
    headers = prepared_request.headers.copy()
    headers["host"] = urlsplit(prepared_request.url).netloc
    return "{} {} {}\n{}{}".format(
        prepared_request.method,
        prepared_request.path_url,
        "HTTP/1.1",
        "\n".join('{}: {}'.format(key, value) for key, value in headers.items()),
        "\n\n" + prepared_request.body.decode("utf-8", "ignore") if prepared_request.body != None else "")

# Don't use this except for debugging purposes
def get_raw_response(response):
    from http import HTTPStatus
    return "{} {} {}\n{}{}".format(
        "HTTP/1.1",
        response.status_code,
        HTTPStatus(response.status_code).name,
        "\n".join('{}: {}'.format(key, value) for key, value in response.headers.items()),
        "\n\n" + response.content.decode("utf-8", "ignore") if response.content != None else "")