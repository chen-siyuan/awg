"""
Write the Markdown file
"""


class FileWriter:

    @classmethod
    def write_file(cls, filename: str, content: str):
        with open(filename, 'w') as f:
            f.write(content)
