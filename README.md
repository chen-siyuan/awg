# AMC Worksheet Generator

AWG generates worksheets consisting of problems from [past AMC exams](https://artofproblemsolving.com/wiki/index.php/AMC_Problems_and_Solutions) for **personal practice** purposes.

## Mechanism

AWG uses [Requests](https://requests.readthedocs.io/en/master/) and [BeautifulSoup4](https://www.crummy.com/software/BeautifulSoup/bs4/doc/) to extract individual problems (text with formulas and diagrams) from [AOPS](https://artofproblemsolving.com/wiki/index.php/AMC_Problems_and_Solutions). It then writes the problems into a LaTeX file and exports it to a PDF using [PyLaTeX](https://jeltef.github.io/PyLaTeX/current/).

## Supported Exams

|AMC 8|AMC 10|AMC 12|AIME|
|---|---|---|---|
|AMC_8|AMC_10|AMC_12|AIME|
||AMC_10A|AMC_12A|AIME_I|
||AMC_10B|AMC_12B|AIME_II|
