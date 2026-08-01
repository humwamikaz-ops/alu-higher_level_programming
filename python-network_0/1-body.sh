#!/bin/bash
# Displays the body of the response only for a 200 status code
curl -sL -o /tmp/body -w "%{http_code}" "$1" | grep -q "^200$" && cat /tmp/body
