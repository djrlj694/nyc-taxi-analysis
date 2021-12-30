#!/usr/bin/env python3
"""
markdown.py - A module defining a class (`MarkdownFile`) for reading a
Markdown file (`*.md`).
"""
from markdown import markdown

from .jinja2 import Jinja2File


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


class MarkdownFile(Jinja2File):
    """
    An object class representing a Markdown file.

    Parameters
    ----------
    `path` : `str`
        The file's pathname.

    Returns
    -------
    `MarkdownFile`
        An instantiated `MarkdownFile` object.
    """

    # -- Output Methods -- #

    def to_html(self, *args, **kwargs) -> str:
        """
        Loads HTML representation of the (rendered) Markdown file.

        Returns
        -------
        `str`
            The HTML content.
        """

        # Define an inner function to convert Markdown to HTML.
        def html(md_str: str) -> str:
            extensions = [
                'markdown.extensions.extra',
                'markdown.extensions.smarty',
                'markdown.extensions.tables',
            ]
            html_str = markdown(
                md_str,
                extensions=extensions,
                output_format='html5',
            )
            return html_str

        # Return the HTML.
        return super().load(html, *args, **kwargs)
