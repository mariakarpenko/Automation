from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By


# Экземпляр драйвера Chrome
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.maximize_window()


# Открыть страницу
driver.get("http://uitestingplayground.com/classattr")


# Кликнуть на синюю кнопку 3 раза + закрывает модальные окна
count = 0
for n in range(3):
    blue_button = driver.find_element("xpath", "//button[contains(concat(' ', normalize-space(@class), ' '), ' btn-primary ')]")
    blue_button.click()
    sleep(1)
    driver.switch_to.alert.accept()
    count = count + 1
    sleep(2)
    print(count)


# Спит 3 секунды
sleep(3)