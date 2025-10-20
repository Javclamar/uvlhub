from selenium.common.exceptions import NoSuchElementException
import time

from core.environment.host import get_host_for_selenium_testing
from core.selenium.common import initialize_driver, close_driver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys



def test_notepad_index():

    driver = initialize_driver()

    try:
        host = get_host_for_selenium_testing()

        # Open the login page
        driver.get(f"{host}/login")

        # Wait a little while to make sure the page has loaded completely
        time.sleep(4)

        # Find the username and password field and enter the values
        email_field = driver.find_element(By.NAME, "email")
        password_field = driver.find_element(By.NAME, "password")

        email_field.send_keys("user1@example.com")
        password_field.send_keys("1234")

        # Send the form
        password_field.send_keys(Keys.RETURN)

        # Wait a little while to ensure that the action has been completed
        time.sleep(4)

        try:
            driver.get(f"{host}/notepad")
            time.sleep(4)
            driver.find_element(By.XPATH, "/html/body/div/div/main/div/p")
            print("Test passed!")

        except NoSuchElementException:
            raise AssertionError('Test failed!')

    finally:

        close_driver(driver)


# Call the test function
test_notepad_index()
