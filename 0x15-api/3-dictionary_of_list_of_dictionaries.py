#!/usr/bin/python3
"""
This script querys an API and returns information
about all User TODO list progress and write data to a json file
"""
import json
import requests
import sys

if __name__ == "__main__":
    # Get all todos
    URL = "http://jsonplaceholder.typicode.com/todos"
    todo_response = requests.get(URL)
    if todo_response.status_code != 200:
        sys.exit(1)

    # Get all Employees
    URL = "http://jsonplaceholder.typicode.com/users"
    e_response = requests.get(URL)
    if e_response.status_code != 200:
        sys.exit(1)

    dictionary = {}
    for employee in e_response.json():
        user_id = employee['id']
        user_name = employee['username']
        dictionary.update({user_id: []})
        for task in todo_response.json():
            if task['userId'] == user_id:
                dictionary[user_id].append({
                                            "username": user_name,
                                            "task": task['title'],
                                            "completed": task['completed']})

    with open('todo_all_employees.json', 'w') as file:
        json.dump(dictionary, file)
