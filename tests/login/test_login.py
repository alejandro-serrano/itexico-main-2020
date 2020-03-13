import pytest
from src.login.login import LoginPage, LoginError

def test_login_successful(driver):
    login_page = LoginPage(driver)
    login_page.login(username="standard_user", password="secret_sauce")

def test_login_unsuccessful(driver):
    login_page = LoginPage(driver)
    with pytest.raises(LoginError):
        login_page.login(username="locked_out_user", password="secret_sauce")
