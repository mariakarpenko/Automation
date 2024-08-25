from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure

class HomePage:
    
    def __init__(self, browser):
        self._driver = browser
        self._driver.get('https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html')
        self._driver.implicitly_wait(4)
        self._driver.maximize_window()

    @allure.step("Очистить и заполнить поле для указания времени ожидания: {sec} секунд(ы)")
    def delay_setting(self, sec: int):
        self._driver.find_element(By.CSS_SELECTOR, '#delay').clear()
        self._driver.find_element(By.CSS_SELECTOR, '#delay').send_keys(sec)

    @allure.step("Нажать на кнопки нужных операторов и операнд")
    def clicking_buttons(self):
        # 7
        self._driver.find_element(By.XPATH, '//*[@id="calculator"]/div[2]/span[1]').click()
        # +
        self._driver.find_element(By.XPATH, '//*[@id="calculator"]/div[2]/span[4]').click()
        # 8
        self._driver.find_element(By.XPATH, '//*[@id="calculator"]/div[2]/span[2]').click()
        # =
        self._driver.find_element(By.XPATH, '//*[@id="calculator"]/div[2]/span[15]').click()

    @allure.step("Подождать {sec} секунд(ы)")
    def waiting_for_result(self, sec: int):
        WebDriverWait(self._driver, sec).until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, 'div.screen'), '15'))