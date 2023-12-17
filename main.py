from bs4 import BeautifulSoup
from mechanicalsoup import Browser


def main() -> None:
    base_url = "http://olympus.realpython.org"
    browser = Browser()
    login_resp = browser.get(f"{base_url}/login")
    login: BeautifulSoup = login_resp.soup  # type: ignore

    form = login.select("form")[0]
    form.select("input")[0]["value"] = "zeus"
    form.select("input")[1]["value"] = "ThunderDude"

    profiles_resp = browser.submit(form, login_resp.url)
    profiles: BeautifulSoup = profiles_resp.soup  # type: ignore

    for anchor in profiles.select("a"):
        anchor_url = base_url + anchor["href"]  # type: ignore
        print(anchor_url)


if __name__ == "__main__":
    main()
