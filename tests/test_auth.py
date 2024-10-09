import pytest
import allure
import requests
from utils.config import Config

headers = {
        'Content-Type': 'application/json',
        }


@allure.title("Test Authentication Invalid Credentials")
@allure.description("This test attempts to validate creation of token ")
@allure.tag("auth", "create-token")
@allure.id("TC#1")
@pytest.mark.parametrize("username, password", [
    ("valid_user1", "valid_pass1"),
    ("valid_user2", "valid_pass2"),
    ("invalid_user", "invalid_pass"),
    ("",'password123'),
    ('admin',''),
    ('',''),
    (' admin ',' password123 '),

])
def test_create_token_invalid(username,password):
    payload = {
        "username":username,
        "password":password
    }
    response = requests.post(Config.auth_url,json=payload,headers=headers)
    print(response.status_code,response.text)
    assert response.status_code==400,f"Failed for {username}: {response.text}"
    assert "token" not in response.json().keys(),f"Failed as token found in response for {username}"
    assert "reason" in response.json().keys(),f"Failed as reason not found in response for {username}"


@allure.title("Test Authentication Valid Credentials")
@allure.description("This test attempts to validate creation of token ")
@allure.tag("auth", "create-token")
@allure.id("TC#2")
@pytest.mark.parametrize("username, password", [
    ('admin','password123')
])
def test_create_token_valid(username,password):
    payload = {
        "username":username,
        "password":password
    }
    response = requests.post(Config.auth_url,json=payload,headers=headers)
    print(response.status_code,response.text)
    assert response.status_code==200,f"Failed for {username}: {response.text}"
    assert "token" in response.json().keys(),f"Failed as token found in response {username}"
    assert len(response.json()['token'])>0



