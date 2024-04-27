#!/bin/bash
# if URL argument is provided
if [ -z "$1" ]; then
    echo "Usage: $0 <URL>"
    exit 1
fi

URL=$1

# curl to fetch the URL and capture response body size in bytes
# -w '%{size_download}': Print the size of response
SIZE=$(curl -s -o /dev/null -w '%{size_download}' "$URL")

echo "$SIZE"
