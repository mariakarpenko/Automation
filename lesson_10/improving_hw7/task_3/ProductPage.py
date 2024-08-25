from selenium.webdriver.common.by import By
import allure

class ProductPage:

    def __init__(self, browser: str):
        """
        Функция-конструктор, создает экзмпляр класса
        """
        self._driver = browser

    @allure.step("Добавить три определенных товара в корзину")
    def adding_products(self):
        """
        Функция добавляет товар в корзину
        """        
        self._driver.find_element(By.CSS_SELECTOR, '#add-to-cart-sauce-labs-backpack').click()
        self._driver.find_element(By.CSS_SELECTOR, '#add-to-cart-sauce-labs-bolt-t-shirt').click()
        self._driver.find_element(By.CSS_SELECTOR, '#add-to-cart-sauce-labs-onesie').click()

    @allure.step("Нажать на иконку корзины в правлм левом углу")
    def to_cart(self):
        """
        Функция нажимает на иконку корзины
        """
        self._driver.find_element(By.CSS_SELECTOR, 'a.shopping_cart_link').click()

        