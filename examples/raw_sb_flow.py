from seleniumbase import SB
from seleniumbase import decorators


@decorators.print_runtime("SeleniumBase flow, test-only")
def run(sb):
    sb.get("https://seleniumbase.github.io/coffee/")
    sb.click('div[data-sb="Mocha"]')
    sb.click("button.pay")
    sb.send_keys("input#name", "Selenium Coffee")
    sb.driver.send_keys("input#email", "test@test.test")
    sb.driver.click("button#submit-payment")
    sb.find_element("#app div.success")
    print(sb.driver.current_url)


@decorators.print_runtime("SeleniumBase flow with launch")
def main():
    with SB(pls="none") as sb:
        run(sb)


if __name__ == "__main__":
    main()
