import allure


def attach_text(name: str, content: str):
    allure.attach(content, name=name, attachment_type=allure.attachment_type.TEXT)


def attach_png(name: str, png_bytes: bytes):
    allure.attach(png_bytes, name=name, attachment_type=allure.attachment_type.PNG)


def attach_html(name: str, html: str):
    allure.attach(html, name=name, attachment_type=allure.attachment_type.HTML)
