from selenium.webdriver.common.by import By

def test_successful_login(driver):
    driver.get("https://the-internet.herokuapp.com/login")
    input_username = driver.find_element(By.ID, "username")
    input_username.send_keys("tomsmith")

    input_password = driver.find_element(By.ID,"password")
    input_password.send_keys("SuperSecretPassword!")

    button_login = driver.find_element(By.CLASS_NAME, "radius")
    button_login.click()

    assert driver.find_element(By.ID,"flash").text == "You logged into a secure area!\n×"

def test_unsuccessful_login(driver):
    driver.get("https://the-internet.herokuapp.com/login")
    input_username = driver.find_element(By.ID, "username")
    input_username.send_keys("smithtom")

    input_password = driver.find_element(By.ID, "password")
    input_password.send_keys("SuperSecretPassword!")

    button_login = driver.find_element(By.CLASS_NAME, "radius")
    button_login.click()

    assert driver.find_element(By.ID, "flash").text == "Your username is invalid!\n×"