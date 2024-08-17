import pytest
import requests

# Получить токен авторизации
@pytest.fixture()
def get_token(user='musa', password='music-fairy'):
    creds = {
        "username": user,
        "password": password
    }
    resp = requests.post('https://x-clients-be.onrender.com' + '/auth/login', json=creds)
    token = resp.json()["userToken"]
    return token
    
