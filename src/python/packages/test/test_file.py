#!/usr/bin/env python3
"""
test_file.py - A module for testing the `file` package.
"""
import os
import unittest
from pathlib import Path

from file import CSVFile
from file import File
from file import Jinja2File


# =========================================================================== #
# METADATA
# =========================================================================== #

__author__ = 'Robert (Bob) L. Jones'
__credits__ = ['Robert (Bob) L. Jones']

__created_date__ = 'Dec 29, 2021'
__modified_date__ = 'Dec 29, 2021'


# =========================================================================== #
# CONSTANTS
# =========================================================================== #


# -- Filesystem -- #

PREFIX = Path(
    os.getenv('PREFIX', default='.'),
).resolve()

ETC_DIR = PREFIX / 'etc'

PLAIN_FILE = ETC_DIR / 'content' / 'sample_email_body.txt'
TEMPLATE_FILE = ETC_DIR / 'content' / 'sample_email_body.md.jinja2'

CSV_FILE = ETC_DIR / 'data' / 'sample_3x3_data.csv'


# =========================================================================== #
# CLASSES
# =========================================================================== #


class TestFile(unittest.TestCase):

    def test_File(self):
        """
        Test the `File` class.
        """

        # Instantiate objects to be tested.
        file = File(PLAIN_FILE)

        # Set assertion test cases.
        actual = list(file)[0]
        expected = 'Hello!'

        # Test assertions.
        self.assertEqual(actual, expected)

    def test_CSVFile(self):
        """
        Test the `CSVFile` class.
        """

        # Instantiate objects to be tested.
        file = CSVFile(CSV_FILE, delimiter='|')

        # Set assertion test cases.
        actual = list(file)[0]
        expected = ['Col_A', 'Col_B', 'Col_C']

        # Test assertions.
        self.assertEqual(actual, expected)

    def test_Jinja2File(self):
        """
        Test the `Jinja2File` class.
        """

        # Instantiate objects to be tested.
        file = Jinja2File(TEMPLATE_FILE)

        # Set assertion test cases.
        actual = file.template.render().split('\n')[0]
        expected = 'Hello again, !'

        # Test assertions.
        self.assertEqual(actual, expected)


# =========================================================================== #
# MAIN EXECUTION
# =========================================================================== #


# -- Main Execution -- #

# If this module is in the main module, call the main() function.
if __name__ == '__main__':
    unittest.main()
