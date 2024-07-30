#!/usr/bin/python3
"""
This script querys an API and returns information
about a User TODO list progress and write data to CSV file
"""
import requests
import sys


if __name__ == "__main__":
    user_id = sys.argv[1]

    URL = "http://jsonplaceholder.typicode.com/todos"
    PARAMS = f"userId={user_id}"
    response = requests.get(URL, params=PARAMS)

    if response.status_code == 200:

        # Get Employee Name
        n_params = f"id={user_id}"
        n_response = requests.get('http://jsonplaceholder.typicode.com/users',
                                  params=n_params)
        if n_response.status_code == 200:
            user_name = n_response.json()[0]["username"]
        else:
            sys.exit(1)

        with open(f"{user_id}.csv", 'w') as file:
            for item in response.json():
                file.write('"{}","{}","{}","{}"\n'
                           .format(user_id,
                                   user_name,
                                   item['completed'],
                                   item['title']))
