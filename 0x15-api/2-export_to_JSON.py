#!/usr/bin/python3
"""export_to_JSON- Exports data in the JSON format"""


if __name__ == "__main__":
    import json
    import requests
    from sys import argv

    userId = int(argv[1])
    userReq = requests.get("https://jsonplaceholder.typicode.com/users/{}".
                           format(userId))
    todosReq = requests.get("https://jsonplaceholder.typicode.com/todos")
    userJson = userReq.json()
    todosJson = todosReq.json()
    dets = {}
    dets["{}".format(userId)] = []
    for todo in todosJson:
        entry = {"task": todo.get("title"),
                 "completed": todo.get("completed"),
                 "username": userJson.get("username")}
        dets.get("{}".format(userId)).append(entry)
    with open("USER_ID.json", "w", encoding="utf-8") as f:
        json.dump(dets, f)
