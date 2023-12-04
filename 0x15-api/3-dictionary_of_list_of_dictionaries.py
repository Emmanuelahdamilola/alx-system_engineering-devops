#!/usr/bin/env python3
"""
Fetches TODO list progress for all employees using a REST API.
"""

import requests
import json


if __name__ == '__main__':
    # Fetch information about all employees
    url = "https://jsonplaceholder.typicode.com/users"
    response = requests.get(url)
    employees = response.json()

    # Initialize a dictionary to store TODO list progress for each employee
    data = {}

    # Iterate over each employee
    for employee in employees:
        # Fetch TODO list for the current employee
        employee_id = employee['id']
        url = f"https://jsonplaceholder.typicode.com/todos?userId={employee_id}"
        response = requests.get(url)
        todos = response.json()

        # Store TODO list information in the data dictionary
        data[employee_id] = []
        for todo in todos:
            data[employee_id].append({
                "username": employee['username'],
                "task": todo['title'],
                "completed": todo['completed']
            })

    # Export the collected data to a JSON file
    filename = "todo_all_employees.json"
    with open(filename, mode='w') as file:
        json.dump(data, file)

    # Print a success message
    print(f"Data exported to {filename} successfully.")
