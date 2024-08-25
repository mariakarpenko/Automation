import pytest
import requests
import json
import allure
from Automation.lesson_10.improving_hw9.conftest import get_token


class Company:

    def __init__(self, url: str):
        """
        Функция-конструктор, создает экземпляр класса
        """        
        self.url = url
    

    @allure.step("API. Добавить новую компанию")
    def create_company(self, token: str, body: json):
        """
        Функция добавляет новую компанию с помощью api-запроса, в параметрах указываются 
        название и описание создаваемой компании
        """
        headers = {"x-client-token": token}
        resp = requests.post(self.url + '/company', headers=headers, json=body)
        return resp.json()
    

    @allure.step("API. Получить ID последней активной компании")
    def last_active_company_id(self) -> int:
        """
        Функция получает id последней активной компании
        """        
        active_params = {"active": 'true'}
        resp = requests.get(self.url + '/company', params=active_params)
        return resp.json()[-1]['id']


    @allure.step("API. Получить данные по компании по ее ID ({id})")
    def get_company(self, id: int):
        """
        Функция получает информацию об определенной компании по её id (указывается как параметр))
        """           
        resp = requests.get(self.url + '/company/' + str(id))
        return resp.json()


class Employee:

    def __init__(self, url: str):
        """
        Функция-конструктор, создает экземпляр класса
        """        
        self.url = url


    @allure.step("API. Получить список сотрудников компании с ID ({company_id})")
    def get_employee_list(self, company_id: int) -> list:
        """
        Функция получает список сотрудников определенной компании (её id указывается как параметр)
        с помощью api-запроса
        """               
        company_id_param = {'company' : company_id}
        response = requests.get(self.url + '/employee', params=company_id_param)
        return response.json()


    @allure.step("API. Добавить нового сотрудника")
    def add_new_employee(self, token: str, body: json):
        """
        Функция добавляет нового сотрудника с помощью api-запроса, в параметрах указывается токен авторизации
        и тело запроса с информацией о сотруднике в формате json
        """    
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
    

    @allure.step("API. Получить данные о сотруднике по его ID ({employee_id})")
    def get_employee_by_id(self, employee_id: int):
        """
        Функция получает информацию об определенном сотруднике по его id 
        с помощью api-запроса
        """           
        resp = requests.get(self.url + '/employee/' + str(employee_id))
        return resp
        

    @allure.step("API. Изменить данные о сотруднике. ID сотрудника: {employee_id}")
    def edit_employee_info(self, token: str, employee_id: int, body: json):
        """
        Функция изменяет информацию об определенном сотруднике 
        с помощью api-запроса, в параметрах указывается токен авторизации,
        id сотрудника и тело запроса с новой информацией о сотруднике в формате json
        """             
        headers = {"x-client-token": token}
        resp = requests.patch(self.url + '/employee/' + str(employee_id), headers=headers, json=body)
        return resp