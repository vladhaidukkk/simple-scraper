from time import sleep

from mechanicalsoup import Browser


def main() -> None:
    browser = Browser()

    for i in range(5):
        if i != 0:
            sleep(1)

        resp = browser.get("http://olympus.realpython.org/dice")
        result = resp.soup.select_one("#result").text  # type: ignore
        print(result)


if __name__ == "__main__":
    main()
