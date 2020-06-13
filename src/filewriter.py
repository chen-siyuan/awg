"""
Write the Markdown file
"""


class Filewriter:

    @classmethod
    def prep_file(cls, filename: str, header: str = ''):
        with open(filename, 'w') as output:
            output.write(header)

    @classmethod
    def write_file(cls, filename: str, content: str, mode: str = 'w'):
        with open(filename, mode) as output:
            output.write(content)
