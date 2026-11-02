from playwright.sync_api import Page


class CartPage:
    def __init__(self, page: Page):
        self.page = page
        self.items = page.locator("[data-test='inventory-item']")
        self.checkout_btn = page.locator("[data-test='checkout']")

    def checkout(self):
        self.checkout_btn.click()
