import requests
import json

access_token = "access_token"


def _url(path):
    return 'https://reqres.in/api' + path


def register_user(email, password):
    return requests.post(
        _url('/register'),
        data={"email": email, "password": password}
    )


def get_auth_token(email, password):
    return requests.post(
        _url('/login'),
        data={"email": email, "password": password}
    )
