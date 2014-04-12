#!/bin/bash

vname=$1

python $vname.py && pdflatex $vname.tex && open $vname.pdf
