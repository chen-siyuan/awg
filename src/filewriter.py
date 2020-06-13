"""
Write the Markdown file
"""


class FileWriter:

    @classmethod
    def write_file(cls, filename: str, content: str, mode:str='w'):
        with open(filename, mode) as f:
            f.write(content)
