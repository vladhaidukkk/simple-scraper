from urllib.request import urlopen

from bs4 import BeautifulSoup


def main() -> None:
    base_url = "http://olympus.realpython.org"
    response = urlopen(f"{base_url}/profiles")
    html = response.read().decode("utf-8")
    soup = BeautifulSoup(html, "html.parser")

    for anchor in soup.find_all("a"):
        anchor_url = base_url + anchor["href"]
        print(anchor_url)


if __name__ == "__main__":
    main()
