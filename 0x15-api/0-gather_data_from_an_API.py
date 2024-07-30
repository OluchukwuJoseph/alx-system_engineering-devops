#!/usr/bin/python3
"""
This script querys an API and returns information
about a User TODO list progress
"""
import requests
import sys


if __name__ == "__main__":
    user_id = sys.argv[1]

    URL = "http://jsonplaceholder.typicode.com/todos"
    PARAMS = f"userId={user_id}"
    response = requests.get(URL, params=PARAMS)

    if response.status_code == 200:

        # Get Total number of tasks
        TOTAL_NUMBER_OF_TASKS = len(response.json())
        n_params = f"id={user_id}"

        # Get Employee Name
        n_response = requests.get('http://jsonplaceholder.typicode.com/users',
                                  params=n_params)
        if n_response.status_code == 200:
            EMPLOYEE_NAME = n_response.json()[0]["name"]
            print(EMPLOYEE_NAME)
        else:
            sys.exit(1)

        # Get Number of done tasks
        NUMBER_OF_DONE_TASKS = 0
        for item in response.json():
            if item['completed'] is True:
                NUMBER_OF_DONE_TASKS += 1

        print("Employee {} is done with tasks({}/{}):"
              .format(EMPLOYEE_NAME,
                      NUMBER_OF_DONE_TASKS,
                      TOTAL_NUMBER_OF_TASKS))

        for item in response.json():
            if item['completed'] is True:
                print(f"\t {item['title']}")
