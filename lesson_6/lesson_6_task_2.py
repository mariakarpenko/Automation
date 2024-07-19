from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

# Экземпляр драйвера Chrome
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.maximize_window()


# Открываем страницу
driver.get("http://uitestingplayground.com/textinput")


# Ищем поле для ввода
input_field = driver.find_element(By.ID, 'newButtonName')


# Вводим в поле новое имя для кнопки
input_field.send_keys('SkyPro')


# Ищем и нажимаем на синюю кнопку
blue_button = driver.find_element(By.ID, 'updatingButton')
blue_button.click()


# Считываем новый текст с кнопки
txt = blue_button.text


# Печатаем текст
print(txt)


# Закрываем браузер
driver.quit()