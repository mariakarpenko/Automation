from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By


# Экземпляр драйвера Chrome
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.maximize_window()


# Открыть страницу
driver.get("http://the-internet.herokuapp.com/add_remove_elements/")


# 5 раз кликнуть на кнопку "Add Element"
for n in range(5):
    add_element_selector = 'button[onclick="addElement()"]'
    add_element = driver.find_element(By.CSS_SELECTOR, add_element_selector)
    add_element.click()


# Собрать со страницы список кнопок "Delete"
delete_elements = driver.find_elements(By.CSS_SELECTOR, 'button.added-manually')


# Вывести на экран длину списка
print(len(delete_elements))


# Спит 1 секунду
sleep(1)