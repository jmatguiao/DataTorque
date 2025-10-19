from locators.login_locators import LoginLocators
from base.base_page import BasePage

class LoginMethods(BasePage):
    def login(self, username: str, password: str):
        self.page.fill(LoginLocators.USERNAME_INPUT, username)
        self.page.fill(LoginLocators.PASSWORD_INPUT, password)
        self.page.click(LoginLocators.LOGIN_BUTTON)