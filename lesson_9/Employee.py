import pytest
import requests
import json
from Automation.lesson_9.conftest import get_token


class Company:
    # Инициализация 
    def __init__(self, url):
        self.url = url
    

    # Добавить компанию:
    def create_company(self, token: str, body: json):
        headers = {"x-client-token": token}
        resp = requests.post(self.url + '/company', headers=headers, params=body)
        return resp.json()
    

    # Последняя активная компания
    def last_active_company_id(self):
        active_params = {"active": 'true'}
        resp = requests.get(self.url + '/company', params=active_params)
        return resp.json()[-1]['id']


    def get_company(self, id):
        resp = requests.get(self.url + '/company/' + str(id))
        return resp.json()


class Employee:

    # Инициализация
    def __init__(self, url):
        self.url = url


    # Получить список сотрудников компании
    def get_employee_list(self, company_id: int):
        company = {'companyId' : company_id}
        response = requests.get(self.url + '/employee', params=company)
        return response.json()


    # Добавить нового сотрудника
    def add_new_employee(self, token: str, body: json):
        headers = {"x-client-token": token}
        # employee = {
        # "id": id, # Обязательное
        # "firstName": firstName, # Обязательное
        # "lastName": lastName, # Обязательное
        # "middleName": middleName,
        # "companyId": companyId, # Обязательное
        # "email": email,
        # "url": url,
        # "phone": phone,
        # "birthdate": birthdate,
        # "isActive": isActive # Обязательное
        # }
        resp = requests.post(self.url + '/employee', headers=headers, json=body)
        return resp.json()
    

    # Получить сотрудника по id
    def get_employee_by_id(self, employee_id: int):
        resp = requests.get(self.url + '/employee/' + str(employee_id))
        return resp
        

    # Изменить информацию о сотруднике
    def edit_employee_info(self, token: str, employee_id: int, body: json):
        headers = {"x-client-token": token}
        resp = requests.patch(self.url + '/employee/' + str(employee_id), headers=headers, json=body)
        return resp