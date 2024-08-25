from time import sleep
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import allure

from HomePage_task2 import HomePage

@allure.id("HW7.2")
@allure.epic("ДЗ 7.2")
@allure.feature("Медленный калькулятор")
@allure.title("Вычисление на калькуляторе с задаваемой задержкой")
@allure.description("Проверка корректности выдаваемого калькулятором результата через заданное количество секунд")
@allure.severity("Critical")
def testing_step_two():
    # Создаем экземпляр драйвера Chrome
    browser = webdriver.Chrome(service = ChromeService(ChromeDriverManager().install()))

    with allure.step("Перейти на веб-страницу в браузере Google Chrome"):
        main_page = HomePage(browser)

    with allure.step("Ввести количество секунд, через которое в калькуляторе отобразится результат вычисления"):
        main_page.delay_setting(45)
    
    with allure.step("Нажать на кнопки операторов и операнд (7 + 8 =)"):
        main_page.clicking_buttons()

    with allure.step("Подождать появления результата необходимое количество секунд"):        
        main_page.waiting_for_result(46)

    with allure.step("Убедится, что результат выражения равен 15"):
        result_txt = browser.find_element(By.CSS_SELECTOR, 'div.screen').text
        assert result_txt == '15'

    with allure.step("Закрыть браузер"):
        browser.quit()