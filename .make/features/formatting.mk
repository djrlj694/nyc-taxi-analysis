#!/usr/bin/make -f
# =========================================================================== #
# Copyright © 2021 | All rights reserved.
# =========================================================================== #
# PROGRAM: formatting.mk
# PROJECT: NYE Taxi Analysis
# COMPANY: djrlj694.dev
# LICENSE: MIT
#
# PURPOSE:
# 1. To define variables for special characters & formatting STDOUT.
#
# AUTHORS:
# 1. Robert (Bob) L. Jones
#
# CREATED: Dec 28, 2021
# REVISED: Dec 29, 2021
# =========================================================================== #


# =========================================================================== #
# INTERNAL CONSTANTS
# =========================================================================== #


# -- Special Characters -- #

# C-style octal code representing an ASCII escape character
ESC := \033

# Whitespace
EMPTY :=
SPACE := $(EMPTY) $(EMPTY)

# -- ANSI Escape Sequences -- #

# Text intensity/emphasis of STDOUT
RESET := $(ESC)[0m
BOLD := $(ESC)[1m
DIM := $(ESC)[2m

# Text color of STDOUT
FG_CYAN := $(ESC)[0;36m
FG_GREEN := $(ESC)[0;32m
FG_RED := $(ESC)[0;31m
FG_YELLOW := $(ESC)[1;33m


# =========================================================================== #
# INTERNAL VARIABLES
# =========================================================================== #


# -- Formatted Strings -- #

# Color-formatted names of file system paths
dir_var = $(FG_CYAN)$(@D)$(RESET)
file_var = $(FG_CYAN)$(@F)$(RESET)
subdir_var = $(FG_CYAN)$(shell basename $(@D))$(RESET)

# Color-formatted names of makefile automatic variables
prereq_var = $(FG_CYAN)$<$(RESET)
target_var = $(FG_CYAN)$@$(RESET)
