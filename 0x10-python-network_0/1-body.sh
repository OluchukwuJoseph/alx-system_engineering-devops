#!/usr/bin/env bash
# This script takes in a URL, sends a GET request to the URL,
# and displays the body of the response.

if [[ $# == 1 ]]
then
    status=$(curl -s -D - -X GET "$1" -o tmp | grep "HTTP/1.1" | awk '{print $2}')
    if [[ $status == 200 ]]
    then
        cat tmp
        rm tmp
    fi
fi
