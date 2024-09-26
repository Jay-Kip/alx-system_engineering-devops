#!/usr/bin/python3
"""
extend your Python script to export data in the JSON format.
"""

import csv
import requests
import sys
import json


if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"

    user_id = sys.argv[1]
    user_response = requests.get(url + "users/{}".format(user_id))

    user = user_response.json()
    username = user.get("username")
    params = {"UserId": user_id}

    todos_response = requests.get(url + "todos", params=params)

    todos = todos_response.json()
    # completed - []

    # Create a dictionary containing the user and to-do list info
    data_to_export = {
        user_id: [
            {
                "task": t.get("title"),
                "completed": t.get("completed"),
                "username": username
            }
            for t in todos
        ]
    }

    with open(f"{user_id}.json", "w") as jsonfile:
        json.dump({data_to_export}, jsonfile, indent=4)
