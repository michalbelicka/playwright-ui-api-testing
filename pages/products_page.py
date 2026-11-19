from playwright.sync_api import Page

class ProductsPage:
    def __init__(self, page: Page):
        self.page = page

    def click_products(self):
        self.page.get_by_role("link", name="Products").click()

    def all_products_heading(self):
        return self.page.locator(".title.text-center", has_text="All Products")

    def add_product_to_cart(self, product_name):
        product = self.page.locator(".productinfo").filter(has_text=product_name)
        product.scroll_into_view_if_needed()
        product.hover()
        product.get_by_text("Add to cart").click()

    def added_heading(self):
        return self.page.get_by_role("heading", name="Added!")

    def click_view_cart(self):
        self.page.get_by_role("link", name="View Cart").click()

    def search_product(self, product_name):
        self.page.get_by_placeholder("Search Product").fill(product_name)
        self.page.locator("#submit_search").click()

    def searched_products_heading(self):
        return self.page.get_by_role("heading", name="Searched Products")

    def searched_product(self, product_name):
        return self.page.locator(".productinfo", has_text=product_name)

    def view_product(self, product_name):
        product = self.page.locator(".product-image-wrapper", has_text=product_name)
        product.get_by_role("link", name="View Product").click()