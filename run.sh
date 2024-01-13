#!/bin/bash

cd docs

cd 2th_sem
mkdocs build
cd ..

cd 4th_sem
mkdocs build
cd ..

cd ..
mkdocs build
mkdocs serve