#!/usr/bin/env sh

rm -rf ./build

cp -r ./src ./build

cd ./build

## Compile LaTeX to pdf
pdflatex thesis.tex
bibtex thesis
pdflatex thesis.tex
pdflatex thesis.tex

mv thesis.pdf ../

## Create web version
latex2html -mkdir -dir ../docs thesis.tex

cd ..
rm -rf ./build