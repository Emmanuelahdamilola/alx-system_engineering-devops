#!/usr/bin/python3
"""
Python script that, using this REST API, for a given employee ID, returns information about his/her TODO list progress.
"""

import requests
import sys


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} EMPLOYEE_ID")
        sys.exit(1)

    employee_id = sys.argv[1]
    url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
    response = requests.get(url)
    employee = response.json()

    url = f"https://jsonplaceholder.typicode.com/todos?userId={employee_id}"
    response = requests.get(url)
    todos = response.json()

    total_tasks = len(todos)
    done_tasks = sum(1 for todo in todos if todo['completed'])

    print(f"Employee {employee['name']} is done with tasks({done_tasks}/{total_tasks}):")
    for todo in todos:
        if todo['completed']:
            print(f"\t {todo['title']}")
