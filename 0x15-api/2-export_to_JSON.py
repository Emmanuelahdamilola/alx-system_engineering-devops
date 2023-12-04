#!/usr/bin/env python3
"""
Returns TODO list progress for a given employee ID using a REST API.
"""

import requests
import sys
import json


if __name__ == '__main__':
    # Check if the correct number of command-line arguments is provided
    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} EMPLOYEE_ID")
        sys.exit(1)

    # Extract employee ID from command-line arguments
    employee_id = sys.argv[1]

    # Fetch employee information from the API
    url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
    response = requests.get(url)
    employee = response.json()

    # Fetch TODO list for the employee from the API
    url = f"https://jsonplaceholder.typicode.com/todos?userId={employee_id}"
    response = requests.get(url)
    todos = response.json()

    # Calculate total and completed tasks
    total_tasks = len(todos)
    done_tasks = sum(1 for todo in todos if todo['completed'])

    # Display employee's progress and completed tasks
    print(f"Employee {employee['name']} is done with tasks "
          f"({done_tasks}/{total_tasks}):")

    for todo in todos:
        if todo['completed']:
            print(f"\t {todo['title']}")

    # Export data to a JSON file
    filename = f"{employee_id}.json"
    data = {employee_id: []}
    for todo in todos:
        data[employee_id].append({
            "task": todo['title'],
            "completed": todo['completed'],
            "username": employee['username']
        })
    with open(filename, mode='w') as file:
        json.dump(data, file)

    print(f"Data exported to {filename} successfully.")
