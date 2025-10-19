from locators.cart_locators import CartLocators
from locators.home_locators import HomeLocators
from base.base_page import BasePage

class CartMethods(BasePage):
    
    def go_to_cart(self):
        self.page.click(HomeLocators.CART_LINK)

    def get_cart_items(self):
        items = []
        for item in self.page.query_selector_all(CartLocators.CART_ITEMS):
            # extract only product name
            name = item.query_selector(".inventory_item_name").inner_text()
            items.append(name)
        return items  # <-- inside the function

    def checkout(self):
        self.page.click(CartLocators.CHECKOUT_BUTTON)