from generator import Generator
from extractor import Extractor
from filewriter import Filewriter


def get_problem(exam: str, year: int, problem: int) -> str:
    return Extractor.extract_question(Generator.generate_url(exam, year, problem))


def main():
    Filewriter.prep_file('output/test.md')
    for i in range(15):
        Filewriter.write_file('output/test.md', get_problem('AIME_II', 2020, i + 1) + '\n', mode='a')


if __name__ == '__main__':
    main()
