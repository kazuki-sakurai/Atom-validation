#!/bin/sh

rm tex/CF_table.tex 
python write_table.py $@ && cd tex && pdflatex CF_table.tex && open CF_table.pdf
