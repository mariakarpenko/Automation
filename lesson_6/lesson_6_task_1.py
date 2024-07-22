from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By


# Экземпляр драйвера Chrome
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.maximize_window()


# Добавляем неявное ожидание
driver.implicitly_wait(20)


# Открываем страницу
driver.get("http://uitestingplayground.com/ajax")


# Ищем и нажимаем на кнопку
driver.find_element(By.CSS_SELECTOR, '#ajaxButton').click()


# Ищем зеленый элемент и запрашиваем его текст
content = driver.find_element(By.CSS_SELECTOR, '#content')
txt = content.find_element(By.CSS_SELECTOR, 'p.bg-success').text


# Печатаем текст элемента
print(txt)


# Закрываем браузер
driver.quit()