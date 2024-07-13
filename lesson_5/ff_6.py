from time import sleep
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


# Экземпляр драйвера Firefox
driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
driver.maximize_window()


# Открыть страницу
driver.get("http://the-internet.herokuapp.com/login")


# Поле 'username'
username_selector = 'input#username'
username = driver.find_element(By.CSS_SELECTOR, username_selector)


# В поле username ввести значение 'tomsmith'
username.send_keys('tomsmith')


# Спит 1 секунду
sleep(1)


# Поле 'password'
password_selector = 'input#password'
password = driver.find_element(By.CSS_SELECTOR, password_selector)


# В поле password ввести значение 'SuperSecretPassword!'
password.send_keys('SuperSecretPassword!')


# Спит 1 секунду
sleep(1)


# Кнопка 'Login'
login_selector = 'button[type="submit"]'
login_button = driver.find_element(By.CSS_SELECTOR, login_selector)


# Нажать кнопку 'Login'
login_button.click()


# Спит 2 секунды
sleep(2)


# Закрывает браузер
driver.quit()