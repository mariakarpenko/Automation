from selenium.webdriver.common.by import By

class AuthPage:

    def __init__(self, browser):
        self._driver = browser
        self._driver.get('https://www.saucedemo.com/')
        self._driver.implicitly_wait(4)
        self._driver.maximize_window()

    def login(self):
        self._driver.find_element(By.CSS_SELECTOR, 'input#user-name').send_keys('standard_user')
        self._driver.find_element(By.CSS_SELECTOR, 'input#password').send_keys('secret_sauce')
        self._driver.find_element(By.CSS_SELECTOR, 'input#login-button').click()