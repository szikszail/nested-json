#!/bin/bash

echo "1) Cleaning"
rm -fr ./build
rm -fr ./dist
rm -fr ./*.egg-info

echo "2) Flake"
python -m flake8 nested_json

echo "3) Testing"
python -m pytest

echo "4) Building"
python -m build

echo "5) Publishing"
python -m twine upload --repository testpypi dist/*