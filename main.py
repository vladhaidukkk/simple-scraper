from urllib.request import urlopen

from bs4 import BeautifulSoup


def main() -> None:
    url = "http://olympus.realpython.org/profiles/dionysus"
    response = urlopen(url)
    html = response.read().decode("utf-8")
    soup = BeautifulSoup(html, "html.parser")

    if soup.title:
        print(f"TITLE: {soup.title.string}")

    body = soup.find("body")
    if body:
        for line in filter(None, body.get_text().splitlines()):
            param, value = line.split(": ")
            print(f"{param.upper()}: {value}")


if __name__ == "__main__":
    main()
