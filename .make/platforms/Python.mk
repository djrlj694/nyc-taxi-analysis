#!/usr/bin/make -f
# =========================================================================== #
# Copyright © 2021 djrlj694.dev. All rights reserved.
# =========================================================================== #
# PROGRAM: Python.mk
# PROJECT: NYE Taxi Analysis
#
# PURPOSE:
# 1. To facilitate Python project initialization, setup, and cleanup.
#
# AUTHORS:
# 1. Robert (Bob) L. Jones
#
# CREATED: Dec 28, 2021
# REVISED: Dec 28, 2021
# =========================================================================== #


# =========================================================================== #
# PHONY TARGETS
# =========================================================================== #


# -- Prerequisites for "clean" Target -- #

.PHONY: clean-python clean-python-build clean-python-pyc

# clean-python: Completes all Python cleanup activities.
clean-python: clean-python-build clean-python-pyc
	@find . -name '.mypy_cache' -exec rm -rf {} +
	@find . -name '__pycache__' -exec rm -rf {} +

# Cleans Python files that are always created in the project's root directory.
clean-python-build:
	@rm -fR *.egg-info

# Cleans Python files that could be created anywhere in the project.
clean-python-pyc:
	@find . -name '*.pyc' -exec rm -f {} +
	@find . -name '*.pyo' -exec rm -f {} +
	@find . -name '*~' -exec rm -f  {} +
