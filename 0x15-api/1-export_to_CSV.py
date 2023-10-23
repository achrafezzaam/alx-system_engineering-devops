#!/usr/bin/python3
''' Export information about user TODO list progress into a csv file '''
import requests
from sys import argv

if __name__ == '__main__':
    url = 'https://jsonplaceholder.typicode.com/users/{}'.format(argv[1])
    username = requests.get(url).json()["username"]
    todos = requests.get(url + '/todos').json()

    with open('{}.csv'.format(argv[1]), 'w', newline='') as file:
        for todo in todos:
            file.write('"{}","{}","{}","{}"\n'
                       .format(argv[1], username,
                               todo['completed'], todo['title']))
