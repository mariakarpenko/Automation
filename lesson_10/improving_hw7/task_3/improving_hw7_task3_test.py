from time import sleep
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import allure

from Automation.lesson_10.improving_hw7.task_3 import AuthPage
from Automation.lesson_10.improving_hw7.task_3 import ProductPage
from Automation.lesson_10.improving_hw7.task_3 import CartPage

@allure.id("HW7.3")
@allure.epic("ДЗ 7.3")
@allure.feature("Добавление товаров в корзину")
@allure.title("Добавление товаров в корзину, и чекаут")
@allure.description("Автотест на добавление определенных товаров в корзину, переход в корзину и проверка на корректность итоговой суммы заказа")
@allure.severity("Critical")
def testing_step_three():
    # Создаем экземпляр драйвера Chrome
    browser = webdriver.Chrome(service = ChromeService(ChromeDriverManager().install()))

    with allure.step("Перейти на страницу авторизации в браузере Google Chrome"):
        auth_page = AuthPage(browser)

    with allure.step("Ввести логин, пароль и нажать на кнопку 'Submit'"):
        auth_page.login()

    with allure.step("Перейти на страницу с каталогом товаров"):
        product_page = ProductPage(browser)
    
    with allure.step("Добавить три определенных товара в корзину"):
        product_page.adding_products()

    with allure.step("Нажать на иконку корзины в правом верхнем углу страницы и перейти в корзину"):
        product_page.to_cart()
        cart_page = CartPage(browser)

    with allure.step("Нажать на кнопку 'Checkout'"):
        cart_page.checkout()

    with allure.step("Ввести данные в поля 'First Name', 'Last Name', 'Zip/Posatl Code'"):
        cart_page.filling_personal_data_form('Maria', 'Karpenko', '777777')

    with allure.step("Нажать на кнопку 'Continue'"):
        cart_page.press_continue()

    with allure.step("Проверить, что итоговая сумма равна $58.29"):
        total_price_inscription = browser.find_element(By.CSS_SELECTOR, '.summary_total_label')
        total = total_price_inscription.text.strip().replace("Total: $", "")
        assert total == '58.29'

    with allure.step("Закрыть браузер"):
        browser.quit()