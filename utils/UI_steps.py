import allure
from selenium.webdriver.common.by import By

@allure.step("Открываем страницу сайта")
def open_page(driver):
    driver.get("https://the-internet.herokuapp.com/login")

@allure.step("Заполняем поля логин и пароль")
def put_login_password(driver, data):
    input_username = driver.find_element(By.ID, "username")
    input_username.send_keys(data[0])

    input_password = driver.find_element(By.ID, "password")
    input_password.send_keys(data[1])

@allure.step("Кликаем кнопку для отправки")
def click(driver):
    button_login = driver.find_element(By.CLASS_NAME, "radius")
    button_login.click()