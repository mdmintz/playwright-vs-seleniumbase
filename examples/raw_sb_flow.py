from seleniumbase import SB
from seleniumbase import decorators


@decorators.print_runtime("SeleniumBase Example")
def run(sb):
    sb.open("https://www.saucedemo.com")
    sb.type("#user-name", "standard_user")
    sb.type("#password", "secret_sauce")
    sb.click('input[type="submit"]')
    sb.click('button[name*="backpack"]')
    sb.click("#shopping_cart_container a")
    sb.click("button#checkout")
    sb.type("input#first-name", "SeleniumBase")
    sb.type("input#last-name", "Automation")
    sb.type("input#postal-code", "77123")
    sb.click("input#continue")
    sb.click("button#finish")
    sb.assert_element('img[alt="Pony Express"]')


with SB() as sb:
    run(sb)
