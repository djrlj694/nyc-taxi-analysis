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
from file import YAMLFile


# =========================================================================== #
# METADATA
# =========================================================================== #


__author__ = 'Robert (Bob) L. Jones'
__credits__ = ['Robert (Bob) L. Jones']

__created_date__ = 'Dec 29, 2020'
__modified_date__ = 'Dec 30, 2020'


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


def extract_data(config: dict):

    # Define an inner function to extract source data files.
    def extract_files(type: str):
        source.extract_files(
            type,
            config[type]['start_date'],
            config[type]['end_date'],
        )

    # Create source.
    source = etl.Source(SOURCE_FILE, SOURCE_URL, SOURCE_DIR)

    # Extract trip records.
    extract_files('yellow')  # Yellow Taxi
    extract_files('green')   # Green Taxi
    extract_files('fhv')     # For-Hire Vehicle
    extract_files('fhvhv')   # High Volume For-Hire Vehicle

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
    DEBUG and print('args.config =', args.config)  # Ex: etc/settings/etl.cfg

    # Read a configuration file.
    cfg = YAMLFile(args.config).load()
    DEBUG and print('cfg =', cfg)
    DEBUG and print('type(cfg) =', type(cfg))

    # Create a mini configuration dictionary.
    sources_cfg = cfg['sources']

    extract_data(sources_cfg)
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
