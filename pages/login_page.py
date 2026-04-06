# pages/login_page.py


class LoginPage:
    def __init__(self, page):
        self.page = page
        self.username_input = page.locator("#user-name")
        self.password_input = page.locator("#password")
        self.login_button = page.locator("#login-button")
        # ADD THIS LINE BELOW:
        self.error_message = page.locator("[data-test='error']")

    def navigate(self):
        self.page.goto("https://www.saucedemo.com/")

    def login(self, user, pwd):
        self.username_input.fill(user)
        self.password_input.fill(pwd)
        self.login_button.click()
