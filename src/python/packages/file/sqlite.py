#!/usr/bin/env python3
"""
sqlite.py - A module defining a class (`SQLiteFile`) for reading a SQLite
database file (`*.sqlite` or `.db`).
"""
import sqlite3
from dataclasses import dataclass
from typing import List

import pandas as pd

from .data import DataFile
from .jinja2 import Jinja2File


# =========================================================================== #
# METADATA
# =========================================================================== #


__author__ = 'Robert (Bob) L. Jones'
__credits__ = ['Robert (Bob) L. Jones']

__created_date__ = 'Dec 28, 2021'
__modified_date__ = 'Dec 28, 2021'


# =========================================================================== #
# CLASSES
# =========================================================================== #


@dataclass
class SQLiteFile(DataFile, Jinja2File):
    """
    An object class representing a SQL file.

    Parameters
    ----------
    `path` : `str`
        The file's pathname.

    Returns
    -------
    `SQLiteFile`
        An instantiated `SQLiteFile` object.
    """

    # -- Getter Methods -- #

    @property
    def columns(self) -> List[str]:
        """
        The getter of the `SQLFile` class property `columns`.
        """

        # Return the query result's columns.
        return [row[0] for row in self.cursor.description]

    @property
    def connection(self) -> sqlite3.Connection:
        """
        The getter of the `SQLiteFile` class property `connection`.
        """

        # Return the database connection.
        return sqlite3.connect(str(self))

    @property
    def cursor(self) -> sqlite3.Cursor:
        """
        The getter of the `SQLiteFile` class property `cursor`.
        """

        # Return the database cursor.
        return self.connection.cursor()

    # -- Output Methods -- #

    def to_df(self, *args, **kwargs) -> pd.DataFrame:
        """
        Loads a DataFrame representation of the (rendered) SQL file.

        Returns
        -------
        `pd.DataFrame`
            The DataFrame.
        """

        # Define an inner function to pass a query result into a DataFrame.
        def query(sql: str) -> pd.DataFrame:
            df = pd.read_sql_query(sql, self.connection)

            self.cursor.execute(sql)
            df = pd.DataFrame(self.cursor.fetchall())
            df.columns = self.columns
            df.reset_index(drop=True, inplace=True)
            return df

        # Return the DataFrame.
        return super().load(query, *args, **kwargs)
