from selenium.webdriver.common.by import By

class ProductPage:

    def __init__(self, browser):
        self._driver = browser

    def adding_products(self):
        self._driver.find_element(By.CSS_SELECTOR, '#add-to-cart-sauce-labs-backpack').click()
        self._driver.find_element(By.CSS_SELECTOR, '#add-to-cart-sauce-labs-bolt-t-shirt').click()
        self._driver.find_element(By.CSS_SELECTOR, '#add-to-cart-sauce-labs-onesie').click()

    def to_cart(self):
        self._driver.find_element(By.CSS_SELECTOR, 'a.shopping_cart_link').click()

        