
from time import sleep
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By


# Создаем экземпляр драйвера Chrome
driver = webdriver.Chrome(service = ChromeService(ChromeDriverManager().install()))


# Максимизируем окно браузера
driver.maximize_window() 


# Открываем страницу
driver.get('https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html')


# Добавляем неявное ожидание на всякий случай
driver.implicitly_wait(10)


# В поле для ввода пишем ‘45’
input_field = driver.find_element(By.CSS_SELECTOR, '#delay')
input_field.send_keys('45')


# Нажимаем на кнопки
driver.find_element(By.XPATH, '//*[@id="calculator"]/div[2]/span[1]').click()
sleep(2)
driver.find_element(By.XPATH, '//*[@id="calculator"]/div[2]/span[4]').click()
sleep(2)
driver.find_element(By.XPATH, '//*[@id="calculator"]/div[2]/span[2]').click()
sleep(2)
driver.find_element(By.XPATH, '//*[@id="calculator"]/div[2]/span[15]').click()
sleep(2)


# Добавляем неявное ожидание
driver.implicitly_wait(50)


# Проверьте (assert), что в окне отобразится результат 15 через 45 секунд
def test_result():
 result_txt = driver.find_element(By.CSS_SELECTOR, 'div.screen').text
 assert result_txt == '15'


# Закрываем браузер
driver.quit()