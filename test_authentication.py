import basic_setup
import requests
import json
from assertpy import assert_that

email = "eve.holt@reqres.in"
password = "cityslicka"
def test_get_auth_token_valid_user():
    response = basic_setup.get_auth_token(email, password)
    assert_that(response.status_code, '200').is_true()
    assert_that(json.loads(response.text)).contains(
        'token').does_not_contain('id')

def test_valid_user_registration():
    response = basic_setup.register_user(email, password)
    response_data = json.loads(response.text)
    assert_that(response.status_code, 200).is_true()
    assert_that("QpwL5tke4Pnpja7X4").is_in(response_data["token"])
    assert_that("4").is_in(response_data["id"])
    assert_that(response_data).contains('id')


def test_get_auth_token_invalid_password():
    response = basic_setup.get_auth_token("eve.holt@reqres.in", "")
    response_data = json.loads(response.text)
    assert_that(response.status_code, '400').is_true()
    assert_that(response_data).contains('error')
    assert_that(response_data).does_not_contain('token')


def test_get_auth_token_invalid_email():
    response = basic_setup.get_auth_token("eve.holt@", "cityslicka")
    response_data = json.loads(response.text)
    assert_that(response.status_code, '400').is_true()
    assert_that(response_data).contains('error')
    assert_that(response_data).does_not_contain('token')


def test_invalid_user_password_registration():
    response = basic_setup.register_user(email, '')
    response_data = json.loads(response.text)
    assert_that(response.status_code, 200).is_true()
    assert_that("Missing password").is_in(response_data["error"])
    assert_that(response_data).contains('error')
    assert_that(response_data).does_not_contain('token')


def test_invalid_user_email_registration():
    response = basic_setup.register_user("", password)
    response_data = json.loads(response.text)
    assert_that(response.status_code, 200).is_true()
    assert_that("Missing email or username").is_in(response_data["error"])
    assert_that(response_data).contains('error')
    assert_that(response_data).does_not_contain('token')


def test_invalid_user_registration():
    response = basic_setup.register_user("email@email.com", "password")
    response_data = json.loads(response.text)
    assert_that(response.status_code, 200).is_true()
    assert_that("Note: Only defined users succeed registration").is_in(response_data["error"])
    assert_that(response_data).contains('error')
    assert_that(response_data).does_not_contain('token')