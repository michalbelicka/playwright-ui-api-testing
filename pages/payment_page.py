from playwright.sync_api import Page

class PaymentPage:
    def __init__(self, page: Page):
        self.page = page

    def payment_heading(self):
            return self.page.get_by_role("heading", name="Payment")
    
    def fill_payment_details(self, name, card_number, cvc, expiry_month, expiry_year):
        self.page.locator('[data-qa="name-on-card"]').fill(name)
        self.page.locator('[data-qa="card-number"]').fill(card_number)
        self.page.locator('[data-qa="cvc"]').fill(cvc)
        self.page.locator('[data-qa="expiry-month"]').fill(expiry_month)
        self.page.locator('[data-qa="expiry-year"]').fill(expiry_year)

    def click_pay_and_confirm_order(self):
         self.page.get_by_role("button", name="Pay and Confirm Order").click()

    def order_placed_heading(self):
        return self.page.locator('[data-qa="order-placed"]').get_by_text("Order Placed!")

    def click_download_invoice(self):
         self.page.locator("a.btn.check_out").get_by_text("Download Invoice").click()