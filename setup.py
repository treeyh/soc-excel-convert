import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="soc-excel-convert",
    version="0.1.0",
    author="Tree",
    author_email="tree@ejyi.com",
    description="Convert Excel to markdown ....",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/treeyh/soc-excel-convert",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: Apache License Version 2.0",
        "Operating System :: OS Independent",
    ],
)