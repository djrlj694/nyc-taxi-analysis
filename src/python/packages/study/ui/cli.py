#!/usr/bin/env python3
"""
cli.py - A module for reading input from a command-line interface (CLI).
"""
import argparse


# =========================================================================== #
# METADATA
# =========================================================================== #


__author__ = 'Robert (Bob) L. Jones'
__credits__ = ['Robert (Bob) L. Jones']

__created_date__ = 'Dec 28, 2021'
__modified_date__ = 'Dec 30, 2021'


# =========================================================================== #
# FUNCTIONS
# =========================================================================== #


# -- Input Processing -- #

def read_args():
    """
    Read command-line arguments.

    Returns
    -------
    Namespace
        A populated namespace of command-line arguments and their values.
    """

    prog = 'study'
    proj = 'NYE Taxi Analysis'

    parser = argparse.ArgumentParser(
        prog=prog,
        description=f'Generates artifacts for study {proj}.',
        epilog=f'example: {prog} -c config.yaml',
    )
    parser.add_argument(
        '-c', '--config',
        action='store',
        type=str,
        required=True,
        help='YAML-formatted configuration file',
    )

    # Return an object containing the parsed arguments.
    return parser.parse_args()


# =========================================================================== #
# MAIN EXECUTION
# =========================================================================== #


# -- Main Program -- #

# If this module is in the main module, run local unit tests.
if __name__ == '__main__':

    # Test custom functions.
    print('Testing custom functions.')
    print('read_args() =', read_args())
    print('read_args().config =', read_args().config)
