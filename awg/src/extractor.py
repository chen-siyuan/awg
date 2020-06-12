"""
Extract content from url
"""


import requests
from lxml import html


class Extractor:

    @classmethod
    def extract_text_with_latex(cls, paragraph: html.Element) -> str:

        text = paragraph.text_content()
        print(text)
        expressions = list(map(lambda img: img.attrib['alt'],
                               paragraph.getchildren()))

        i = 0
        while i < len(text):
            if text[i] == ' ' and text[i + 1] in {
                    ' ', '.', ',', '?', '\xa0', '\n'}:
                text = text[:i + 1] + expressions.pop(0) + text[i + 1:]
            i += 1

        return text.rstrip()

    @classmethod
    def extract_paragraph(cls, url: str) -> html.Element:

        page = requests.get(url)
        tree = html.fromstring(page.text)

        paragraphs = tree.xpath('//p')
        i = 0

        while i + 1 < len(paragraphs) and paragraphs[i].text_content().find('the') == -1:
            i += 1

        return paragraphs[i]
