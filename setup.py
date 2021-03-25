#-*- encoding: utf-8 -*-

import os
import io

from setuptools import find_packages, setup


if os.path.exists("requirements.txt"):
    with open("README.md", "r", encoding='UTF-8') as fh:
        long_description = fh.read()
else:
    long_description = ""

if os.path.exists("requirements.txt"):
    with open("requirements.txt", "r", encoding='UTF-8') as fh:
        install_requires = fh.read().split("\n")
else:
    install_requires = []


setup(
    name="soc-excel-convert",
    version="1.0.1",
    author="Tree",
    author_email="tree@ejyi.com",
    description="Convert Excel to markdown ....",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/treeyh/soc-excel-convert",
    keywords=["soc", "excel", "convert", "markdown"],
    # packages=['src'],
    package_dir={"": "src"},
    packages=find_packages(
        where="src",
        exclude=["docs"],
    ),
    license='Apache License 2.0',
    classifiers=[
        "Programming Language :: Python :: 3",
        'License :: OSI Approved :: Apache Software License',
        "Operating System :: OS Independent",
    ],

    entry_points={
        "console_scripts": [
            "soc-excel-convert=soc_excel_convert._internal:main",
        ],
    },

    install_requires=install_requires,
    zip_safe=False,
    python_requires='>=3',
)