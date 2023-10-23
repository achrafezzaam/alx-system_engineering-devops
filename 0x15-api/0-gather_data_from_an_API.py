#!/usr/bin/python3
''' Return information about user TODO list progress '''
import requests
from sys import argv

if __name__ == '__main__':
    url = 'https://jsonplaceholder.typicode.com/users/{}'.format(argv[1])
    username = requests.get(url).json()
    todos = requests.get(url + '/todos').json()
    finished = [todo for todo in todos if todo['completed']]
    print('Employee {} is done with tasks({}/{}):'.format(username["name"],
                                                          len(finished),
                                                          len(todos)))
    for todo in finished:
        print('\t {}'.format(todo['title']))
