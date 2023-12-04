#!/usr/bin/python3
"""
Python script that, using this REST API, returns TODO list progress for a given employee ID.
"""

import csv  # Import CSV module for handling CSV files
import requests  # Import the requests module for making HTTP requests
import sys  # Import sys module for command-line arguments


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
    print(f"Employee {employee['name']} is done with tasks ({done_tasks}/{total_tasks}):")
    for todo in todos:
        if todo['completed']:
            print(f"\t {todo['title']}")

    # Export data to a CSV file
    filename = f"{employee_id}.csv"
    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file,
                            delimiter=',',
                            quotechar='"',
                            quoting=csv.QUOTE_ALL)

        for todo in todos:
            writer.writerow([
                employee_id,
                employee['username'],
                todo['completed'],
                todo['title']
            ])

    print(f"Data exported to {filename} successfully.")
