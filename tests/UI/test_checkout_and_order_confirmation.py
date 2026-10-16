from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
from pages.payment_page import PaymentPage
from playwright.sync_api import expect

def test_checkout_and_order_confirmation(logged_in_with_product):

    cart_page = CartPage(logged_in_with_product)
    checkout_page = CheckoutPage(logged_in_with_product)
    payment_page = PaymentPage(logged_in_with_product)

    expect(cart_page.product_in_cart("Blue Top")).to_be_visible()

    cart_page.click_proceed_to_checkout()

    expect(checkout_page.delivery_address_heading()).to_be_visible()

    expect(checkout_page.billing_address_heading()).to_be_visible()

    expect(checkout_page.review_order_heading()).to_be_visible()

    expect(checkout_page.product_name("Blue Top")).to_be_visible()

    order_comment = "Please deliver the order in the morning."

    checkout_page.enter_order_comment(order_comment)

    checkout_page.click_place_order()

    cart_page.close_ad()
    
    if "google_vignette" in logged_in_with_product.url:
            cart_page.close_ad()

    expect(payment_page.payment_heading()).to_be_visible()

    payment_page.fill_payment_details(
        name="Test User",
        card_number="4242424242424242",
        cvc="123",
        expiry_month="12",
        expiry_year="2030"
    )

    payment_page.click_pay_and_confirm_order()

    expect(payment_page.order_placed_heading()).to_be_visible()
