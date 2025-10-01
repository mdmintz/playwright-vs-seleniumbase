import timeit
from playwright.sync_api import sync_playwright


def run(page):
    print('Start page = "%s"' % page.url)


def main():
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch()
        context = browser.new_context()
        page = context.new_page()
        run(page)
        context.close()
        browser.close()


if __name__ == "__main__":
    runtime = timeit.timeit(stmt="main()", globals=globals(), number=1)
    print("{Playwright headless launch} ran for %.3f seconds" % runtime)
