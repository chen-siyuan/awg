class Generator:

    exams = {'AMC_8',
             'AMC_10', 'AMC_10A', 'AMC_10B',
             'AMC_12', 'AMC_12A', 'AMC_12B',
             'AIME', 'AIME_I', 'AIME_II'}

    exam_dates = {'AMC_8': (1999, 2020, 25),
                  'AMC_10': (2000, 2002, 25),
                  'AMC_10A': (2002, 2021, 25),
                  'AMC_10B': (2002, 2021, 25),
                  'AMC_12': (2000, 2002, 25),
                  'AMC_12A': (2002, 2021, 25),
                  'AMC_12B': (2002, 2021, 25),
                  'AIME': (1983, 1999, 15),
                  'AIME_I': (2000, 2021, 15),
                  'AIME_II': (2000, 2021, 15)}

    @classmethod
    def validate_input(cls, exam: str, year: int, problem: int) -> None:
        assert isinstance(exam, str)
        assert isinstance(year, int)
        assert isinstance(problem, int)
        assert exam in cls.exam_dates, '"{}" is an invalid exam'.format(exam)
        start_year, end_year, num_problems = cls.exam_dates.get(exam)
        assert start_year <= year < end_year, '"{}" is an invalid year for "{}"'.format(year, exam)
        assert 0 < problem <= num_problems, '"{}" is an invalid problem for "{}"'.format(problem, exam)

    @classmethod
    def generate_url(cls, exam: str, year: int, problem: int) -> str:
        cls.validate_input(exam, year, problem)
        head = 'https://artofproblemsolving.com/wiki/index.php/'
        tail = '{0}_{1}_Problems/Problem_{2}'.format(year, exam, problem)
        return head + tail
