from selenium.webdriver.common.by import By

class CartPage:

    def __init__(self, browser):
        self._driver = browser

    def checkout(self):
        self._driver.find_element(By.CSS_SELECTOR, '#checkout').click()

    def filling_personal_data_form(self, first_name, last_name, zip_code):
        self._driver.find_element(By.CSS_SELECTOR, '#first-name').send_keys(first_name)
        self._driver.find_element(By.CSS_SELECTOR, '#last-name').send_keys(last_name)
        self._driver.find_element(By.CSS_SELECTOR, '#postal-code').send_keys(zip_code)

    def press_continue(self):
        self._driver.find_element(By.CSS_SELECTOR, '#continue').click()