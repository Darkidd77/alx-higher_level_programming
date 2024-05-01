#!/bin/bash
# GET request to the URL, and displays the body of the response
curl -sSfL --location --write-out "%{http_code}\n"  "$1" | grep -E '^200$' && curl -sSf "$1"
