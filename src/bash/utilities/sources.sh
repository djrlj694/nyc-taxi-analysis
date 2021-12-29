# =========================================================================== #
# Copyright © 2021 | All rights reserved.
# =========================================================================== #
# PROGRAM: preli.sh
# PROJECT: NYE Taxi Analysis
# COMPANY: djrlj694.dev
# LICENSE: MIT
#
# PURPOSE:
# - To consolidate the sourcing of Bash shell variables & functions.
#
# AUTHORS:
# - Robert (Bob) L. Jones
#
# CREATED: Dec 29, 2021
# REVISED: Dec 29, 2021
# =========================================================================== #


# =========================================================================== #
# SOURCED VARIABLES
# =========================================================================== #


if [ -f "~/.env" ]; then
    . "~/.env"
fi

. "${PREFIX}/src/bash/variables/python.env"
. "${PREFIX}/src/bash/variables/default.env"


# =========================================================================== #
# SOURCED FUNCTIONS
# =========================================================================== #


. "${PREFIX}/src/bash/functions/python.sh"
