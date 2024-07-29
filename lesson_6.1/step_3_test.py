from time import sleep
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

def testing_step_three():
    # Создаем экземпляр драйвера Chrome
    driver = webdriver.Chrome(service = ChromeService(ChromeDriverManager().install()))

    # Максимизируем окно браузера
    driver.maximize_window() 

    # Открываем страницу
    driver.get('https://www.saucedemo.com/')

    # Добавляем неявное ожидание на всякий случай
    driver.implicitly_wait(4)

    # Авторизация вводом логина, пароля и нажатием на кнопку «Login»
    driver.find_element(By.CSS_SELECTOR, 'input#user-name').send_keys('standard_user')
    driver.find_element(By.CSS_SELECTOR, 'input#password').send_keys('secret_sauce')
    driver.find_element(By.CSS_SELECTOR, 'input#login-button').click()

    # Добавляем в корзину товары (нажимаем на кнопки «В корзину» у соответствующих товаров)
    driver.find_element(By.CSS_SELECTOR, '#add-to-cart-sauce-labs-backpack').click()
    driver.find_element(By.CSS_SELECTOR, '#add-to-cart-sauce-labs-bolt-t-shirt').click()
    driver.find_element(By.CSS_SELECTOR, '#add-to-cart-sauce-labs-onesie').click()

    # Переходим в корзину (Нажимаем на кнопку «В корзину»)
    driver.find_element(By.CSS_SELECTOR, 'a.shopping_cart_link').click()

    # Нажимаем ‘Checkout’
    driver.find_element(By.CSS_SELECTOR, '#checkout').click()

    # Заполняем форму своими данными: имя, фамилия, почтовый индекс
    driver.find_element(By.CSS_SELECTOR, '#first-name').send_keys('Maria')
    driver.find_element(By.CSS_SELECTOR, '#last-name').send_keys('Karpenko')
    driver.find_element(By.CSS_SELECTOR, '#postal-code').send_keys('777777')

    # Нажимаем на кнопку ‘Continue’
    driver.find_element(By.CSS_SELECTOR, '#continue').click()

    # Проверяем, что итоговая сумма равна $58.29.
    total_price_inscription = driver.find_element(By.CSS_SELECTOR, '.summary_total_label')
    total = total_price_inscription.text.strip().replace("Total: $", "")
    assert total == '58.29'

    # Закрываем браузер
    driver.quit()