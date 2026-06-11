import allure
import pytest

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

@pytest.fixture
def driver():
    options = Options()
    options.add_argument("--headless")  # run without UI
    options.add_argument("--no-sandbox")  # required in many CI environments
    options.add_argument("--disable-dev-shm-usage")  # overcome limited /dev/shm size on Linux

    driver = webdriver.Chrome(options=options)
    driver.implicitly_wait(10)
    yield driver
    driver.quit()

@pytest.fixture
@allure.step("Подготовка валидных данных")
def valid_data():
    return "tomsmith", "SuperSecretPassword!"

@pytest.fixture
@allure.step("Подготовка невалидных данных")
def invalid_data():
    return "smithtom", "SuperSecretPassword!"