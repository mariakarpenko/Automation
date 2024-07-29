
from time import sleep
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

def testing_step_two():
    # Создаем экземпляр драйвера Chrome
    driver = webdriver.Chrome(service = ChromeService(ChromeDriverManager().install()))

    # Максимизируем окно браузера
    driver.maximize_window() 

    # Открываем страницу
    driver.get('https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html')

    # Добавляем неявное ожидание на всякий случай
    driver.implicitly_wait(10)

    # Очищаем поле для ввода времени задержки
    driver.find_element(By.CSS_SELECTOR, '#delay').clear()
    # В поле для ввода пишем ‘45’
    driver.find_element(By.CSS_SELECTOR, '#delay').send_keys('45')

    # Нажимаем на кнопки
    driver.find_element(By.XPATH, '//*[@id="calculator"]/div[2]/span[1]').click()
    sleep(2)
    driver.find_element(By.XPATH, '//*[@id="calculator"]/div[2]/span[4]').click()
    sleep(2)
    driver.find_element(By.XPATH, '//*[@id="calculator"]/div[2]/span[2]').click()
    sleep(2)
    driver.find_element(By.XPATH, '//*[@id="calculator"]/div[2]/span[15]').click()
    sleep(2)

    # Добавляем явное ожидание
    waiting_for_result = WebDriverWait(driver, 46)
    waiting_for_result.until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, 'div.screen'), '15'))

    # Проверьте (assert), что в окне отобразится результат '15' через 45 секунд
    result_txt = driver.find_element(By.CSS_SELECTOR, 'div.screen').text
    assert result_txt == '15'

    # Закрываем браузер
    driver.quit()