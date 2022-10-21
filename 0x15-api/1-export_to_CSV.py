#!/usr/bin/python3
"""export_to_CSV- Collects and exports employee data to CSV"""


if __name__ == "__main__":
    import csv
    import requests
    from sys import argv

    userId = int(argv[1])
    userReq = requests.get("https://jsonplaceholder.typicode.com/users/{}".
                           format(userId))
    todosReq = requests.get("https://jsonplaceholder.typicode.com/todos")
    userJson = userReq.json()
    todosJson = todosReq.json()
    userName = userJson.get("username")
    tasks = []
    for item in todosJson:
        if item.get("userId") == userId:
            tasks.append(item)
    with open("USER_ID.csv", mode="w") as csv_file:
        fieldnames = ["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS",
                      "TASK_TITLE"]
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames, delimiter=',', quotechar='"', quoting=csv.QUOTE_ALL)

        for task in tasks:
            writer.writerow({"USER_ID": userId, "USERNAME": userName,
                             "TASK_COMPLETED_STATUS": task.get("completed"),
                             "TASK_TITLE": task.get("title")})
