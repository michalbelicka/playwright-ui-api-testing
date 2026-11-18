from pages.products_page import ProductsPage
from pages.cart_page import CartPage
from playwright.sync_api import expect

def test_add_product_to_cart(logged_in_and_empty_cart):

    products_page = ProductsPage(logged_in_and_empty_cart)
    cart_page = CartPage(logged_in_and_empty_cart)

    products_page.click_products()

    expect(products_page.all_products_heading()).to_be_visible()

    products_page.add_product_to_cart("Blue Top")

    expect(products_page.added_heading()).to_be_visible()

    products_page.click_view_cart()

    expect(cart_page.product_in_cart("Blue Top")).to_be_visible()