from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
from pages.payment_page import PaymentPage
import tempfile
from pathlib import Path
from playwright.sync_api import expect

def test_download_invoice(logged_in_with_product):

    cart_page = CartPage(logged_in_with_product)
    checkout_page = CheckoutPage(logged_in_with_product)
    payment_page = PaymentPage(logged_in_with_product)

    cart_page.click_proceed_to_checkout()

    checkout_page.click_place_order()

    cart_page.close_ad()

    payment_page.fill_payment_details(
            name="Test User",
            card_number="4242424242424242",
            cvc="123",
            expiry_month="12",
            expiry_year="2030"
    )

    payment_page.click_pay_and_confirm_order()

    with tempfile.TemporaryDirectory() as tmp:
        with logged_in_with_product.expect_download() as download_info:
            payment_page.click_download_invoice()

        download = download_info.value
        invoice_path = Path(tmp) / download.suggested_filename
        download.save_as(invoice_path)

        assert invoice_path.exists()
        assert invoice_path.stat().st_size > 0

        invoice_text = invoice_path.read_text()

        assert "Hi Tester Testing, Your total purchase amount is 500. Thank you" in invoice_text