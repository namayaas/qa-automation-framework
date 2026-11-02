import pytest
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
import config


@pytest.fixture
def login_page(page):
    return LoginPage(page).open()


@pytest.fixture
def logged_in(page, login_page):
    """Logs in as the standard user and returns the inventory page object."""
    login_page.login(**config.VALID_USER)
    return InventoryPage(page)


@pytest.fixture
def cart_page(page):
    return CartPage(page)


@pytest.fixture
def checkout_page(page):
    return CheckoutPage(page)
