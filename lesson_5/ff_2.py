from time import sleep
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By


# Экземпляр драйвера Firefox
driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
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


# Закрывает браузер
driver.quit()