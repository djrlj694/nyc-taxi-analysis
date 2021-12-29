#!/bin/bash
# =========================================================================== #
# Copyright © 2021 | All rights reserved.
# =========================================================================== #
# PROGRAM: study.sh
# PROJECT: NYE Taxi Analysis
# COMPANY: djrlj694.dev
# LICENSE: MIT
#
# PURPOSE:
# - To set shell variables/functions for running the Python package `study`.
#
# AUTHORS:
# - Robert (Bob) L. Jones
#
# CREATED: Dec 28, 2021
# REVISED: Dec 28, 2021
# =========================================================================== #


# =========================================================================== #
# SETUP
# =========================================================================== #


# Path to this script's project root
# Example: ~/Documents/GitHub/nyc-taxi-analysis
PREFIX="$(dirname $(dirname $0))"

# Sourced variables/functions
. "${PREFIX}/src/bash/utilities/sources.sh"

# Path to custom Python packages
PYTHONPATH="${PREFIX}:${PYTHONPATH}"


# =========================================================================== #
# DEBUG
# =========================================================================== #


# Print debugging info.
${DEBUG} && __python_debug


# =========================================================================== #
# MAIN PROCEDURE
# =========================================================================== #


# Run a Python package as if it were a Python script.
__python "${PREFIX}/src/python/packages/${PYTHONPKG}" $@
