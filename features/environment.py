from playwright.sync_api import sync_playwright
from src.config.settings import settings
from src.pages.login_page import LoginPage
from src.pages.inventory_page import InventoryPage
from src.utils.allure_attachments import attach_png, attach_html, attach_text


def before_all(context):
    context.settings = settings


def before_scenario(context, scenario):
    context.pw = sync_playwright().start()
    browser_type = getattr(context.pw, context.settings.browser)
    context.browser = browser_type.launch(headless=context.settings.headless)
    context.context = context.browser.new_context()
    context.page = context.context.new_page()

    context.login_page = LoginPage(context.page)
    context.inventory_page = InventoryPage(context.page)


def after_scenario(context, scenario):
    # Evidence-first: attach artifacts on failure
    if scenario.status == "failed":
        try:
            attach_png("screenshot", context.page.screenshot(full_page=True))
        except Exception as e:
            attach_text("screenshot_error", str(e))

        try:
            attach_html("page_html", context.page.content())
        except Exception as e:
            attach_text("html_error", str(e))

    context.context.close()
    context.browser.close()
    context.pw.stop()
