#!/bin/bash
# GET request to the URL, and displays the body of the response
curl -sL -o /dev/null -w "%{http_code}\n"  "$1" | grep 200 && curl -s "$1"
