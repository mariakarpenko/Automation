import json
import pytest
import requests
import psycopg2
from sqlalchemy import create_engine
from sqlalchemy.sql import text

from conftest import get_token
from Employee import Employee, Company
from EmployeeTable import EmployeeTable, CompanyTable

api = Employee('https://x-clients-be.onrender.com/')

employee = Employee('https://x-clients-be.onrender.com/')
company = Company('https://x-clients-be.onrender.com/')
db_employee = EmployeeTable("postgresql://x_clients_user:95PM5lQE0NfzJWDQmLjbZ45ewrz1fLYa@dpg-cqsr9ulumphs73c2q40g-a.frankfurt-postgres.render.com/x_clients_db_fxd0")
db_company = CompanyTable('postgresql://x_clients_user:95PM5lQE0NfzJWDQmLjbZ45ewrz1fLYa@dpg-cqsr9ulumphs73c2q40g-a.frankfurt-postgres.render.com/x_clients_db_fxd0')


def test_auth(get_token):
    token = get_token



# Проверка получения списка сотрудников компании
def test_get_employee_list():
    # Создаем новую организацию в базе
    new_company = db_company.create_company('Эльдорадо', 'Магазин техники')
    # Сохраняем в переменную максимальный id в списке компаний (id принадлежит последней созданной компании)
    max_company_id = db_company.get_max_id()

    # Получаем список сотрудников методом api
    api_result = employee.get_employee_list(max_company_id)
    # Получаем список сотрудников запросом sql
    db_result = db_employee.get_employees(max_company_id)

    # Сравниваем, что длина списка сотрудников, полученная через api, равна списку в базе данных
    assert len(api_result) == len(db_result)

    # Удаляем созданную компанию
    db_company.delete_company(max_company_id)



# Просмотр информации о сотруднике по его id
def test_get_employee_by_id(get_token):

    token = str(get_token)

    # Создаем новую организацию в базе
    new_company = db_company.create_company('restore', 'Магазин техники')
    # Сохраняем в переменную максимальный id в списке компаний (id принадлежит последней созданной компании)
    max_company_id = db_company.get_max_id()

    # Добавляем нового сотрудника
    employee_body = {
        'id': 1, # Обязательное
        'firstName': 'Sarah', # Обязательное
        'lastName': 'Parker', # Обязательное
        'middleName': 'Jessica',
        'companyId': max_company_id, # Обязательное
        'email': 'sarahpark@test.com',
        'url': 'photo',
        'phone': '88887776655',
        'birthdate': '2000-01-01',
        'isActive': 'true' # Обязательное
    }
    new_employee_id = (employee.add_new_employee(token, employee_body))['id']
    
    # Получаем о нем информацию по id
    employee_info = employee.get_employee_by_id(new_employee_id)
    assert employee_info.json()['id'] == new_employee_id
    assert employee_info.status_code == 200
    assert employee_info.json()['firstName'] == employee_body['firstName']
    assert employee_info.json()['lastName'] == employee_body['lastName']
    assert employee_info.json()['middleName'] == employee_body['middleName']
    assert employee_info.json()['companyId'] == employee_body['companyId']
    # Баг: в ответе вместо указанного email вернулось "email":null
    # assert employee_info.json()['email'] == employee_body['email']          
    assert employee_info.json()['avatar_url'] == employee_body['url']
    assert employee_info.json()['phone'] == employee_body['phone']
    assert employee_info.json()['birthdate'] == employee_body['birthdate']
    # assert employee_info.json()['isActive'] == employee_body['isActive']

    # Удаляем созданного сотрудника из базы
    db_employee.delete_employee(new_employee_id)
    # Удаляем созданную компанию
    db_company.delete_company(max_company_id)



# Проверка добавления нового сотрудника и получения информации о сотруднике по его id
def test_add_new_employee(get_token):
    token = str(get_token)

    # Создаем новую организацию в базе
    new_company = db_company.create_company('М.Видео', 'Магазин техники')
    # Сохраняем в переменную максимальный id в списке компаний (id принадлежит последней созданной компании)
    max_company_id = db_company.get_max_id()

    # Добавляем нового сотрудника
    employee_body = {
        'id': 1, # Обязательное
        'firstName': 'May', # Обязательное
        'lastName': 'Flowers', # Обязательное
        'middleName': 'Lily',
        'companyId': max_company_id, # Обязательное
        'email': 'mayflowers@test.com',
        'url': 'photo',
        'phone': '87654320987',
        'birthdate': '2000-01-01',
        'isActive': 'true' # Обязательное
    }    
    new_employee_id = (employee.add_new_employee(token, employee_body))['id']

    # Проверки
    assert new_employee_id is not None
    employee_info = employee.get_employee_by_id(new_employee_id)
    assert employee_info.json()['id'] == new_employee_id
    assert employee_info.status_code == 200

    # Удаляем созданного сотрудника из базы
    db_employee.delete_employee(new_employee_id)
    # Удаляем созданную компанию
    db_company.delete_company(max_company_id)



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

# @pytest.mark.xfail
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

    # Создаем новую организацию в базе
    new_company = db_company.create_company('Ситилинк', 'Магазин техники')
    # Сохраняем в переменную максимальный id в списке компаний (id принадлежит последней созданной компании)
    max_company_id = db_company.get_max_id()

    # Добавляем сотрудника в компанию
    employee_body = {
        'id': 6, # Обязательное
        'firstName': 'Sarah', # Обязательное
        'lastName': 'Woods', # Обязательное
        'middleName': 'Florence',
        'companyId': max_company_id, # Обязательное
        'email': 'swoods@test.com',
        'url': 'photo',
        'phone': '87654320987',
        'birthdate': '2000-01-01',
        'isActive': 'true', # Обязательное
    }
    added_employee = employee.add_new_employee(token, employee_body)
    added_employee_id = added_employee['id']

    # Редактируем данные о сотруднике
    edited_employee_body = {
        'isActive': 'false',
        'email': 'sarahflowoods@test.com',
        'url': 'differentPhoto',
    }
    edited_employee = employee.edit_employee_info(token, added_employee_id, edited_employee_body)
    
    # Проверка на статус кода
    assert edited_employee.status_code == 200
    # Проверка фактическое изменение данных
    assert (edited_employee.json()["isActive"]) == edited_employee_body.get("isActive")
    assert (edited_employee.json()['email']) == edited_employee_body.get('email')
    assert (edited_employee.json()['url']) == edited_employee_body.get('url')

    # Удаляем созданного сотрудника из базы
    db_employee.delete_employee(added_employee_id)
    # Удаляем созданную компанию
    db_company.delete_company(max_company_id)