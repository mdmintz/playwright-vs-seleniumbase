from playwright.sync_api import sync_playwright
from seleniumbase import decorators


def run(page):
    print('Start page = "%s"' % page.url)


@decorators.print_runtime("Playwright headless launch")
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
