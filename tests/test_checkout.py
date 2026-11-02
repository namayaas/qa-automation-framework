import pytest
from playwright.sync_api import expect
import config


@pytest.mark.smoke
def test_TC10_end_to_end_purchase(logged_in, cart_page, checkout_page):
    logged_in.add_to_cart_by_index(0)
    logged_in.open_cart()
    expect(cart_page.items).to_have_count(1)
    cart_page.checkout()
    info = config.CHECKOUT_INFO
    checkout_page.fill_info(info["first"], info["last"], info["zip"])
    checkout_page.finish()
    expect(checkout_page.complete_header).to_have_text("Thank you for your order!")


@pytest.mark.negative
def test_TC11_checkout_requires_first_name(logged_in, cart_page, checkout_page):
    logged_in.add_to_cart_by_index(0)
    logged_in.open_cart()
    cart_page.checkout()
    checkout_page.fill_info("", "User", "97201")
    expect(checkout_page.error).to_contain_text("First Name is required")
