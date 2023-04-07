from setuptools import setup, find_packages

# Setting up
setup(
    name="Winfo",
    version="0.0.1",
    author="BLUEAMETHYST Studios",
    author_email="simon.schoeneberg@t-online.de",
    description="Get information about your windows system",
    packages=find_packages(),
    keywords=['python', 'windows', 'util', 'information', 'system'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Microsoft :: Windows",
    ]
)