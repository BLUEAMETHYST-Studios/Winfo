rem THIS SCRIPT IS ONLY USED FOR MAKING THE PROCESS OF PUBLISHING PACKAGES FASTER (PLEASE IGNORE!)
@echo off

setup.py sdist bdist_wheel
twine upload dist/* --verbose