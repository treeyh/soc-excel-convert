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
    keywords=["soc", "excel", "convert", "markdown"],
    # packages=['src'],
    package_dir={"": "src"},
    packages=find_packages(
        where="src",
        exclude=["docs"],
    ),
    license="Apache License Version 2.0",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: Apache License Version 2.0",
        "Operating System :: OS Independent",
    ],

    entry_points={
        "console_scripts": [
            "soc-excel-convert=soc-excel-convert._internal:main",
        ],
    },

    install_requires=['et-xmlfile>=1.0.1', 'jdcal>=1.4.1', 'openpyxl>=2.6.2'],
    zip_safe=False,
    python_requires='>=3',
)