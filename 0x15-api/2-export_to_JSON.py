#!/usr/bin/python3
''' Export information about user TODO list progress into a json file '''
import json
import requests
from sys import argv

if __name__ == '__main__':
    url = 'https://jsonplaceholder.typicode.com/users/{}'.format(argv[1])
    username = requests.get(url).json()["username"]
    todos = requests.get(url + '/todos').json()
    todos_list = []
    for todo in todos:
        todo_info = {"task": todo['title'],
                     "completed": todo['completed'],
                     "username": username}
        todos_list.append(todo_info)
    new = {argv[1]: todos_list}
    with open('{}.json'.format(argv[1]), 'w') as file:
        json.dump(new, file)
