from playwright.sync_api import sync_playwright
from seleniumbase import decorators


@decorators.print_runtime("Playwright flow, test-only")
def run(page):
    page.goto("https://seleniumbase.github.io/coffee/")
    page.locator('div[data-sb="Mocha"]').click()
    page.locator("button.pay").click()
    page.fill("input#name", "Selenium Coffee")
    page.fill("input#email", "test@test.test")
    page.locator("button#submit-payment").click()
    page.locator("#app div.success")
    print(page.url)


@decorators.print_runtime("Playwright flow with launch")
def main():
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()
        run(page)
        context.close()
        browser.close()


if __name__ == "__main__":
    main()
