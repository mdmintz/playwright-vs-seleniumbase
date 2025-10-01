import timeit
from seleniumbase import SB


def run(sb):
    print('Start page = "%s"' % sb.driver.current_url)


def main():
    with SB(chs=True, pls="none") as sb:
        run(sb)


if __name__ == "__main__":
    runtime = timeit.timeit(stmt="main()", globals=globals(), number=1)
    print("{SeleniumBase headless launch} ran for %.3f seconds" % runtime)
