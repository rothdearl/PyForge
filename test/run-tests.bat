@echo off

:: Install required packages.
pip3 install coverage --upgrade --user %*

rem python -m unittest discover -t ../ "test" -q
coverage run -m unittest discover -t ../ "test" -q
coverage report -m
coverage html
