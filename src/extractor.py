"""
Extract content from url
"""


import requests
from bs4 import BeautifulSoup
from bs4.element import NavigableString


class Extractor:

    @classmethod
    def extract_question(cls, url: str) -> str:
        res = ''
        soup = BeautifulSoup(requests.get(url).content, 'html.parser')
        for div in soup.find_all('div'):
            if div.has_attr('class') and div['class'][0] == 'mw-parser-output':
                for descendant in div.p.descendants:
                    res += descendant if isinstance(descendant, NavigableString) else descendant['alt']
        return res
