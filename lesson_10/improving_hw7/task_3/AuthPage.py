from selenium.webdriver.common.by import By
import allure

class AuthPage:

    def __init__(self, browser: str):
        """
        Функция-конструктор, создает экзмпляр класса
        """
        self._driver = browser
        self._driver.get('https://www.saucedemo.com/')
        self._driver.implicitly_wait(4)
        self._driver.maximize_window()

    @allure.step("Авторизоваться (ввести логин, пароль и нажать на кнопку 'Login')")
    def login(self):
        """
        Функция авторизуется (вводит логин, пароль и наживает на кнопку "Login")
        """
        self._driver.find_element(By.CSS_SELECTOR, 'input#user-name').send_keys('standard_user')
        self._driver.find_element(By.CSS_SELECTOR, 'input#password').send_keys('secret_sauce')
        self._driver.find_element(By.CSS_SELECTOR, 'input#login-button').click()