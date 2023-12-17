from urllib.request import urlopen


def get_tag_content(html: str, tag: str) -> str:
    tag_start = html.index(f"<{tag}")
    start = tag_start + html[tag_start:].index(">") + 1
    end = html.index(f"</{tag}")
    return html[start:end]


def main() -> None:
    url = "http://olympus.realpython.org/profiles/poseidon"
    response = urlopen(url)
    html = response.read().decode("utf-8")

    title = get_tag_content(html, "title")
    print(title)


if __name__ == "__main__":
    main()
