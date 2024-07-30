#!/usr/bin/python3
"""
This script querys an API and returns information
about a User TODO list progress and write data to a json file
"""
import json
import requests
import sys


if __name__ == "__main__":
    user_id = sys.argv[1]

    URL = "http://jsonplaceholder.typicode.com/todos"
    PARAMS = f"userId={user_id}"
    response = requests.get(URL, params=PARAMS)

    if response.status_code == 200:

        n_params = f"id={user_id}"

        # Get Employee Name
        n_response = requests.get('http://jsonplaceholder.typicode.com/users',
                                  params=n_params)
        if n_response.status_code == 200:
            user_name = n_response.json()[0]["username"]
        else:
            sys.exit(1)

        user_todos = {user_id: []}
        for item in response.json():
            user_todos[user_id].append({
                                         "task": item['title'],
                                         "completed": item['completed'],
                                         "username": user_name})

        with open(f'{user_id}.json', 'w') as file:
            json.dump(user_todos, file)
