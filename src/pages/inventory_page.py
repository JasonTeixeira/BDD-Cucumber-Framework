from playwright.sync_api import Page, expect


class InventoryPage:
    def __init__(self, page: Page):
        self.page = page
        self.title = page.locator(".title")
        self.items = page.locator(".inventory_item")

    def assert_loaded(self):
        expect(self.title).to_have_text("Products")
        expect(self.items.first).to_be_visible()
