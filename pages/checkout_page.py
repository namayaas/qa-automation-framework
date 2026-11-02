from playwright.sync_api import Page


class CheckoutPage:
    def __init__(self, page: Page):
        self.page = page
        self.first = page.locator("[data-test='firstName']")
        self.last = page.locator("[data-test='lastName']")
        self.zip = page.locator("[data-test='postalCode']")
        self.continue_btn = page.locator("[data-test='continue']")
        self.finish_btn = page.locator("[data-test='finish']")
        self.complete_header = page.locator("[data-test='complete-header']")
        self.error = page.locator("[data-test='error']")

    def fill_info(self, first: str, last: str, zip_code: str):
        self.first.fill(first)
        self.last.fill(last)
        self.zip.fill(zip_code)
        self.continue_btn.click()

    def finish(self):
        self.finish_btn.click()
