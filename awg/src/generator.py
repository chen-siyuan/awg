"""
Generate url used by the Extractor
"""


class Generator:

    exams = {'AMC_8',
             'AMC_10A', 'AMC_10B',
             'AMC_12A', 'AMC_12B',
             'AIME_I', 'AIME_II'}

    @classmethod
    def generate_url(cls, exam: str, year: int, problem: int) -> str:

        assert exam in cls.exams, '"{}" is an invalid exam'.format(exam)

        head = 'https://artofproblemsolving.com/wiki/index.php/'
        tail = '{0}_{1}_Problems/Problem_{2}'.format(year, exam, problem)
        return head + tail
