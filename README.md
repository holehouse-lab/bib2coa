bib2coa
==============================



A command-line tool that converts a single bibtex file to a tsv with paper, author that can be used as the foundation for an NSF COA form.

## Install

To install [current stable version from PyPI](https://pypi.org/project/bib2coa/)


	pip install bib2coa

To install source clone this repository or download the zip file and unzip and run

	pip install .
	
From within the source dir tree (where `setup.py` is).

## Usage
To build a tab-separated file (TSV) from a bibtex file run

	bib2coa <filename>
	
This creates an outputfile called `coa_initial.tsv` which has two tab-separated columns. Unique authors (col 1) and the paper they come from with the paper year. 

To see stats on the conversion include `--stats` flag. 

To output a file with a different name add the `--output my_file.tsv` (for example).
		
