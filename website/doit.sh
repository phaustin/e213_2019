#!/bin/bash -v
sphinx-build -v -N -b html .  _build
mkdir -p _build/pdfs
rsync -av pdfs/* _build/pdfs/.
