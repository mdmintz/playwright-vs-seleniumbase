from seleniumbase import SB
from seleniumbase import decorators


@decorators.print_runtime("SeleniumBase flow, test-only")
def run(sb):
    sb.driver.get("https://seleniumbase.github.io/coffee/")
    sb.driver.wait_for_element("button.pay")
    sb.driver.click('div[data-sb="Mocha"]')
    sb.driver.click("button.pay")
    sb.driver.wait_for_element("input#name")
    sb.driver.send_keys("input#name", "Selenium Coffee")
    sb.driver.send_keys("input#email", "test@test.test")
    sb.driver.click("button#submit-payment")
    sb.driver.assert_element("#app div.success")
    print(sb.driver.current_url)


@decorators.print_runtime("SeleniumBase flow with launch")
def main():
    with SB(chs=True, pls="none", sjw=True) as sb:
        run(sb)


if __name__ == "__main__":
    main()
