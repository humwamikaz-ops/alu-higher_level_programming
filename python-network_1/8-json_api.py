#!/usr/bin/python3
"""sends a POST request to search_user with a letter parameter"""
import requests
import sys

if __name__ == "__main__":
    letter = sys.argv[1] if len(sys.argv) > 1 else ""
    response = requests.post("http://0.0.0.0:5000/search_user", data={"q": letter})
    try:
        json_data = response.json()
    except ValueError:
        print("Not a valid JSON")
    else:
        if not json_data:
            print("No result")
        else:
            print("[{}] {}".format(json_data.get("id"), json_data.get("name")))
