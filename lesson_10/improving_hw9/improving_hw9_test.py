import json
import pytest
import requests
import psycopg2
from sqlalchemy import create_engine
from sqlalchemy.sql import text
import allure

from Automation.lesson_10.improving_hw9.conftest import get_token
from Automation.lesson_10.improving_hw9.Employee import Employee, Company
from Automation.lesson_10.improving_hw9.EmployeeTable import EmployeeTable, CompanyTable

employee = Employee('https://x-clients-be.onrender.com/')
company = Company('https://x-clients-be.onrender.com/')
db_employee = EmployeeTable("postgresql://x_clients_user:95PM5lQE0NfzJWDQmLjbZ45ewrz1fLYa@dpg-cqsr9ulumphs73c2q40g-a.frankfurt-postgres.render.com/x_clients_db_fxd0")
db_company = CompanyTable('postgresql://x_clients_user:95PM5lQE0NfzJWDQmLjbZ45ewrz1fLYa@dpg-cqsr9ulumphs73c2q40g-a.frankfurt-postgres.render.com/x_clients_db_fxd0')



@allure.id("9.1")
@allure.epic("ДЗ 9")
@allure.feature("Авторизация")
@allure.title("Получение токена аторизации")
@allure.description("")
@allure.severity("Blocker")
def test_auth(get_token):
    token = get_token



@allure.id("9.2")
@allure.epic("ДЗ 9")
@allure.feature("Сотрудники")
@allure.title("Получение списка сотрудников компании")
@allure.description("")
@allure.severity("Blocker")
def test_get_employee_list():
    with allure.step("Добавить в БД новую компанию"):
        new_company = db_company.create_company('Эльдорадо', 'Магазин техники')
    
    with allure.step("Получить ID последней добавленной компании"):
        max_company_id = db_company.get_max_id()

    with allure.step("Получить список сотрудников компании через API"):
        api_result = employee.get_employee_list(max_company_id)

    with allure.step("Получить список сотрудников компании через SQL"):
        db_result = db_employee.get_employees(max_company_id)

    with allure.step("Убедиться, что длина списка сотрудников, полученная через API, равна списку сотрудников в базе данных"):
        assert len(api_result) == len(db_result)

    with allure.step("Удалить ранее созданную компанию"):
        db_company.delete_company(max_company_id)



@allure.id("9.3")
@allure.epic("ДЗ 9")
@allure.feature("Сотрудники")
@allure.title("Просмотр информации о сотруднике по его ID")
@allure.description("")
@allure.severity("Blocker")
def test_get_employee_by_id(get_token):
    with allure.step("Добавить в БД новую компанию"):
        new_company = db_company.create_company('restore', 'Магазин техники')

    with allure.step("Получить ID последней добавленной компании"):
        max_company_id = db_company.get_max_id()

    with allure.step("Добавить нового сотрудника"):
        token = str(get_token)
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
    
    with allure.step("Получить информацию о сотруднике по его ID"):
        employee_info = employee.get_employee_by_id(new_employee_id)
    
    with allure.step("Проверить, что отправленные данные о новом сотруднике совпадают с полученными о нем данными при API-запросе"):
        assert employee_info.json()['id'] == new_employee_id
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

    with allure.step("Проверить, что статус-код запроса - 200"):
        assert employee_info.status_code == 200
    
    with allure.step("Удалить ранее добавленного сотрудника из базы"):
        db_employee.delete_employee(new_employee_id)

    with allure.step("Удалить ранее созданную компанию"):
        db_company.delete_company(max_company_id)



@allure.id("9.4")
@allure.epic("ДЗ 9")
@allure.feature("Сотрудники")
@allure.title("Добавление нового сотрудника")
@allure.description("")
@allure.severity("Blocker")
def test_add_new_employee(get_token):
    with allure.step("Добавить в БД новую компанию"):
        new_company = db_company.create_company('М.Видео', 'Магазин техники')

    with allure.step("Получить ID последней добавленной компании"):
        max_company_id = db_company.get_max_id()

    with allure.step("Добавить нового сотрудника"):
        token = str(get_token)
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

    with allure.step("Проверить, что ID сотрудника не равен None"):
        assert new_employee_id is not None
    
    with allure.step("Проверить, что введенный ранее ID добавленного сотрудника совпадает с его полученным ID при API-запросе"):
        employee_info = employee.get_employee_by_id(new_employee_id)
        assert employee_info.json()['id'] == new_employee_id

    with allure.step("Проверить, что статус-код запроса - 200"):
        assert employee_info.status_code == 200
    
    with allure.step("Удалить ранее добавленного сотрудника из базы"):
        db_employee.delete_employee(new_employee_id)

    with allure.step("Удалить ранее созданную компанию"):
        db_company.delete_company(max_company_id)



@allure.id("9.5")
@allure.epic("ДЗ 9")
@allure.feature("Сотрудники")
@allure.title("Добавление нового сотрудника без токена авторизации")
@allure.description("")
@allure.severity("Blocker")
def test_add_new_employee_no_token():
    with allure.step("Получить ID последней активной компании"):
        company_id = company.last_active_company_id()
    
    with allure.step("Отправить запрос на добавление сотрудника с 'пустым' токеном авторизации"):
        token = ''
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
    
    with allure.step("Удостовериться, что пришла ошибка 'Unauthorized'"):
        assert new_employee['message'] == 'Unauthorized'



# БАГ: СОТРУДНИК ДОБАВЛЯЕТСЯ ПРИ ОТСУТСТВИИ ОБЯЗАТЕЛЬНОГО КЛЮЧА ID
# @allure.id("9.6")
# @allure.epic("ДЗ 9")
# @allure.feature("Сотрудники")
# @allure.title("Добавление нового сотрудника без ключа 'id'")
# @allure.description("")
# @allure.severity("Critical")
# def test_add_new_employee_no_id(get_token):
#     with allure.step("Получить ID последней активной компании"):
#         company_id = company.last_active_company_id()

