import re
from urllib.request import urlopen


def get_tag_content(html: str, tag: str) -> str | None:
    match = re.search(rf"<{tag}.*?>(.*?)</{tag}.*?>", html, re.IGNORECASE)
    return match.groups()[0] if match else None


def get_param_value(html: str, param: str) -> str | None:
    param_start = html.find(param)
    if param_start < 0:
        return None

    relative_param_end = html[param_start:].find(":")
    if relative_param_end < 0:
        return None
    param_end = param_start + relative_param_end

    value_start = param_end + 1
    value_end = value_start + html[value_start:].find("<")
    value = html[value_start:] if value_end < 0 else html[value_start:value_end]
    return value.strip()


def main() -> None:
    url = "http://olympus.realpython.org/profiles/dionysus"
    response = urlopen(url)
    html = response.read().decode("utf-8")

    title = get_tag_content(html, "title")
    print(f"TITLE: {title}")

    for param in ("Name", "Hometown", "Favorite animal", "Favorite Color"):
        value = get_param_value(html, param)
        print(f"{param.upper()}: {value}")


if __name__ == "__main__":
    main()
