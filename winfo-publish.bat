rem THIS SCRIPT IS ONLY USED FOR MAKING THE PROCESS OF PUBLISHING PACKAGES FASTER (PLEASE IGNORE!)

setup.py sdist bdist_wheel
twine upload dist/* --verbose