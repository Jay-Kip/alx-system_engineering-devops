#!/usr/bin/python3
"""
extend your Python script to export data in the JSON format.
"""

import csv
import requests
import sys


if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"

    employee_id = sys.argv[1]
    user_response = requests.get(url + "users/{}".format(employee_id))

    user = user_response.json()
    params = {"UserId": employee_id}

    todos_response = requests.get(url + "todos", params=params)

    todos = todos_response.json()
    tasks - []

    for todo in todos:
        tasks.append({
            "tasks": todo.get("title"),
            "completed": todo.get("completed"),
            "username": user.get("username")
        })

    with open(f"{employee_id}.json", "w") as jsonfile:
        json.dump({employee_id: tasks}, jsonfile, indent=4)
