#!/bin/bash
# curl to fetch the URL and capture response body size in bytes
echo "SIZE=$(curl -s -o /dev/null -w '%{size_download}' "$URL")"
