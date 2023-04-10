.PHONY: clean

all:
		mkdir -p build
			pdflatex -output-directory=build report.tex

watch:
		ls *.tex | entr -r make

clean:
		rm -r build
