# AMC Worksheet Generator

AWG generates worksheets consisting of problems from [past AMC exams](https://artofproblemsolving.com/wiki/index.php/AMC_Problems_and_Solutions) for **personal practice** purposes. It uses [Requests](https://requests.readthedocs.io/en/master/) and [BeautifulSoup4](https://www.crummy.com/software/BeautifulSoup/bs4/doc/) to extract individual problems (text with formulas and diagrams) from [AOPS](https://artofproblemsolving.com/wiki/index.php/AMC_Problems_and_Solutions). It then writes the problems into a LaTeX file and exports it to a PDF using [PyLaTeX](https://jeltef.github.io/PyLaTeX/current/).

## Acknowledgement

All problems are copyrighted by the [Mathematical Association of America](https://www.maa.org/)'s [American Mathematics Competitions](https://www.maa.org/math-competitions). This project would not be possible without [Overleaf](https://www.overleaf.com/).

## Features

- Automatically extracts problems and generates tex and pdf files
- Supports both inline and displayed formulas
- Supports multiple choice problems
- Supports unlimited number of problems within one worksheet
- Generates randomized worksheets (**to be added**)

## Screenshots

![Code](assets/example_code.png)
![Output](assets/example_pdf.png?)

## Supported Exams

|AMC 8|AMC 10|AMC 12|AIME|
|:---:|:---:|:---:|:---:|
|AMC_8|AMC 10|AMC 12|AIME|
||AMC 10A|AMC 12A|AIME I|
||AMC 10B|AMC 12B|AIME II|

## Formula Substitutions

AWG automatically substitutes some of the latex commands extracted from the html file to better accommodate the standards of PyLaTeX. Those substitutions are listed below:

- '\tfrac' to '\frac'
- '•' to '$\cdot$'
- '$$' to '$\$
