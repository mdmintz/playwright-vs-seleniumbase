from playwright.sync_api import sync_playwright
from seleniumbase import decorators


@decorators.print_runtime("Playwright flow, test-only")
def run(page):
    page.goto("https://www.saucedemo.com")
    page.locator("#user-name")
    page.fill("#user-name", "standard_user")
    page.fill("#password", "secret_sauce")
    page.locator('input[type="submit"]').click()
    page.locator('button[name*="backpack"]').click()
    page.locator("#shopping_cart_container a").click()
    page.locator("button#checkout").click()
    page.fill("input#first-name", "SeleniumBase")
    page.fill("input#last-name", "Automation")
    page.fill("input#postal-code", "77123")
    page.locator("input#continue").click()
    page.locator("button#finish").click()
    page.locator('img[alt="Pony Express"]')
    print(page.url)


@decorators.print_runtime("Playwright flow with launch")
def main():
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch()
        context = browser.new_context()
        page = context.new_page()
        run(page)
        context.close()
        browser.close()


if __name__ == "__main__":
    main()
