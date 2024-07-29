from time import sleep
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

from task_3_AuthPage import AuthPage
from task_3_ProductPage import ProductPage
from task_3_CartPage import CartPage

def testing_step_three():
    # Создаем экземпляр драйвера Chrome
    browser = webdriver.Chrome(service = ChromeService(ChromeDriverManager().install()))

    auth_page = AuthPage(browser)
    auth_page.login()

    product_page = ProductPage(browser)
    product_page.adding_products()
    product_page.to_cart()

    cart_page = CartPage(browser)
    cart_page.checkout()
    cart_page.filling_personal_data_form('Maria', 'Karpenko', '777777')
    cart_page.press_continue()

    # Проверяем, что итоговая сумма равна $58.29.
    total_price_inscription = browser.find_element(By.CSS_SELECTOR, '.summary_total_label')
    total = total_price_inscription.text.strip().replace("Total: $", "")
    assert total == '58.29'

    # Закрываем браузер
    browser.quit()