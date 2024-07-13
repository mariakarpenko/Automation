from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By


# Экземпляр драйвера Chrome
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.maximize_window()


# Открыть страницу
driver.get("http://uitestingplayground.com/dynamicid")


# Кликаем 3 раза
count = 0
for n in range(3):
    button_selector = 'button.btn-primary'
    button = driver.find_element(By.CSS_SELECTOR, button_selector).click()
    count = count + 1
    sleep(2)
    print(count)


# Спит 3 секунду
sleep(3)