#!/usr/bin/env python3
"""
source.py - A module defining a class (`Source`) for modeling a data source.
"""
from dataclasses import dataclass
from dataclasses import field
from pathlib import Path

import pandas as pd


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
class Source():
    """
    An object class representing a data source.

    Parameters
    ----------
    `filename` : `str`
        The data source's filename (as a format string).
    `dir_path` : `str`
        The data source's path.
    `base_url` : `str`
        The data source's URL.

    Returns
    -------
    `Source`
        An instantiated `Source` object.
    """

    # -- Instance Attributes -- #

    filename: str
    base_url: str
    dir_path: str

    url: str = field(init=False)
    path: str = field(init=False)

    # -- Constructor Methods -- #

    def __post_init__(self):
        self.url = f'{self.base_url}/{self.filename}'
        self.path = str(Path(self.base_url) / self.filename)

    # -- Main Methods -- #

    def extract(self, *args):

        # Render source data metadata from format strings.
        filename = self.filename % args
        url = self.url % args
        path = self.path % args

        # Extract data from remote source.
        print(
            f"Extracting file '{filename}'",
            f"from '{self.base_url}'",
            f"to '{self.dir_path}'...",
            end='',
        )
        if Path(path).is_file():
            # Print status.
            print('skipping.')
        else:
            # Download source data as CSV from an API.
            df = pd.read_csv(url)

            # Save a copy of the extracted data.
            df.to_csv(path, index=False)

            # Print status.
            print('done.')

            # Debug data frame.
            self.preview(df, self.extract.__name__)

    def __str__(self) -> str:
        """
        The string representation of a data source.

        Returns
        -------
        `str`
            The string representation.
        """

        # Return the string representation.
        return self.filename

    # -- Helper Methods -- #

    @staticmethod
    def preview(df: pd.DataFrame, func_name: str):
        print(f'INSIDE {func_name}(): type =', type(df).__name__)
        print(df.head(5))
