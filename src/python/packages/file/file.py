#!/usr/bin/env python3
"""
file.py - A module defining a class (`File`) for reading a text file.
"""
import os
import sys
from collections.abc import Iterator
from dataclasses import dataclass
from pathlib import Path


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
class File():
    """
    An object class representing a text file.

    Parameters
    ----------
    `path` : `Path`
        The file's pathname.

    Returns
    -------
    `File`
        An instantiated `File` object.
    """

    # -- Instance Attributes -- #

    path: Path

    # -- Constructor Methods -- #

    def __post_init__(self):
        self.path = Path(str(self))

    # -- Getter Methods -- #

    @property
    def raw(self) -> str:
        """
        The getter of the `File` class property `raw`.
        """

        # Check if the file exists.
        self.open(mode='r')

        # Return the file's raw text content.
        return self.path.read_text()

    # -- Output Methods -- #

    def __iter__(self) -> Iterator:
        """
        The iterator representation of a file.

        Returns
        -------
        `Iterator`
            The iterator representation.
        """

        # Check if the file exists.
        self.open(mode='r')

        # Set an empty list for storing the file's lines of content.
        lines = []

        # Read the file's content, or fail and exit the program.
        try:
            with open(self.path) as fid:
                lines = [line.rstrip('\n') for line in fid]
        except Exception as e:
            exit(e)

        # Yield the iterator representation.
        yield from lines

    def __str__(self) -> str:
        """
        The string representation of a file.

        Returns
        -------
        `str`
            The string representation.
        """

        # Compute a normalized (i.e, full) version of the pathname w/ all
        # environment variables embedded in it expanded (i.e., replaced w/ the
        # value each variable represents).
        path = str(self.path)
        expandedpath = os.path.expandvars(path)
        abspath = os.path.abspath(expandedpath)

        # Return the string representation.
        return abspath

    # -- Helper Methods -- #

    @staticmethod
    def exit(e: Exception):
        """
        Prints an exception and exits.
        """

        print(f'{type(e).__name__}:', e)
        sys.exit(1)

    def open(self, mode: str = 'r'):
        """
        Exits if a file or its parent directory can't be opened.
        """

        # Set the path to test.
        path = Path(str(self))
        if mode == 'w':
            path = path.parent

        # Read the file's content, or fail and exit the program.
        try:
            path.resolve(strict=True)
        except FileNotFoundError as e:
            exit(e)
        except OSError as e:
            exit(e)
        except Exception as e:
            exit(e)
