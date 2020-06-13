"""
Generate url used by the Extractor
"""


class Generator:

    exams = {'AMC_8',
             'AMC_10', 'AMC_10A', 'AMC_10B',
             'AMC_12', 'AMC_12A', 'AMC_12B',
             'AIME', 'AIME_I', 'AIME_II'}


    @classmethod
    def validate_input(cls, exam: str, year: int, problem: int) -> None:
        assert exam in cls.exams, '"{}" is an invalid exam'.format(exam)

        if exam == 'AMC_8':
            assert 1999 <= year <= 2019, '"{}" is an invalid year for "{}"'.format(year, exam)
        elif exam in {'AMC_10', 'AMC_12'}:
            assert 2000 <= year <= 2001, '"{}" is an invalid year for "{}"'.format(year, exam)
        elif exam in {'AMC_10A', 'AMC_10B', 'AMC_12A', 'AMC_12B'}:
            assert 2002 <= year <= 2020, '"{}" is an invalid year for "{}"'.format(year, exam)
        elif exam == 'AIME':
            assert 1983 <= year <= 1999, '"{}" is an invalid year for "{}"'.format(year, exam)
        elif exam in {'AIME_I', 'AIME_II'}:
            assert 2000 <= year <= 2020, '"{}" is an invalid year for "{}"'.format(year, exam)

        if exam in {'AIME', 'AIME_I', 'AIME_II'}:
            assert 1 <= problem <= 15, '"{}" is an invalid problem for "{}"'.format(problem, exam)
        else:
            assert 1 <= problem <= 25, '"{}" is an invalid problem for "{}"'.format(problem, exam)


    @classmethod
    def generate_url(cls, exam: str, year: int, problem: int) -> str:
        cls.validate_input(exam, year, problem)
        head = 'https://artofproblemsolving.com/wiki/index.php/'
        tail = '{0}_{1}_Problems/Problem_{2}'.format(year, exam, problem)
        return head + tail
