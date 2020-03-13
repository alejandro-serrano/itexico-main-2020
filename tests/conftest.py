import pytest
import selenium.webdriver

@pytest.fixture
def driver():
    driver = selenium.webdriver.Chrome()
    driver.implicitly_wait(10)
    driver.get('https://www.saucedemo.com/')
    yield driver
    driver.quit()
