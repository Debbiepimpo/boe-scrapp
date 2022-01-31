from urllib.parse import urlparse
import requests
from bs4 import BeautifulSoup as bs


def get_repos(url, name_arts):
    arts = urlparse(url)

    if arts.scheme and arts.netloc:
        articulos = requests.get(url, name_arts)
        if articulos.ok:
            return articulos.json()
    return None


def html_tags(articulos):
    soup = bs()
    html = soup.new_tag("html")
    soup.append(html)
    unordered_list = soup.new_tag("ul")
    for art in articulos:
        list_art = soup.new_tag("li")
        list_art.append(art["name"])
        unordered_list.append(list_art)
    html.append(unordered_list)

    return soup


if __name__ == "__main__":
    NAME_ARTS = {
        "name": "name1",
        "name2": "name2",
        "name3": "name3",
        "name4": "name4",
    }
    URL = "https://www.boe.es/boe/dias/2022/01/31/"
    print(get_repos(URL, NAME_ARTS))
    print(html_tags(get_repos(URL, NAME_ARTS)).prettify())