#-*- encoding: utf-8 -*-

from setuptools import find_packages, setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="soc-excel-convert",
    version="0.1.0",
    author="Tree",
    author_email="tree@ejyi.com",
    description="Convert Excel to markdown ....",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/treeyh/soc-excel-convert",
    keywords="soc excel convert markdown json ",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: Apache License Version 2.0",
        "Operating System :: OS Independent",
    ],

    zip_safe=False,
    python_requires='>=3.0,!=3.0.*,!=3.1.*,!=3.2.*,!=3.3.*,!=3.4.*',
)