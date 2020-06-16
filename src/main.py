from generator import Generator
from extractor import Extractor
from filewriter import Filewriter


def get_problem(exam: str, year: int, problem: int, description: bool = False) -> str:
    return (('[\\textbf{{{} {} P{}}}] '.format(year, exam.replace('_', ' '), problem) if description else '')
            + Extractor.extract_question(Generator.generate_url(exam, year, problem)))


def main():
    filewriter = Filewriter('output/2018_AIME_II')

    filewriter.initialize_doc('2018 AIME II Problems', 'MAA')
    for i in range(15):
        filewriter.add_problem_to_section(get_problem('AIME_II', 2018, i + 1, description=True))
        print('Problem {} successfully added to tex file'.format(i + 1))
    filewriter.add_section('Problems')
    filewriter.write_tex()

    Filewriter.write_pdf_from_tex('output/2018_AIME_II.tex')


if __name__ == '__main__':
    main()
