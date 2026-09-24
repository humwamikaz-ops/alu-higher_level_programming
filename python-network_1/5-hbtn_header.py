#!/usr/bin/python3
"""
Python script that displays X-Request-Id header value.
"""
import requests
import sys

if __name__ == "__main__":
    response = requests.get(sys.argv[1])
    print(response.headers.get("X-Request-Id"))
