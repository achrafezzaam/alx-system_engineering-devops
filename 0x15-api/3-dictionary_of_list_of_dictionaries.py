#!/usr/bin/python3
''' Export information about users TODO list progress into a json file '''
import json
import requests

if __name__ == '__main__':
    url = 'https://jsonplaceholder.typicode.com/users'
    users = requests.get(url).json()
    new = {}
    for user in users:
        user_url = 'https://jsonplaceholder.typicode.com/users/{}'.format(
                    user["id"])
        todos = requests.get(user_url + '/todos').json()
        todos_list = []
        for todo in todos:
            todo_info = {"username": user['username'],
                         "task": todo['title'],
                         "completed": todo['completed']}
            todos_list.append(todo_info)
        new[user['id']] = todos_list
    with open('todo_all_employees.json', 'w') as file:
        json.dump(new, file)
