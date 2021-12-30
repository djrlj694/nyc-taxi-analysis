#!/usr/bin/env python3
"""
csv.py - A module defining a class (`File`) for reading a delimited data file
(e.g. `*.csv`)
"""
import csv
from collections.abc import Iterator
from dataclasses import dataclass

import pandas as pd

from .data import DataFile
from .delimited import DelimitedFile
from .file import File


# =========================================================================== #
# METADATA
# =========================================================================== #


__author__ = 'Robert (Bob) L. Jones'
__credits__ = ['Robert (Bob) L. Jones']

__created_date__ = 'Dec 29, 2021'
__modified_date__ = 'Dec 29, 2021'


# =========================================================================== #
# CLASSES
# =========================================================================== #


@dataclass
class CSVFile(DataFile, DelimitedFile, File):
    """
    An object class representing a CSV file.

    Parameters
    ----------
    `path` : `str`
        The file's pathname.

    `delimiter` : `str`
        The file's field delimiter.

    Returns
    -------
    `CSVFile`
        An instantiated `CSVFile` object.
    """

    # -- Instance Attributes -- #

    delimiter: str = ','

    # -- Output Methods -- #

    def __iter__(self) -> Iterator:
        """
        The iterator representation of a CSV file.

        Returns
        -------
        `Iterator`
            The iterator representation.
        """

        # Check if the file exists.
        self.open(mode='r')

        # Set an empty list for storing the file's lines of content.
        records = []

        # Read and parse the CSV file, or fail and exit the program.
        try:
            with open(self.path) as fid:
                reader = csv.reader(fid, delimiter=self.delimiter)
                records = list(reader)
        except Exception as e:
            exit(e)

        # Yield the iterator representation.
        yield from records

    def to_df(self, *args, **kwargs) -> pd.DataFrame:
        """
        Loads a DataFrame representation of the CSV file.

        Returns
        -------
        `Iterator`
            The DataFrame representation.
        """

        # Return the DataFrame.
        return pd.read_csv(self.path, sep=self.delimiter, *args, **kwargs)
