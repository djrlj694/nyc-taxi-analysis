#!/usr/bin/env python3
"""
delimited.py - A module defining an abstract base class (`DelimitedFile`) for
loading an object to a Pandas DataFrame
"""
from abc import ABC
from dataclasses import dataclass


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
class DelimitedFile(ABC):
    """
    An abstract class representing a delimited file object.
    """

    # -- Instance Attributes -- #

    delimiter: str
