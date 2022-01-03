#!/bin/bash
# =========================================================================== #
# Copyright © 2022 | All rights reserved.
# =========================================================================== #
# PROGRAM: extract_header.sh
# PROJECT: NYE Taxi Analysis
# COMPANY: djrlj694.dev
# LICENSE: MIT
#
# PURPOSE:
# - To extract headers from data files.
#
# AUTHORS:
# - Robert (Bob) L. Jones
#
# CREATED: Jan 03, 2021
# REVISED: Jan 03, 2021
# =========================================================================== #


# =========================================================================== #
# SETUP
# =========================================================================== #


# Path to this script's project root
# Example: ~/Documents/GitHub/nyc-taxi-analysis
PREFIX="$(dirname $(dirname $0))"


# =========================================================================== #
# FUNCTIONS
# =========================================================================== #


# Extracts the header from a data file.
function __extract_header
{
    # Set local variables.
    typeset -r data_dir="${PREFIX}/data"
    typeset -r source="${data_dir}/01_raw/${1}"
    typeset -r target="${data_dir}/02_intermediate/header_${1}"

    # Extract header.
    echo "${1}|$(head -1 "${source}")" > ${target}
}


# Extracts headers from data files.
function __extract_headers
{
    # Set local variables.
    typeset -r data_dir="${PREFIX}/data"

    # Extract headers.
    for file in $(find "${data_dir}/01_raw" -type f); do
        __extract_header $(basename ${file})
    done
}


# =========================================================================== #
# MAIN PROCEDURE
# =========================================================================== #


# Extract headers from data files.
__extract_headers
