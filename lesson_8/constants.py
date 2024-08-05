import pytest
import requests

# Получить токен авторизации
@pytest.fixture()
def get_token(self, user='musa', password='music-fairy'):
    creds = {
        "username": user,
        "password": password
    }
    resp = requests.post(self.url + '/auth/login', json=creds)
    token = resp.json()["userToken"]
    return token
    
