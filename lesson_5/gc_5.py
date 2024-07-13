from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


# Экземпляр драйвера Chrome
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.maximize_window()


# Открыть страницу
driver.get("http://the-internet.herokuapp.com/inputs")


# Найти поле для ввода
input_field_selector = 'input[type="number"]'
input_field = driver.find_element(By.CSS_SELECTOR, input_field_selector)


# Ввести в поле текст '1000'
input_field.send_keys('1000')


# Спит 2 секунды
sleep(2)


# Очистить это поле (метод clear)
input_field.clear()


# Спит 2 секунды
sleep(2)


# Ввести в это же поле текст '999'
input_field.send_keys('999')


# Спит 2 секунды
sleep(2)