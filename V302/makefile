all: V.pdf

V.pdf: V.bcf

V.bcf: V.tex
	lualatex V.tex
	biber V.bcf
	lualatex V.tex
	
