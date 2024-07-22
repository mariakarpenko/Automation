from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By


# Экземпляр драйвера Chrome, максимизируем окно, добавляем явное ожидание
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.maximize_window()
waiter = WebDriverWait(driver, 40)

# Открываем страницу
driver.get("https://bonigarcia.dev/selenium-webdriver-java/loading-images.html")

# Ждем, пока не загрузятся все страницы (определяем по появлению надписи "Done!")
waiter.until(
    EC.text_to_be_present_in_element((By.CSS_SELECTOR, 'p.lead#text'), 'Done!')
)


# Ищем третий элемент (медаль)
award = driver.find_element(By.CSS_SELECTOR, 'img[alt="award"]')


# Запрашиваем значение атрибута 'src' элемента
award_src = award.get_attribute('src')


# Печатаем значение атрибута 'src'
print(award_src)


# Закрываем браузер
driver.quit()