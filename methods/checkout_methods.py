from locators.checkout_locators import CheckoutLocators
from base.base_page import BasePage

class CheckoutMethods(BasePage):
    def fill_checkout_info(self, first_name, last_name, postal_code):
        self.page.fill(CheckoutLocators.FIRST_NAME, first_name)
        self.page.fill(CheckoutLocators.LAST_NAME, last_name)
        self.page.fill(CheckoutLocators.POSTAL_CODE, postal_code)
        self.page.click(CheckoutLocators.CONTINUE_BUTTON)

    def finish_checkout(self):
        self.page.click(CheckoutLocators.FINISH_BUTTON)

    def get_complete_message(self):
        return self.page.inner_text(CheckoutLocators.COMPLETE_MESSAGE)