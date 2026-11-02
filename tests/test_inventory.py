import pytest
from playwright.sync_api import expect


@pytest.mark.smoke
def test_TC06_products_displayed(logged_in):
    expect(logged_in.title).to_have_text("Products")
    expect(logged_in.items).to_have_count(6)


@pytest.mark.regression
def test_TC07_sort_price_low_to_high(logged_in):
    logged_in.sort_by("lohi")
    prices = logged_in.price_list()
    assert prices == sorted(prices)


@pytest.mark.regression
def test_TC08_sort_price_high_to_low(logged_in):
    logged_in.sort_by("hilo")
    prices = logged_in.price_list()
    assert prices == sorted(prices, reverse=True)


@pytest.mark.regression
def test_TC09_add_item_updates_cart_badge(logged_in):
    logged_in.add_to_cart_by_index(0)
    expect(logged_in.cart_badge).to_have_text("1")
