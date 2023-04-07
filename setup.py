from setuptools import setup, find_packages

with open("README.md", "r") as f:
    readme = f.read()
    f.close()
    
setup(
    name="Winfo",
    version="0.0.1.2",
    author="BLUEAMETHYST Studios",
    author_email="simon.schoeneberg@t-online.de",
    description="Get information about your windows system",
    long_description_content_type="text/markdown",
    long_description=readme,
    packages=find_packages(),
    keywords=['python', 'windows', 'util', 'information', 'system'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Microsoft :: Windows",
    ]
)