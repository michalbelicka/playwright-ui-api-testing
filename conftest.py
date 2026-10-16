import pytest
from playwright.sync_api import Page
from playwright.sync_api import Playwright
from pages.login_page import LoginPage
from pages.signup_page import SignupPage
from pages.cart_page import CartPage
from pages.products_page import ProductsPage

@pytest.fixture
def home_page(page: Page):

    page.goto("https://www.automationexercise.com/")
    
    cookie_banner = page.get_by_role("button", name="Súhlas")

    if cookie_banner.is_visible():
        cookie_banner.click()

    return page

@pytest.fixture
def logged_in(home_page):

    signup_page = SignupPage(home_page)
    login_page = LoginPage(home_page)

    signup_page.click_signup_login()

    login_page.enter_login_details("tester2310@example.com", "password")
    
    login_page.click_login()

    return home_page

@pytest.fixture
def logged_in_and_empty_cart(logged_in):

    cart_page = CartPage(logged_in)

    cart_page.click_cart()

    cart_page.empty_cart()

    cart_page.close_ad()

    return logged_in

@pytest.fixture
def empty_cart(home_page):

    cart_page = CartPage(home_page)

    cart_page.click_cart()
    
    cart_page.empty_cart()
    
    cart_page.close_ad()

    return home_page

@pytest.fixture
def logged_in_with_product(logged_in):

    cart_page = CartPage(logged_in)
    
    cart_page.click_cart()
    
    cart_page.empty_cart()
    
    cart_page.close_ad()

    products_page = ProductsPage(logged_in)

    # products_page.click_products()

    logged_in.goto("https://www.automationexercise.com/products")

    if "google_vignette" in logged_in.url:
        cart_page.close_ad()

    products_page.add_product_to_cart("Blue Top")

    products_page.click_view_cart()

    return logged_in

@pytest.fixture
def api_request(playwright: Playwright):

    request_context = playwright.request.new_context()

    yield request_context

    request_context.dispose()