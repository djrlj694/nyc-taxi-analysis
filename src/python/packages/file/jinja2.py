#!/usr/bin/env python3
"""
jinja2.py - A module defining a class (`Jinja2File`) for reading a Jinja2
template file (`*.jinja2`).
"""
from typing import Any
from typing import Callable

from jinja2 import Template

from .file import File


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


class Jinja2File(File):
    """
    An object class representing a Jinja2 template file.

    Parameters
    ----------
    `path` : `str`
        The file's pathname.

    Returns
    -------
    `Jinja2File`
        An instantiated `Jinja2File` object.
    """

    # -- Getter Methods -- #

    @property
    def template(self) -> Template:
        """
        The getter of the `Jinja2File` class property `template`.

        Returns
        -------
        `Template`
            A Jinja2 template.
        """

        # Check if the file exists.
        super().open(mode='r')

        # Return a Jinja2 template.
        return Template(self.raw)

    # -- Output Methods -- #

    def load(self, transform: Callable = None, *args, **kwargs) -> Any:
        """
        Renders the template file as a Unicode string, then either returns the
        string itself or a Python object source by the string.

        Returns
        -------
        `Any`
            The unicode string or the Python object sourced by it.
        """

        # Return the Unicode string.
        u_str = self.template.render(*args, **kwargs)
        if transform is None:
            return u_str
        # ...or another Python object sourced by the string.
        else:
            return transform(u_str)
