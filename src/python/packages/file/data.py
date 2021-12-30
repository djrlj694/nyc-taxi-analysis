#!/usr/bin/env python3
"""
data.py - A module defining an abstract base class (`DataFile`) for loading
an object to a Pandas DataFrame
"""
from abc import ABC
from dataclasses import dataclass

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
class DataFile(ABC):
    """
    An abstract class representing a DataFrame-loadable object.
    """

    # -- Input Methods -- #

    def to_df(self, *args, **kwargs) -> pd.DataFrame:
        """
        The DataFrame representation of a data file object.

        Returns
        -------
        `pd.DataFrame`
            The DataFrame representation.
         """

        # Return the DataFrame.
        pass
