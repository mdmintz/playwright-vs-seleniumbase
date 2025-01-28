from seleniumbase import SB
from seleniumbase import decorators


def run(sb):
    print('Start page = "%s"' % sb.driver.current_url)


@decorators.print_runtime("SeleniumBase headless launch")
def main():
    with SB(chs=True) as sb:
        run(sb)


if __name__ == "__main__":
    main()
