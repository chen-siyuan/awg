from generator import Generator as generator
from extractor import Extractor as extractor
from filewriter import FileWriter as filewriter


def get_problem(exam: str, year: int, problem: int) -> str:
    return extractor.extract_text_with_latex(extractor.extract_paragraph(
        generator.generate_url(exam, year, problem)))


def main():
    filewriter.write_file('output/test.md', get_problem('AMC_12A', 2003, 30))


if __name__ == '__main__':
    main()
