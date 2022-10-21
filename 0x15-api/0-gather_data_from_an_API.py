#!/usr/bin/python3
"""gather_data_from_an_API- Gathers users task data from an API"""
import json
import requests
from sys import argv

userId = int(argv[1])
userReq = requests.get("https://jsonplaceholder.typicode.com/users/{}".
                       format(userId))
todosReq = requests.get("https://jsonplaceholder.typicode.com/todos")
userJson = userReq.json()
todosJson = todosReq.json()
inc = []
comp = []
for item in todosJson:
    if item["userId"] == userId:
        if item["completed"]:
            comp.append(item)
        else:
            inc.append(item)
print("Employee {} is done with tasks({}/{}):".
      format(userJson["name"], len(comp), (len(comp) + len(inc))))
for task in comp:
    print("\t {}".format(task["title"]))
