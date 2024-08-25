from time import sleep
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

from task_2_MainPage import MainPage


def testing_step_two():
    # Создаем экземпляр драйвера Chrome
    browser = webdriver.Chrome(service = ChromeService(ChromeDriverManager().install()))

    main_page = MainPage(browser)
    main_page.delay_setting(45)
    main_page.clicking_buttons()
    main_page.waiting_for_result(46)

    # Проверяем, что в окне отобразится результат '15' через 45 секунд
    result_txt = browser.find_element(By.CSS_SELECTOR, 'div.screen').text
    assert result_txt == '15'

    # Закрываем браузер
    browser.quit()