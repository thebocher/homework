from typing import Union, List

import requests

from bs4 import BeautifulSoup

from tools import get_url, prepare_url, prepare_urls
from constants import SEARCH_PATTERN


url = get_url()

html = str(requests.get(url).content, 'utf-8')

def get_urls(url: str) -> List[str]:
    soup = get_soup(html, 'lxml')
    pages_count = get_pages_count(soup)
    prepared_urls = prepare_urls(url, SEARCH_PATTERN, pages_count)
    return prepared_urls

def get_soup(html: str, parser: Union[str, None] = None) -> BeautifulSoup:
    if parser is None:
        return BeautifulSoup(html)

    return BeautifulSoup(html, parser)

def get_pages_count(soup: BeautifulSoup) -> int:
    span = soup.find_all('span', class_='item fleft')[-1]
    count = int(span.text)
    return count

def get_offers_urls(url: str) -> List[str]:
    html = str(requests.get(url).content, 'utf-8')
    soup = get_soup(html, 'lxml')
    table = soup.find('table', class_='fixed offers breakword redesigned')
    tags_a = table.find_all('a', class_='marginright5 link linkWithHash detailsLink')

    links = []

    for tag_a in tags_a:
        href = tag_a.attrs.get('href')
        if href:
            links.append(href)

    return links

urls = get_urls(url)

print(get_offers_urls(urls[0]))