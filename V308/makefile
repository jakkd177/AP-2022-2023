all: V308.pdf

V308.pdf: V308.bcf

V308.bcf: V308.tex
	lualatex V308.tex
	biber V308.bcf
	lualatex V308.tex
	
