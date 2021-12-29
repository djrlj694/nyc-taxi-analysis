# =========================================================================== #
# Copyright © 2021 djrlj694.dev. All rights reserved.
# =========================================================================== #
# PROGRAM: python.sh
# PROJECT: NYE Taxi Analysis
#
# PURPOSE:
# 1. To declare Bash shell functions for Python features.
#
# AUTHORS:
# 1. Robert (Bob) L. Jones
#
# CREATED: Dec 28, 2021
# REVISED: Dec 28, 2021
# =========================================================================== #


# =========================================================================== #
# FUNCTIONS
# =========================================================================== #


# Wraps the Python interpreter with shell variables before running a given
# Python script ($1).
function __python
{
    # Run the Python interpreter.
    PREFIX="${PREFIX}" \
    PYTHONDONTWRITEBYTECODE=1 PYTHONPATH="${PYTHONPATH}" \
    ${PYTHON} "$@"
}

# Prints the Python path.
function __python_debug_path
{
    # Run the Python interpreter.
    __python -c "import sys; print('\n'.join(sys.path))"
}

# Prints the Python3 path.
function __python_debug_path3
{
    echo "which ${PYTHON}=$(which python3)"
}

# Prints Python-related shell variables.
function __python_debug_vars
{
    echo "PYTHON=${PYTHON}"
    echo "PYTHONPKG=${PYTHONPKG}"
    echo "PYTHONPATH=${PYTHONPATH}"
}

# Prints Python-related debugging info.
function __python_debug
{
    __python_debug_vars
    __python_debug_path3
    __python_debug_path
}
