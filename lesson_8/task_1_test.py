import json
import pytest
import requests
from Employee import Employee, Company

api = Employee('https://x-clients-be.onrender.com/')

employee = Employee('https://x-clients-be.onrender.com/')
company = Company('https://x-clients-be.onrender.com/')


def test_auth(get_token):
    token = get_token


# Проверка получения списка сотрудников компании
def test_get_employee_list():
    company_id = company.last_active_company_id()
    body = employee.get_employee_list(company_id)
    assert len(body) > 0


# Проверка добавления нового сотрудника и получения информации о сотруднике по его id
def test_add_new_employee(get_token):
    token = str(get_token)
    company_id = company.last_active_company_id()
    
    body = api.get_employee_list(1)
    len_before = len(body)

    employee_body = {
        'id': 1, # Обязательное
        'firstName': 'May', # Обязательное
        'lastName': 'Flowers', # Обязательное
        'middleName': 'Lily',
        'companyId': company_id, # Обязательное
        'email': 'mayflowers@test.com',
        'url': 'photo',
        'phone': '87654320987',
        'birthdate': '2000-01-01',
        'isActive': 'true' # Обязательное
    }
             
    new_employee_id = (employee.add_new_employee(token, employee_body))['id']
    assert new_employee_id is not None
    employee_info = employee.get_employee_by_id(new_employee_id)
    assert employee_info.json()['id'] == new_employee_id
    assert employee_info.status_code == 200



# Проверка добавления нового сотрудника без токена авторизации
def test_add_new_employee_no_token():
    token = ''
    company_id = company.last_active_company_id()
    employee_body = {
        'id': 1, # Обязательное
        'firstName': 'May', # Обязательное
        'lastName': 'Flowers', # Обязательное
        'middleName': 'Lily',
        'companyId': company_id, # Обязательное
        'email': 'mayflowers@test.com',
        'url': 'photo',
        'phone': '87654320987',
        'birthdate': '2000-01-01',
        'isActive': 'true', # Обязательное
    }
    new_employee = employee.add_new_employee(token, employee_body)
    assert new_employee['message'] == 'Unauthorized'


# Проверка добавления нового сотрудника без ключа "id"
# БАГ: СОТРУДНИК ДОБАВЛЯЕТСЯ ПРИ ОТСУТСТВИИ ОБЯЗАТЕЛЬНОГО КЛЮЧА ID

# def test_add_new_employee_no_id(get_token):
#     token = str(get_token)
#     company_id = company.last_active_company_id()
#     employee_body = {
#         'firstName': 'Jill', # Обязательное
#         'lastName': 'Flowers', # Обязательное
#         'middleName': 'Lily',
#         'companyId': company_id, # Обязательное
#         'email': 'mayflowers@test.com',
#         'url': 'photo',
#         'phone': '87654320987',
#         'birthdate': '2000-01-01',
#         'isActive': 'true', # Обязательное
#     }
#     new_employee = employee.add_new_employee(token, employee_body)
#     assert new_employee["message"] == 'Internal server error'


# Проверка добавления нового сотрудника без ключа "firstName"
def test_add_new_employee_no_firstname(get_token):
    token = str(get_token)
    company_id = company.last_active_company_id()
    employee_body = {
        'id': 2, # Обязательное
        'lastName': 'Flowers', # Обязательное
        'middleName': 'Lily',
        'companyId': company_id, # Обязательное
        'email': 'mayflowers@test.com',
        'url': 'photo',
        'phone': '87654320987',
        'birthdate': '2000-01-01',
        'isActive': 'true', # Обязательное
    }
    new_employee = employee.add_new_employee(token, employee_body)
    assert new_employee['message'] == 'Internal server error'


# Проверка добавления нового сотрудника без ключа "lastName"
def test_add_new_employee_no_lastname(get_token):
    token = str(get_token)
    company_id = company.last_active_company_id()
    employee_body = {
        'id': 3, # Обязательное
        'firstName': 'Catherine', # Обязательное
        'middleName': 'Lily',
        'companyId': company_id, # Обязательное
        'email': 'ccath@test.com',
        'url': 'photo',
        'phone': '87654320987',
        'birthdate': '2000-01-01',
        'isActive': 'true', # Обязательное
    }
    new_employee = employee.add_new_employee(token, employee_body)
    assert new_employee['message'] == 'Internal server error'


# Проверка добавления нового сотрудника без ключа "companyId"
def test_add_new_employee_no_company_id(get_token):
    token = str(get_token)
    company_id = company.last_active_company_id()
    employee_body = {
        'id': 4, # Обязательное
        'firstName': 'Lola', # Обязательное
        'lastName': 'Jackson', # Обязательное
        'middleName': 'Lily',
        'email': 'lolajackson@test.com',
        'url': 'photo',
        'phone': '87654320987',
        'birthdate': '2000-01-01',
        'isActive': 'true', # Обязательное
    }
    new_employee = employee.add_new_employee(token, employee_body)
    assert new_employee['message'] == 'Internal server error'


# Проверка добавления нового сотрудника без ключа "isActive"
# БАГ: СОТРУДНИК ДОБАВЛЯЕТСЯ ПРИ ОТСУТСТВИИ ОБЯЗАТЕЛЬНОГО КЛЮЧА, ОБОЗНАЧАЮЩЕГО СТАТУС СОТРУДНИКА

# def test_add_new_employee_no_status(get_token):
#     token = str(get_token)
#     company_id = company.last_active_company_id()
#     employee_body = {
#         'id': 5, # Обязательное
#         'firstName': 'Catherine', # Обязательное
#         'lastName': 'Jackson', # Обязательное
#         'middleName': 'Lily',
#         'companyId': company_id, # Обязательное
#         'email': 'cjack@test.com',
#         'url': 'photo',
#         'phone': '87654320987',
#         'birthdate': '2000-01-01',
#     }
#     new_employee = employee.add_new_employee(token, employee_body)
#     assert new_employee['message'] == 'Internal server error'


def test_edit_employee_info(get_token):
    token = str(get_token)
    company_id = company.last_active_company_id()
    employee_body = {
        'id': 6, # Обязательное
        'firstName': 'Sarah', # Обязательное
        'lastName': 'Woods', # Обязательное
        'middleName': 'Florence',
        'companyId': company_id, # Обязательное
        'email': 'swoods@test.com',
        'url': 'photo',
        'phone': '87654320987',
        'birthdate': '2000-01-01',
        'isActive': 'true', # Обязательное
    }

    added_employee = employee.add_new_employee(token, employee_body)
    added_employee_id = added_employee['id']


    edited_employee_body = {
        'isActive': 'false',
        'email': 'sarahflowoods@test.com',
        'url': 'differentPhoto',
    }

    edited_employee = employee.edit_employee_info(token, added_employee_id, edited_employee_body)
    # Проверка на ствтус кода
    assert edited_employee.status_code == 200
    # Проверка фактическое изменение данных
    assert (edited_employee.json()["isActive"]) == edited_employee_body.get("isActive")
    assert (edited_employee.json()['email']) == edited_employee_body.get('email')
    assert (edited_employee.json()['url']) == edited_employee_body.get('url')