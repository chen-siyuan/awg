from generator import Generator as generator
from extractor import Extractor as extractor
from filewriter import FileWriter as filewriter


def get_problem(exam: str, year: int, problem: int) -> str:
    return extractor.extract_text_with_latex(extractor.extract_paragraph(
        generator.generate_url(exam, year, problem)))


def main():
    for i in range(15):
        filewriter.write_file('output/test.md', get_problem('AIME_II', 2020, i + 1) + '\n', mode='a')


if __name__ == '__main__':
    main()
