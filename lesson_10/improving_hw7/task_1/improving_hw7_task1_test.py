import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import allure

from MainPage_task1 import MainPage

@allure.id("HW7.1")
@allure.epic("ДЗ 7.1")
@allure.feature("Форма")
@allure.title("Заполнение формы данными")
@allure.description("Автотест на заполнение формы данными и ее потдверждение")
@allure.severity("Critical")
def testing_step_one():
    # Создаем экземпляр драйвера Chrome
    browser = webdriver.Chrome(service = ChromeService(ChromeDriverManager().install()))
    
    with allure.step("Перейти на веб-страницу в браузере Google Chrome"):
        main_page = MainPage(browser)
    
    with allure.step("Заполнить все поля в форме данными, поле 'Zip Code' оставить незаполненным"):
        main_page.filling_form()
    
    with allure.step("Нажать на кнопку 'Submit'"):
        main_page.submit_form()

    with allure.step("Проверить, что поле 'Zip code' подсвечено красным"):
        zip_code_color_attribute = browser.find_element(By.CSS_SELECTOR, '#zip-code').value_of_css_property('background-color')
        assert zip_code_color_attribute == 'rgba(248, 215, 218, 1)'

    with allure.step("Проверить, что остальные поля подсвечены зеленым"):
        first_name_color_attribute = browser.find_element(By.CSS_SELECTOR, '#first-name').value_of_css_property('background-color')
        assert first_name_color_attribute == 'rgba(209, 231, 221, 1)'

        last_name_color_attribute = browser.find_element(By.CSS_SELECTOR, '#last-name').value_of_css_property('background-color')
        assert last_name_color_attribute == 'rgba(209, 231, 221, 1)'

        address_color_attribute = browser.find_element(By.CSS_SELECTOR, '#address').value_of_css_property('background-color')
        assert address_color_attribute == 'rgba(209, 231, 221, 1)'

        city_color_attribute = browser.find_element(By.CSS_SELECTOR, '#city').value_of_css_property('background-color')
        assert city_color_attribute == 'rgba(209, 231, 221, 1)'

        country_color_attribute = browser.find_element(By.CSS_SELECTOR, '#country').value_of_css_property('background-color')
        assert country_color_attribute == 'rgba(209, 231, 221, 1)'

        e_mail_color_attribute = browser.find_element(By.CSS_SELECTOR, '#e-mail').value_of_css_property('background-color')
        assert e_mail_color_attribute == 'rgba(209, 231, 221, 1)'

        phone_number_color_attribute = browser.find_element(By.CSS_SELECTOR, '#phone').value_of_css_property('background-color')
        assert phone_number_color_attribute == 'rgba(209, 231, 221, 1)'

        job_position_color_attribute = browser.find_element(By.CSS_SELECTOR, '#job-position').value_of_css_property('background-color')
        assert job_position_color_attribute == 'rgba(209, 231, 221, 1)'

        company_color_attribute = browser.find_element(By.CSS_SELECTOR, '#company').value_of_css_property('background-color')
        assert company_color_attribute == 'rgba(209, 231, 221, 1)'
 
    with allure.step("Закрыть браузер"):
        browser.quit()