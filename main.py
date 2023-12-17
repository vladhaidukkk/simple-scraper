import re
from urllib.request import urlopen


def get_tag_content(html: str, tag: str) -> str | None:
    match = re.search(rf"<{tag}.*?>(.*?)</{tag}.*?>", html, re.IGNORECASE)
    return match.groups()[0] if match else None


def main() -> None:
    url = "http://olympus.realpython.org/profiles/poseidon"
    response = urlopen(url)
    html = response.read().decode("utf-8")

    title = get_tag_content(html, "title")
    print(title)


if __name__ == "__main__":
    main()
