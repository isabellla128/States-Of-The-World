import requests
import json

URL = "http://127.0.0.1:5000"


def get_method(route):
    """Display the response of the route"""
    response_api = requests.get(URL + route)
    if response_api.status_code == 200:
        data = response_api.text
        parse_json = json.loads(data)
        for line in parse_json:
            print(line)
    else:
        print("This route doesn't exist!")


def input_from_user():
    """Get input from user"""
    command = input("Enter a route: ")
    while True:
        if command == '' or command == 'exit':
            break
        get_method(command)
        command = input("Enter a route: ")


input_from_user()
