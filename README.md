# thesis

The thesis is written in [LaTeX](https://www.tug.org/texlive/quickinstall.html) and managed as code.

## File structure

* [README.md](README.md) - This file
* [thesis.pdf](https://n2048-creative-technology.github.io/thesis/thesis.pdf) - This thesis compiled as a pdf document
* [thesis.tex](src/thesis.tex) - Document structure and configuration
* [thesis.bib](src/thesis.bib) - References and bibliography
* [****CHAPTERS****.tex](src/*.tex) - Text/code for every chapter
* [create.sh](create.sh) - Compilation script
* [latex-pdf.yml](.github/workflows/latex-pdf.yml) - Automatic deployment settings
* [deploy.yml](.github/workflows/deploy.yml) - Automatic deployment settings

## Automated deployment 

Every time the text is updated, the code will be compiled into a PDF and it will be made accessible via 
[this link](https://n2048-creative-technology.github.io/thesis/)

[![READ PDF](https://n2048-creative-technology.github.io/thesis/)](https://n2048-creative-technology.github.io/thesis/)


## Install LaTex
```
curl -L -o install-tl-unx.tar.gz https://mirror.ctan.org/systems/texlive/tlnet/install-tl-unx.tar.gz
zcat < install-tl-unx.tar.gz | tar x
cd install-tl-20240920/
sudo perl install-tl --no-interaction 
```

Edit ~/.bashrc and add these lines at the end: 
```
export MANPATH=/usr/local/texlive/2024/texmf-dist/doc/man:$MANPATH
export INFOPATH=/usr/local/texlive/2024/texmf-dist/doc/info:$INFOPATH
export PATH=/usr/local/texlive/2024/bin/x86_64-linux:$PATH
```

Install the compilers (if not installed)
```
sudo apt install pdflatex
sudo apt-get install latexml
sudo apt-get install pandoc
sudo apt-get install latex2html
```

## Compilation
Compile the LaTeX documents to a PDF using the following commands: 
```
bibtex thesis
pdflatex thesis.tex 
``` 

Aditionally, the thesis is exported as an HTML web page using 
```
latex2html -mkdir -dir docs thesis.tex
```

## Code Repository
The thesis is stored on [Github](https://github.com/n2048-creative-technology/thesis)
