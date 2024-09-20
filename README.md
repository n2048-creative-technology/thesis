# thesis

The thesis is written in [LaTeX](https://www.tug.org/texlive/quickinstall.html)

Install LaTex
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

install the compiler (if not installed)
```
sudo apt install pdflatex
```

Compile the LaTeX documents to a PDF using the following commands: 
```
bibtex thesis
pdflatex thesis.tex 
``` 
