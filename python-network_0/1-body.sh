#!/bin/bash
# sends a GET request and displays the body only if status code is 200
curl -s -o /tmp/response_body -w "%{http_code}" "$1" | grep -q "^200$" && cat /tmp/response_body
