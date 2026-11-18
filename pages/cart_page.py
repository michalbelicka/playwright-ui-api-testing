from playwright.sync_api import Page
from playwright.sync_api import expect

class CartPage:
    def __init__(self, page: Page):
        self.page = page

    def click_cart(self):
        self.page.get_by_role("link", name=" Cart").click()

    def cart_is_empty_message(self):
        return self.page.locator(".text-center", has_text="Cart is empty!")

    def empty_cart(self):
        delete_buttons = self.page.locator(".cart_quantity_delete").filter(visible=True).first

        while delete_buttons.count() > 0:
            try:
                delete_buttons.click(force=True)

                self.page.wait_for_load_state("networkidle")

            except Exception:
                break


    def product_in_cart(self, product_name):
        return self.page.locator(".cart_description", has_text=product_name)

    def remove_product(self, product_name):
        product = self.page.locator("#cart_info", has_text=product_name)

        product.locator(".cart_quantity_delete").click()

    def product_quantity(self, product_name):
        product = self.page.locator("#cart_info", has_text=product_name)

        return product.locator(".disabled")

    def product_total_price(self, product_name):
        product = self.page.locator("#cart_info", has_text=product_name)

        return product.locator("p.cart_total_price")

    def click_proceed_to_checkout(self):
        self.page.locator("a.check_out").click()