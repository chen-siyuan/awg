from aops.generator import Generator as generator
from aops.extractor import Extractor as extractor
from aops.filewriter import FileWriter as filewriter


def get_problem(exam: str, year: int, problem: int) -> str:
    return extractor.extract_text_with_latex(extractor.extract_paragraph(
        generator.generate_url(exam, year, problem)))


def main():
    print(generator.generate_url('AMC_12A', 2002, 5))
    filewriter.write_file('output/test.md', get_problem('AMC_12A', 2002, 5))


if __name__ == '__main__':
    main()