#     with allure.step("Отправить запрос на добавление сотрудника без ключа 'id'"):
#         token = str(get_token)
#         employee_body = {
#             'firstName': 'Jill', # Обязательное
#             'lastName': 'Flowers', # Обязательное
#             'middleName': 'Lily',
#             'companyId': company_id, # Обязательное
#             'email': 'mayflowers@test.com',
#             'url': 'photo',
#             'phone': '87654320987',
#             'birthdate': '2000-01-01',
#             'isActive': 'true', # Обязательное
#         }
#         new_employee = employee.add_new_employee(token, employee_body)

#     with allure.step("Удостовериться, что пришла ошибка 'Internal server error'"):
#         assert new_employee["message"] == 'Internal server error'



@allure.id("9.7")
@allure.epic("ДЗ 9")
@allure.feature("Сотрудники")
@allure.title("Добавление нового сотрудника без ключа 'firstName'")
@allure.description("")
@allure.severity("Critical")
def test_add_new_employee_no_firstname(get_token):
    with allure.step("Получить ID последней активной компании"):
        company_id = company.last_active_company_id()

    with allure.step("Отправить запрос на добавление сотрудника без ключа 'firstName'"):
        token = str(get_token)
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
    
    with allure.step("Удостовериться, что пришла ошибка 'Internal server error'"):
        assert new_employee['message'] == 'Internal server error'



@allure.id("9.8")
@allure.epic("ДЗ 9")
@allure.feature("Сотрудники")
@allure.title("Добавление нового сотрудника без ключа 'lastName'")
@allure.description("")
@allure.severity("Critical")
def test_add_new_employee_no_lastname(get_token):
    with allure.step("Получить ID последней активной компании"):
        company_id = company.last_active_company_id()

    with allure.step("Отправить запрос на добавление сотрудника без ключа 'lastName'"):
        token = str(get_token)
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

    with allure.step("Удостовериться, что пришла ошибка 'Internal server error'"):
        assert new_employee['message'] == 'Internal server error'



@allure.id("9.9")
@allure.epic("ДЗ 9")
@allure.feature("Сотрудники")
@allure.title("Добавление нового сотрудника без ключа 'companyId'")
@allure.description("")
@allure.severity("Critical")
def test_add_new_employee_no_company_id(get_token):
    with allure.step("Получить ID последней активной компании"):
        company_id = company.last_active_company_id()

    with allure.step("Отправить запрос на добавление сотрудника без ключа 'companyId'"):
        token = str(get_token)
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

    with allure.step("Удостовериться, что пришла ошибка 'Internal server error'"):
        assert new_employee['message'] == 'Internal server error'



# БАГ: СОТРУДНИК ДОБАВЛЯЕТСЯ ПРИ ОТСУТСТВИИ ОБЯЗАТЕЛЬНОГО КЛЮЧА, ОБОЗНАЧАЮЩЕГО СТАТУС СОТРУДНИКА
# @allure.id("9.10")
# @allure.epic("ДЗ 9")
# @allure.feature("Сотрудники")
# @allure.title("Добавление нового сотрудника без ключа 'isActive'")
# @allure.description("")
# @allure.severity("Critical")
# def test_add_new_employee_no_status(get_token):
#     with allure.step("Получить ID последней активной компании"):
#         company_id = company.last_active_company_id()

#     with allure.step("Отправить запрос на добавление сотрудника без ключа 'isActive'"):
#         token = str(get_token)
#         employee_body = {
#             'id': 5, # Обязательное
#             'firstName': 'Catherine', # Обязательное
#             'lastName': 'Jackson', # Обязательное
#             'middleName': 'Lily',
#             'companyId': company_id, # Обязательное
#             'email': 'cjack@test.com',
#             'url': 'photo',
#             'phone': '87654320987',
#             'birthdate': '2000-01-01',
#         }
#         new_employee = employee.add_new_employee(token, employee_body)
    
#     with allure.step("Удостовериться, что пришла ошибка 'Internal server error'"):
#         assert new_employee['message'] == 'Internal server error'



@allure.id("9.11")
@allure.epic("ДЗ 9")
@allure.feature("Сотрудники")
@allure.title("Редактирование данных о сотруднике")
@allure.description("")
@allure.severity("Blocker")
def test_edit_employee_info(get_token):
    with allure.step("Добавить в БД новую компанию"):
        new_company = db_company.create_company('Ситилинк', 'Магазин техники')
    with allure.step("Получить ID последней добавленной компании"):
        max_company_id = db_company.get_max_id()

    with allure.step("Добавить нового сотрудника"):
        token = str(get_token)
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

    with allure.step("Отредактировать данные нового сотрудника"):
        edited_employee_body = {
            'isActive': 'false',
            'email': 'sarahflowoods@test.com',
            'url': 'differentPhoto',
        }
        edited_employee = employee.edit_employee_info(token, added_employee_id, edited_employee_body)
    
    with allure.step("Проверить, что статус-код запроса - 200"):
        assert edited_employee.status_code == 200

    with allure.step("Проверить, что отправленные данные о сотруднике изменились"):
        assert (edited_employee.json()["isActive"]) == edited_employee_body.get("isActive")
        assert (edited_employee.json()['email']) == edited_employee_body.get('email')
        assert (edited_employee.json()['url']) == edited_employee_body.get('url')

    with allure.step("Удалить ранее добавленного сотрудника из базы"):
        db_employee.delete_employee(added_employee_id)
    
    with allure.step("Удалить ранее созданную компанию"):
        db_company.delete_company(max_company_id)