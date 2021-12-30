#!/usr/bin/env python3
"""
__main__.py - The main module for processing data and creating visual summaries
for this study.
"""
import os
import sys
from pathlib import Path

import etl
import pandas as pd
import ui.cli as cli


# =========================================================================== #
# METADATA
# =========================================================================== #


__author__ = 'Robert (Bob) L. Jones'
__credits__ = ['Robert (Bob) L. Jones']

__created_date__ = 'Dec 29, 2020'
__modified_date__ = 'Dec 29, 2020'


# =========================================================================== #
# EXPORTS
# =========================================================================== #


# Define the module's API -- the list of exportable objects (classes,
# functions, etc.) -- when performing a "wild import" (`from field import *`).
__all__ = [
    'DEBUG',
]


# =========================================================================== #
# CONSTANTS
# =========================================================================== #


# -- Debugging -- #

DEBUG = bool(os.getenv('DEBUG', default=False))

# -- Filesytem -- #

PREFIX = Path(os.getenv('PREFIX', default='.')).resolve()

DATA_DIR = PREFIX / 'data'
SOURCE_DIR = DATA_DIR / '01_raw'
RESULTS_DIR = PREFIX / 'results'

SOURCE_FILE = '%s_tripdata_%4d-%02d.csv'

# -- URLs -- #

SOURCE_URL = 'https://s3.amazonaws.com/nyc-tlc/trip+data'


# =========================================================================== #
# FUNCTIONS
# =========================================================================== #


# -- Data Analytics -- #

def visualize_data(df: pd.DataFrame):
    pass

    # Debug data frame.
    DEBUG and preview(df, visualize_data.__name__)

    # Return data frame for reuse.
    return df


# -- Data Processing: Extract -- #


def extract_data():

    # Create source.
    source = etl.Source(SOURCE_FILE, SOURCE_URL, SOURCE_DIR)

    # Yellow Taxi trip records
    for year in range(2009, 2021):
        for month in range(1, 13):
            source.extract('yellow', year, month)
    for month in range(1, 8):
        source.extract('yellow', 2021, month)

    # Green Taxi trip records
    for month in range(8, 13):
        source.extract('green', 2013, month)
    for year in range(2014, 2021):
        for month in range(1, 13):
            source.extract('green', year, month)
    for month in range(1, 8):
        source.extract('green', 2021, month)

    # For-Hire Vehicle trip records
    for year in range(2015, 2021):
        for month in range(1, 13):
            source.extract('fhv', year, month)
    for month in range(1, 8):
        source.extract('fhv', 2021, month)

    # High Volume For-Hire Vehicle trip records
    for month in range(2, 13):
        source.extract('fhvhv', 2019, month)
    for year in range(2020, 2021):
        for month in range(1, 13):
            source.extract('fhvhv', year, month)
    for month in range(1, 8):
        source.extract('fhvhv', 2021, month)

# -- Data Processing: Transform -- #


# -- Data Processing: Load -- #


# -- Utilities -- #


def percent(num, denom):
    return 100 * num / denom


def preview(df: pd.DataFrame, func_name: str):
    print(f'INSIDE {func_name}(): type =', type(df).__name__)
    print(df.head(5))


def zScore(x, mean, std):
    return (x - mean) / std


# -- Main Program -- #


def main():
    """
    Runs the main set of functions that define the program.
    """

    # Confirm debugging state.
    DEBUG and print('DEBUG =', DEBUG)

    # Confirm Python path.
    DEBUG and print('sys.path =', sys.path)

    # Print constants.
    DEBUG and print('PREFIX =', PREFIX)

    # Print CLI option values.
    if DEBUG:
        print('args.data =', args.data)        # Ex: data/01_raw
        print('args.results =', args.results)  # Ex: results

    extract_data()
    # df = extract_data()
    # df = transform_data(df)
    # visualize_data(df)


# =========================================================================== #
# MAIN EXECUTION
# =========================================================================== #


# -- CLI option processing -- #

args = cli.read_args()

# -- Main Program -- #

# If this module is in the main module, call the main() function.
if __name__ == '__main__':
    main()

# -- Housekeeping -- #

# Exit the program normally (i.e., with a POSIX exit code of 0).
sys.exit(0)
