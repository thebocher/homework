from typing import Union, List

import requests

from bs4 import BeautifulSoup

from tools import get_url, prepare_url, prepare_urls
from constants import SEARCH_PATTERN

from mongodb_connection import OLXOffer, connect_to_mongo

import re

import csv


url = get_url()

html = str(requests.get(url).content, 'utf-8')

s = requests.Session()

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

# def get_phone_number(u_div, pt_):
#     phone_id_li = str(u_div.ul.li)
#     phone_id = re.search(r"'id':'(\w+)'", phone_id_li).group(1)  
    
#     headers = {
#         'accept': '*/*',
#         'accept-encoding': 'gzip, deflate, br',
#         'accept-language': 'uk,en-US;q=0.9,en;q=0.8',
#         'sec-fetch-dest': 'empty',
#         'sec-fetch-mode': 'cors',
#         'sec-fetch-site': 'same-origin',
#         'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36',
#         'x-requested-with': 'XMLHttpRequest'
#     }
#     response = requests.get(f'https://www.olx.ua/uk/ajax/misc/contact/phone/{phone_id}/?pt={pt_}', headers=headers)
#     # print(dict(response.request.headers).get('pt'))
#     print(response.url)
#     return response.json().get('value')
    
def get_info(url):
    html = s.get(url)
    soup: BeautifulSoup = get_soup(html.text, 'lxml')    
    info = {}
    
    title_box = soup.find('div', class_='offer-titlebox')
    user_div = soup.find('div', class_='fblock fblock--details clr')
    
    offer_id = soup.find('div', id='offerbottombar', class_='offer-bottombar')  \
                    .find_all('li', class_='offer-bottombar__item')             \
                    [-1]                                                        \
                    .strong                                                     \
                    .text
    author = user_div.find('div', class_='quickcontact__user-name').text
    # phone_number = get_phone_number(user_div, pt)
    title = title_box.h1.text.strip()
    description = soup.find('div', class_='clr lheight20 large', id='textContent').text.strip()
    try:
        price = title_box.find('strong', class_='pricelabel__value').text.strip()
    except:
        price = None
        
    if offer_id:
        info['offer_id'] = offer_id
    if author:
        info['author'] = author
    if title:
        info['title'] = title
    if price: 
        info['price'] = price
    if description:
        info['description'] = description
    return info

def export_all_to_csv(filename):
    """Exports everything from mongodb to .csv file <filename>"""
    with open(filename, 'w', encoding='utf-8') as f:
        writer = csv.writer(f, delimiter=',', quoting=csv.QUOTE_MINIMAL, quotechar='"')
        writer.writerow(['Offer_id', 'Author', 'Title', 'Price', 'Description'])
        
        all_offers = OLXOffer.objects.all()
        for offer in all_offers:
            writer.writerow([
                offer.offer_id.strip().replace('\n', '').replace('\r', ''), 
                offer.author.strip().replace('\n', '').replace('\r', ''), 
                offer.title.strip().replace('\n', '').replace('\r', ''), 
                offer.price.strip().replace('\n', '').replace('\r', ''), 
                offer.description.strip().replace('\n', '').replace('\r', '')
            ])
        
pages_urls = get_urls(url)
connect_to_mongo()



for page_url in pages_urls:                   #
    offers_urls = get_offers_urls(page_url)   #
    for offer_url in offers_urls:             #
        info = get_info(offer_url)            #   grabs info from all offer urls
        try:                                  #           which fit your
            offer = OLXOffer(**info)          #    
            offer.save()                      #
        except:                               #
            pass                              #

"""the commented code below takes a random offer url and gets info from it"""
# from random import choice
# get_info_url = choice(
#     get_offers_urls(
#         choice(
#             get_urls(url)
#         )
#     )
# )
# info = get_info(get_info_url)
# try:
#     offer = OLXOffer(**info)
#     offer.save()
# except:
#     pass


export_to_csv = True if input('Export data to csv file too?[y/n]').strip() == 'y' else False
if export_to_csv:
    export_all_to_csv('offers.csv')