# -*- coding: utf-8 -*-

from setuptools import setup, find_packages
import codecs
import os
    
VERSION = '0.0.1'
DESCRIPTION = 'SciModelStats class code for course use only'

# Setting up
setup(
    name="scimodel",
    version=VERSION,
    author="SciModel.dev (Yahya Khawam)",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    packages=find_packages(),
    install_requires=['numpy', 'pandas', 'scipy', 'torch', 'python-math', 'statsmodels', 'seaborn']
)
