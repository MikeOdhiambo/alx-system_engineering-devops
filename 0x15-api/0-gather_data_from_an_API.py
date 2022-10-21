#!/usr/bin/python3
"""gather_data_from_an_API- Gathers users task data from an API"""


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
    inc = []
    comp = []
    for item in todosJson:
        if item.get("userId") == userId:
            if item.get("completed"):
                comp.append(item)
            else:
                inc.append(item)
    print("Employee {} is done with tasks({}/{}):".
          format(userJson.get("name"), len(comp), (len(comp) + len(inc))))
    for task in comp:
        print("\t {}".format(task.get("title")))
