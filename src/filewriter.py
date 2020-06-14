from pdflatex import PDFLaTeX


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
    def write_pdf_from_tex(cls, tex_filename: str, latex_filename: str = None):
        pdfl = PDFLaTeX.from_texfile(tex_filename)
        if latex_filename:
            pdfl.set_jobname(latex_filename)
        pdfl.create_pdf(keep_pdf_file=True)
