
import allure
from selenium.webdriver.common.by import By

from utils.UI_steps import open_page, put_login_password, click

@allure.title("Успешная авторизация")
@allure.description("Авторизация пользователя при введении валидных данных")
def test_successful_login(driver, valid_data):
    open_page(driver)
    put_login_password(driver, valid_data)
    click(driver)
    with allure.step("Проверка того что открывается страница подтверждения входа"):
        assert driver.find_element(By.ID,"flash").text == "You logged into a secure area!\n×"

@allure.title("Неуспешная авторизация")
@allure.description("Попытка авторизации пользователя при введении невалидных данных")
def test_unsuccessful_login(driver, invalid_data):
    open_page(driver)
    put_login_password(driver, invalid_data)
    click(driver)

    with allure.step("Проверка того что открывается страница с сообщением о неверном логине"):
        assert driver.find_element(By.ID, "flash").text == "Your username is invalid!\n×"