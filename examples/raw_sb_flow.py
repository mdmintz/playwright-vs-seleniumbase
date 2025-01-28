from seleniumbase import SB
from seleniumbase import decorators


@decorators.print_runtime("SeleniumBase flow, test-only")
def run(sb):
    sb.open("https://www.saucedemo.com")
    sb.send_keys("#user-name", "standard_user")
    sb.send_keys("#password", "secret_sauce")
    sb.click('input[type="submit"]')
    sb.click('button[name*="backpack"]')
    sb.click("#shopping_cart_container a")
    sb.click("button#checkout")
    sb.send_keys("input#first-name", "SeleniumBase")
    sb.send_keys("input#last-name", "Automation")
    sb.send_keys("input#postal-code", "77123")
    sb.click("input#continue")
    sb.click("button#finish")
    sb.assert_element('img[alt="Pony Express"]')
    print(sb.get_current_url())


@decorators.print_runtime("SeleniumBase flow with launch")
def main():
    with SB() as sb:
        run(sb)


if __name__ == "__main__":
    main()
