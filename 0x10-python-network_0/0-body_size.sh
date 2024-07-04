#!/usr/bin/env bash
# This script that takes in a URL, sends a request to that URL,
# and displays the size of the body of the response

if [[ $# == 1 ]]
then
    curl -s -D - "$1" | grep "Content-Length:" | awk '{print $2}'
fi
