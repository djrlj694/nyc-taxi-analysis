#!/usr/bin/env python3
"""
yaml.py - A module defining a class (`YAMLFile`) for reading a YAML file
(`*.yaml`).
"""
from typing import Any

import yaml

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


class YAMLFile(Jinja2File):
    """
    An object class representing a YAML file.

    Parameters
    ----------
    `path` : `str`
        The file's pathname.

    Returns
    -------
    `YAMLFile`
        An instantiated `YAMLFile` object.
    """

    # -- Output Methods -- #

    def load(self, *args, **kwargs) -> Any:
        """
        Renders the template file as a Unicode string, then parses the first
        YAML document in the string & produces a corresponding Python object.

        Returns
        -------
        `Any`
            The Python object.
        """

        # Return the dictionary.
        return super().load(yaml.load, *args, **kwargs)
