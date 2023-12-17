from urllib.request import urlopen

url = "http://olympus.realpython.org/profiles/aphrodite"
response = urlopen(url)
html = response.read().decode("utf-8")

print(html)
