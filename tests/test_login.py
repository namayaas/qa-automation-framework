import pytest
from playwright.sync_api import expect
import config


@pytest.mark.smoke
def test_TC01_valid_login(login_page, page):
    login_page.login(**config.VALID_USER)
    expect(page).to_have_url(f"{config.BASE_URL}/inventory.html")


@pytest.mark.negative
def test_TC02_locked_out_user(login_page):
    login_page.login(**config.LOCKED_USER)
    expect(login_page.error).to_contain_text("locked out")


@pytest.mark.negative
def test_TC03_invalid_credentials(login_page):
    login_page.login(**config.INVALID_USER)
    expect(login_page.error).to_contain_text("do not match")


@pytest.mark.negative
def test_TC04_empty_username(login_page):
    login_page.login("", "secret_sauce")
    expect(login_page.error).to_contain_text("Username is required")


@pytest.mark.negative
def test_TC05_empty_password(login_page):
    login_page.login("standard_user", "")
    expect(login_page.error).to_contain_text("Password is required")
