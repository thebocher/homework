from typing import List
from urllib.parse import quote

from constants import BASE_URL, PLACEHOLDER, SEARCH_PATTERN



def get_url() -> str:
    """Get url for search"""
    query = input('Your query: ')
    return prepare_url(query)


def prepare_url(query: str) -> str:
    """Preparing url"""

    query = query.replace(' ', '-')
    query = quote(query)
    url = BASE_URL.replace(PLACEHOLDER, query)

    return url

def prepare_urls(url: str, pattern: str, count: int) -> List[str]:
    """Preparing pagination pages"""
    if not count:
        return []
    return [f'{url}{pattern}{page}' for page in range(1, count+1)]

if __name__ == "__main__":
    assert prepare_url('macbook') == prepare_url('macbook')
    assert prepare_url('?') == prepare_url('?')
    
    assert prepare_urls(prepare_url('macbook'), SEARCH_PATTERN, 0) == []