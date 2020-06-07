"""
Created on Sun May 31 17:55:42 2020.

@author: Tocivlasok
"""

import setuptools


with open("README.md", "r") as fh:
    long_description = fh.read()


setuptools.setup(
    name="mechanictocivlasok",
    version="0.0.3",
    packages=setuptools.find_packages(),
    
    # metadata
    author="Simona Korkobcova",
    author_email="simona.korkobcova@gmail.com",
    description="git directory: mechanic-aminations-BA",
    long_description=long_description,
    url="https://github.com/Tocivlasok/mechanic-animation-BA.git",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)


