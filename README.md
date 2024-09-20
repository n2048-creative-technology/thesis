# thesis

The thesis is written in [LaTeX](https://www.tug.org/texlive/quickinstall.html) and managed as code.

## File structure

* [README.md](README.md) - This file
* [thesis.pdf](thesis.pdf) - This thesis compiled as a pdf document
* [thesis.tex](src/thesis.tex) - Document structure and configuration
* [references.bib](src/references.bib) - References and bibliography
* [introduction.tex](src/introduction.tex) - Introduction
* [chapter01.tex](src/chapte01.tex) - Chapter 1
* [create.sh](create.sh) - Compilation script
* [deploy.yml](.github/workflows/deploy.yml) - Automatic deployment settings

## Automated deployment 

Every time the repository is updated, the contents of the docs folder (website version of this thesis) will be exported to 
[this link](https://n2048-creative-technology.github.io/thesis/)

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