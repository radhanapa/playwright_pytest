from playwright.sync_api import Page


class ProductsPage:
    def __init__(self, page: Page):
        self.page = page
        self.title = page.locator(".title")
        self.inventory_items = page.locator(".inventory_item")
        self.cart_badge = page.locator(".shopping_cart_badge")

    def add_first_item_to_cart(self):
        # Clicks the 'Add to cart' button of the first item in the list
        self.inventory_items.first.locator("button").click()

    def get_cart_count(self):
        return self.cart_badge.text_content()
