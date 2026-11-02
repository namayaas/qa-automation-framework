from playwright.sync_api import Page


class InventoryPage:
    def __init__(self, page: Page):
        self.page = page
        self.title = page.locator("[data-test='title']")
        self.items = page.locator("[data-test='inventory-item']")
        self.cart_badge = page.locator("[data-test='shopping-cart-badge']")
        self.cart_link = page.locator("[data-test='shopping-cart-link']")
        self.sort_dropdown = page.locator("[data-test='product-sort-container']")
        self.prices = page.locator("[data-test='inventory-item-price']")

    def add_to_cart_by_index(self, index: int = 0):
        self.items.nth(index).locator("button").click()

    def sort_by(self, value: str):
        """value: az | za | lohi | hilo"""
        self.sort_dropdown.select_option(value)

    def price_list(self) -> list[float]:
        return [float(p.replace("$", "")) for p in self.prices.all_inner_texts()]

    def open_cart(self):
        self.cart_link.click()
