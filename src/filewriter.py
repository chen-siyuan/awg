from pdflatex import PDFLaTeX
from pylatex import Document, Section, Subsection, Command, Enumerate, NoEscape, Package


class Filewriter:

    unsupported_commands = {r'\tfrac': r'\frac'}

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

    def __init__(self, tex_filename):
        self.doc = Document(tex_filename)
        self.problems = []

    def add_problem_to_section(self, problem: str):
        for unsupported, supported in Filewriter.unsupported_commands.items():
            problem = problem.replace(unsupported, supported)
        self.problems.append(problem)

    def initialize_doc(self, title: str, author: str, with_date: bool = True):

        self.doc.packages.append(Package('amsmath'))  # To enable align
        self.doc.packages.append(Package('hyperref'))  # To enable hyperlink

        self.doc.preamble.append(Command('title', title))
        self.doc.preamble.append(Command('author', author))
        if with_date:
            self.doc.preamble.append(Command('date', NoEscape(r'\today')))
        self.doc.append(NoEscape(r'\maketitle'))

        with self.doc.create(Section('Acknowledgement')):
            self.doc.append(NoEscape(r"All the following problems are copyrighted by the \href{https://www.maa.org/}{Mathematical Association of America}'s \href{https://www.maa.org/math-competitions}{American Mathematics Competitions}."))

    def add_section(self, section_name: str):
        with self.doc.create(Section(section_name)):
            with self.doc.create(Enumerate()) as enum:
                for problem in self.problems:
                    enum.add_item(NoEscape(problem))
        self.problems = []

    def write_tex(self):
        self.doc.generate_tex()
