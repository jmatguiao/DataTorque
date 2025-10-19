from locators.home_locators import HomeLocators
from base.base_page import BasePage

class HomeMethods(BasePage):
    def get_inventory_items(self):
        return self.page.query_selector_all(HomeLocators.INVENTORY_ITEMS)

    def add_backpack_to_cart(self):
        self.page.click(HomeLocators.BACKPACK_ADD_BTN)

    def add_bike_light_to_cart(self):
        self.page.click(HomeLocators.BIKE_LIGHT_ADD_BTN)

    def get_cart_count(self):
        badge = self.page.query_selector(HomeLocators.CART_BADGE)
        if badge:
            return int(badge.inner_text())
        return 0