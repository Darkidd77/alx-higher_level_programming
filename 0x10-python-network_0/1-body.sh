#!/bin/bash
response=$(curl -o /tmp/response.txt -w -s "%{http_code}" "$1")
if [ "$(tail -n1 /tmp/response.txt)" == "200" ]; then cat /tmp/response.txt | sed '$d'
