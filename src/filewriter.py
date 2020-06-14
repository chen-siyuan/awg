from pdflatex import PDFLaTeX
from pylatex import Document, Section, Command
from pylatex.utils import NoEscape


class Filewriter:

    @classmethod
    def prep_file(cls, filename: str, header: str = ''):
        with open(filename, 'w') as output:
            output.write(header)

    @classmethod
    def write_file(cls, filename: str, content: str, mode: str = 'w'):
        with open(filename, mode) as output:
            output.write(content)

    @classmethod
    def write_pdf_from_tex(cls, tex_filename: str, pdf_filename: str = None):

        assert tex_filename.endswith('.tex'), '"{}" is not a valid .tex file name'.format(tex_filename)

        if pdf_filename is None:
            pdf_filename = tex_filename[:-4]
        if pdf_filename[0] == '/':
            pdf_filename = pdf_filename[1:]
        if pdf_filename.endswith('.pdf'):
            pdf_filename = pdf_filename[:-4]

        pdfl = PDFLaTeX.from_texfile(tex_filename)
        pdfl.set_jobname(pdf_filename)
        pdfl.create_pdf(keep_pdf_file=True)


'''doc = Document('test')
doc.preamble.append(Command('title', 'TITLE'))
doc.preamble.append(Command('author', 'Daniel Chen'))
doc.preamble.append(Command('date', r'\today'))
doc.generate_tex()
'''
Filewriter.write_pdf_from_tex('test.tex', 'test3.pdf')
