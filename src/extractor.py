import requests
from bs4 import BeautifulSoup
from bs4.element import NavigableString, Tag


class Extractor:

    @classmethod
    def extract_text_from_tag(cls, tag: Tag) -> str:
        assert isinstance(tag, Tag), 'extract_text_from_tag() could only be used on Tags'
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
                flag = False
                for child in div.children:
                    if child.name == 'h2':
                        if flag:
                            return res
                        else:
                            flag = True
                    elif child.name == 'p' and flag:
                        for descendant in child.descendants:
                            if isinstance(descendant, NavigableString):
                                res += descendant
                            else:
                                res += cls.extract_text_from_tag(descendant)
                        res += '\n'
        return 'EXTRACTION ERROR: DID NOT FIND SECOND H2 TAG'
