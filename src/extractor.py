import requests
from bs4 import BeautifulSoup
from bs4.element import NavigableString, Tag


class Extractor:

    @classmethod
    def extract_text(cls, tag: Tag) -> str:
        assert isinstance(tag, Tag), 'extract_text() could only be used on Tags'
        if tag.name == 'i':
            return ''  # For some reason, <i> tags' texts are reproduced by a later navigable string
        if tag.name == 'img':
            return tag['alt']
        return 'WARNING: EXTRACTING_TEXT_FROM_UNKNOWN_TYPE_TAGS'

    @classmethod
    def extract_question(cls, url: str) -> str:
        res = ''
        soup = BeautifulSoup(requests.get(url).content, 'html.parser')
        for div in soup.find_all('div'):
            if div.has_attr('class') and div['class'][0] == 'mw-parser-output':
                for descendant in div.p.descendants:
                    if isinstance(descendant, NavigableString):
                        res += descendant
                    else:
                        res += cls.extract_text(descendant)
        return res
