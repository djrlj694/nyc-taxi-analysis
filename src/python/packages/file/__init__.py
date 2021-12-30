#!/usr/bin/env python3
"""
__init__.py - The top-level Python module for the `file` package.
"""
from .csv import CSVFile
from .data import DataFile
from .delimited import DelimitedFile
from .file import File
from .jinja2 import Jinja2File
from .markdown import MarkdownFile
from .sqlite import SQLiteFile
from .yaml import YAMLFile


# =========================================================================== #
# METADATA
# =========================================================================== #


__author__ = 'Robert (Bob) L. Jones'
__credits__ = ['Robert (Bob) L. Jones']

__created_date__ = 'Dec 29, 2021'
__modified_date__ = 'Dec 29, 2021'


# =========================================================================== #
# EXPORTS
# =========================================================================== #


__all__ = [
    'CSVFile',
    'DataFile',
    'DelimitedFile',
    'File',
    'Jinja2File',
    'MarkdownFile',
    'SQLiteFile',
    'YAMLFile',
]
