#!/bin/bash
# sends a request to the URL passed as argument and displays body size in bytes
curl -s -o /dev/null -w "%{size_download}\n" "$1"
