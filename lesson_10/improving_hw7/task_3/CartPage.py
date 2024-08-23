from selenium.webdriver.common.by import By
import allure

class CartPage:

    def __init__(self, browser: str):
        """
        Функция-конструктор, создает экзмпляр класса
        """
        self._driver = browser

    @allure.step("Нажать на кнопку 'Checkout'")
    def checkout(self):
        """
        Функция нажимает на кнопку "Checkout"
        """        
        self._driver.find_element(By.CSS_SELECTOR, '#checkout').click()

    @allure.step("Ввести данные в поля 'First Name': {first_name}, 'Last Name': {last_name}, 'Zip/Posatl Code': {zip_code}")
    def filling_personal_data_form(self, first_name: str, last_name: str, zip_code: str):
        """
        Функция вводит данные в поля "First Name", "Last Name", "Zip/Posatl Code"
        Вводимые данные указываются в параметрах
        """                
        self._driver.find_element(By.CSS_SELECTOR, '#first-name').send_keys(first_name)
        self._driver.find_element(By.CSS_SELECTOR, '#last-name').send_keys(last_name)
        self._driver.find_element(By.CSS_SELECTOR, '#postal-code').send_keys(zip_code)

    @allure.step("Нажать на кнопку 'Contunue'")
    def press_continue(self):
        """
        Функция нажимает на кнопку "Contunue"
        """        
        self._driver.find_element(By.CSS_SELECTOR, '#continue').click()