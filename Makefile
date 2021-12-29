#!/usr/bin/make -f
# =========================================================================== #
# Copyright © 2021 djrlj694.dev. All rights reserved.
# =========================================================================== #
# PROGRAM: Makefile
# PROJECT: NYE Taxi Analysis
#
# PURPOSE:
# 1. To support the phases of software project development leading to
#    production-quality releases.
#
# AUTHORS:
# 1. Robert (Bob) L. Jones
#
# CREATED: Dec 28, 2021
# REVISED: Dec 28, 2021
# =========================================================================== #


# =========================================================================== #
# ENVIRONMENT
# =========================================================================== #


-include .env


# =========================================================================== #
# DEFAULT CONSTANTS
# =========================================================================== #


# -- Debugging & Error Capture -- #

# 0 = false, 1 = true
VERBOSE ?= 0

# -- Make -- #

# Name of the main makefile.
MAKEFILE ?= $(firstword $(MAKEFILE_LIST))

# Path of the directory containing the main makefile.
MAKEFILE_DIR ?= $(dir $(realpath $(MAKEFILE)))

# Path of the directory containing secondary makefiles.
MAKE_DIR ?= $(MAKEFILE_DIR).make/


# =========================================================================== #
# INTERNAL CONSTANTS
# =========================================================================== #


# -- Commands -- #

# Command options for no verbosity.
ifeq ($(VERBOSE),0)
Q := --quiet
S := --silent
endif

# Command options for verbosity.
ifneq ($(VERBOSE),0)
V := -v
endif

# -- Help Strings -- #

# -- Continuous Integration/Delivery (CI/CD) -- #

BUILD=`date +%FT%T%z`
VERSION := `git tag | tail -1`


# ============================================================================ #
# PHONY TARGETS
# ============================================================================ #


# -- Main Targets -- #

.PHONY: all clean run run0 run1

# Force the default target execution sequence to display the online help if no
# target is specified in the command line following "make".
all: help

## clean: Completes all cleanup activities.
clean:
	clean-python

## run: Completes all run activities.
run: run0 run1

## run0: Completes all run activities.
run0:
	bin/study.sh -h

## run1: Completes all run activities.
run1:
	bin/study.sh -d data/01_raw -r results


# =========================================================================== #
# SECONDARY MAKEFILES
# =========================================================================== #


# -- Feature Dependencies -- #

-include $(MAKE_DIR)features/formatting.mk
-include $(MAKE_DIR)features/helping.mk

# -- Platform Dependencies -- #

-include $(MAKE_DIR)platforms/Python.mk
