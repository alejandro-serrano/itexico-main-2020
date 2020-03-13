from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions

WAIT_FOR_ELEMENT = 0.5

class LoginPage():

    USERNAME_FLD = (By.ID, 'user-name')
    PASSWORD_FLD = (By.ID, 'password')
    LOGIN_BTN = (By.XPATH, '//input[@value="LOGIN"]')
    ERROR_MESSAGE = (By.XPATH, '//*[@data-test="error"]')
    EXPECTED_ERROR_MESSAGE = 'Epic sadface: Username and password do not match any user in this service'

    def __init__(self, driver):
        self.driver = driver

    def login(self, username, password):
        self._set_text(username, *self.USERNAME_FLD)
        self._set_text(password, *self.PASSWORD_FLD)
        self.driver.find_element(*self.LOGIN_BTN).click()
        self._check_login_successful()

    def _set_text(self, value, locator_type, locator):
        input_field = self.driver.find_element(locator_type, locator)
        input_field.clear()
        input_field.send_keys(value)

    def _get_text(self, locator_type, locator):
        return self.driver.find_element(locator_type, locator).text

    def _check_login_successful(self):
        try:
            WebDriverWait(self.driver, WAIT_FOR_ELEMENT).until(
                expected_conditions.invisibility_of_element_located(self.LOGIN_BTN))
        except:
            WebDriverWait(self.driver, WAIT_FOR_ELEMENT).until(
                expected_conditions.visibility_of_element_located(self.ERROR_MESSAGE))
            error_message = self._get_text(*self.ERROR_MESSAGE)
            raise LoginError(error_message)


class LoginError(Exception):
    pass
