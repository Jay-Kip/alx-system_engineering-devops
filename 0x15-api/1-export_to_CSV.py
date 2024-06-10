#!/usr/bin/python3
"""
extend your Python script to export data in the CSV format.
"""

import csv
import requests
import sys


if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"

    employee_id = sys.argv[1]
    user_response = requests.get(url + "users/{}".format(employee_id))

    user = user_response.json()
    params = {"userId": employee_id}

    todos_response = requests.get(url + "todos", params=params)

    todos = todos_response.json()
    completed = []

    for todo in todos:
        if todo.get("completed") is True:
            completed.append(todo.get("tittle"))

    with open(f"{employee_id}.csv", "w", newline="") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(
            ["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"])
        writer.writerow(completed)
