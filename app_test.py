# Modules
import requests

# Constants
baseUrl = 'http://127.0.0.1:5000'

# User Testing
def test_createUser():
    user = {'username': 'Mock', 'displayname': 'Name', 'password': 'password'}

    response = requests.post(url = baseUrl + '/users/createUser', data = user)

    userId = response.json()['result'][0]

    assert userId == 4

# Post testing
def test_getPost():
    title = {'id': 3}

    response = requests.get(url = baseUrl + '/posts/getPost', data = title, headers={'Authorization': 'Bearer c9b85ec8f3054a80d30f6e380ab851549e03ee74429e6b21959845eaab8ffd6d'})

    postId = response.json()['result'][0]

    assert postId == 3

# Login testing
def test_login():
    credentials = {'username': 'user', 'password': 'pass'}

    response = requests.post(url = baseUrl + '/login', data = credentials)

    token = response.json()['result'][1]

    assert token != ''