from playwright.sync_api import Page
import config


class LoginPage:
    def __init__(self, page: Page):
        self.page = page
        self.username = page.locator("[data-test='username']")
        self.password = page.locator("[data-test='password']")
        self.login_btn = page.locator("[data-test='login-button']")
        self.error = page.locator("[data-test='error']")

    def open(self):
        self.page.goto(config.BASE_URL)
        return self

    def login(self, username: str, password: str):
        self.username.fill(username)
        self.password.fill(password)
        self.login_btn.click()
