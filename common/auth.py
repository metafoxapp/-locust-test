import csv
from random import choice

from faker import Faker
from locust import HttpUser

fake = Faker()
users = []

token_values = dict()

with open('./storage/data/users.csv') as csv_file:
    reader = csv.reader(csv_file, delimiter=',', quotechar='"')
    for row in reader:
        users.append(row)


def pick_random_user():
    user = choice(users)
    return dict(id=user[0], username=user[1], password=user[2])


def authenticate(http_user: HttpUser):
    ctx = http_user.context()

    username = ctx.get("username")
    password = ctx.get("password")

    if not token_values.get(username) is None:
        token = token_values.get(username)
        http_user.client.headers['Authorization'] = 'Bearer ' + token
        print("Re-use token for user " + username)

    else:
        with http_user.client.post('/api/v1/user/login', None, {
            'username': username,
            'password': password
        }) as response:
            token = response.json().get('access_token')

            # set auth token.
            if token is None:
                raise Exception("Login failure " + username + ":" + password)

            # save token to go back later
            token_values[username] = token
            ctx['token'] = token
            http_user.client.headers['Authorization'] = 'Bearer ' + token
