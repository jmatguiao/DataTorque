import pytest
from playwright.sync_api import sync_playwright
from methods.login_methods import LoginMethods
from methods.home_methods import HomeMethods
from methods.cart_methods import CartMethods
from methods.checkout_methods import CheckoutMethods
import os

USERNAME = "standard_user"
PASSWORD = "secret_sauce"
URL = "https://www.saucedemo.com/"

@pytest.fixture(scope="session")
def browser():
    os.makedirs("test_results/videos", exist_ok=True)
    os.makedirs("test_results/screenshots", exist_ok=True)
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context(record_video_dir="test_results/videos/")
        page = context.new_page()
        yield page, context  # yield both page and context
        context.close()
        browser.close()

def test_purchase_two_items(browser):
    page, context = browser

    login_page = LoginMethods(page)
    home_page = HomeMethods(page)
    checkout_page = CheckoutMethods(page)
    cart_page = CartMethods(page)

    #TC001 - Login page
    login_page.navigate(URL)
    login_page.login(USERNAME, PASSWORD)
    login_page.take_screenshot("login_success")

    #TC002 -  Add first two items to cart
    home_page.add_backpack_to_cart()
    home_page.add_bike_light_to_cart()
    home_page.take_screenshot("items_added_to_cart")

    #TC003 -  Go to cart and verify added items
    cart_page.go_to_cart()
    cart_page.take_screenshot("cart_page")
    items_in_cart = cart_page.get_cart_items()
    assert "Sauce Labs Backpack" in items_in_cart
    assert "Sauce Labs Bike Light" in items_in_cart
    assert len(items_in_cart) == 2

    #TC004 -  Checkout page
    cart_page.checkout()
    checkout_page.fill_checkout_info("Jona Marie", "Guiao", "2025")
    checkout_page.finish_checkout()
    checkout_page.take_screenshot("checkout_complete")

    # Verify checkout complete
    assert checkout_page.get_complete_message() == "Thank you for your order!"