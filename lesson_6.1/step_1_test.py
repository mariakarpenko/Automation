import time
from selenium import webdriver
# from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

def testing_step_one():
    # Создаем экземпляр драйвера Chrome
    driver = webdriver.Chrome(service = ChromeService(ChromeDriverManager().install()))


    # Максимизируем окно браузера
    driver.maximize_window() 


    # Открываем страницу
    driver.get('https://bonigarcia.dev/selenium-webdriver-java/data-types.html')


    # Добавляем неявное ожидание на всякий случай
    driver.implicitly_wait(10)


    # Заполняем форму
    # Поле ‘First name’
    first_name = driver.find_element(By.CSS_SELECTOR, 'input[name="first-name')
    first_name.send_keys('Иван')

    # Поле ‘Last name’
    last_name = driver.find_element(By.CSS_SELECTOR, 'input[name="last-name"]')
    last_name.send_keys('Петров')

    # Поле ‘Address’
    address = driver.find_element(By.CSS_SELECTOR, 'input[name="address"]')
    address.send_keys('Ленина, 55-3')

    # Поле ‘Zip code’
    zip_code = driver.find_element(By.CSS_SELECTOR, 'input[name="zip-code"]')
    zip_code.send_keys('')

    # Поле ‘City’
    city = driver.find_element(By.CSS_SELECTOR, 'input[name="city"]')
    city.send_keys('Москва')

    # Поле ‘Country’
    country = driver.find_element(By.CSS_SELECTOR, 'input[name="country"]')
    country.send_keys('Россия')

    # Поле ‘E-mail’
    e_mail = driver.find_element(By.CSS_SELECTOR, 'input[name="e-mail"]')
    e_mail. send_keys('test@skypro.com')

    # Поле ‘Phone number’
    phone_number = driver.find_element(By.CSS_SELECTOR, 'input[name="phone"]')
    phone_number. send_keys('+7985899998787')

    # Поле ‘Job position’
    job_position = driver.find_element(By.CSS_SELECTOR, 'input[name="job-position"]')
    job_position. send_keys('QA')

    # Поле ‘Company’
    company = driver.find_element(By.CSS_SELECTOR, 'input[name="company"]')
    company. send_keys('SkyPro')

    # Нажимаем на кнопку ‘Submit’
    driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()


    # Неявное ожидание
    driver.implicitly_wait(10)

    # Проверяем (assert), что поле Zip code подсвечено красным
    zip_code_color_attribute = driver.find_element(By.CSS_SELECTOR, '#zip-code').value_of_css_property('background-color')
    assert zip_code_color_attribute == 'rgba(248, 215, 218, 1)'


    # Проверяем, что остальные поля подсвечены зеленым
    first_name_color_attribute = driver.find_element(By.CSS_SELECTOR, '#first-name').value_of_css_property('background-color')
    assert first_name_color_attribute == 'rgba(209, 231, 221, 1)'

    last_name_color_attribute = driver.find_element(By.CSS_SELECTOR, '#last-name').value_of_css_property('background-color')
    assert last_name_color_attribute == 'rgba(209, 231, 221, 1)'

    address_color_attribute = driver.find_element(By.CSS_SELECTOR, '#address').value_of_css_property('background-color')
    assert address_color_attribute == 'rgba(209, 231, 221, 1)'

    city_color_attribute = driver.find_element(By.CSS_SELECTOR, '#city').value_of_css_property('background-color')
    assert city_color_attribute == 'rgba(209, 231, 221, 1)'

    country_color_attribute = driver.find_element(By.CSS_SELECTOR, '#country').value_of_css_property('background-color')
    assert country_color_attribute == 'rgba(209, 231, 221, 1)'

    e_mail_color_attribute = driver.find_element(By.CSS_SELECTOR, '#e-mail').value_of_css_property('background-color')
    assert e_mail_color_attribute == 'rgba(209, 231, 221, 1)'

    phone_number_color_attribute = driver.find_element(By.CSS_SELECTOR, '#phone').value_of_css_property('background-color')
    assert phone_number_color_attribute == 'rgba(209, 231, 221, 1)'

    job_position_color_attribute = driver.find_element(By.CSS_SELECTOR, '#job-position').value_of_css_property('background-color')
    assert job_position_color_attribute == 'rgba(209, 231, 221, 1)'

    company_color_attribute = driver.find_element(By.CSS_SELECTOR, '#company').value_of_css_property('background-color')
    assert company_color_attribute == 'rgba(209, 231, 221, 1)'
 

    # Закрываем браузер
    driver.quit()