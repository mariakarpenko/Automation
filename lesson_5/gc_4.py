from time import sleep
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By


# Экземпляр драйвера Chrome
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.maximize_window()


# Открыть страницу
driver.get("http://the-internet.herokuapp.com/entry_ad")


wait = WebDriverWait(driver, 10)
# Ожидание, пока модальное окно не появится
modal_window = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '.modal')))


# Ожидание, пока модальное окно не появится
close_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.modal-footer')))


# Спит 3 секунды
sleep(3)


# Клик на кнопку
close_button.click()


# Спит 3 секунды
sleep(3)