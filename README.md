# COVID-19's Impact on the NYC Taxi Industry

[![version](https://img.shields.io/badge/version-0.1.0-yellow.svg)](https://semver.org)
[![Python 3.8.5](https://img.shields.io/badge/python-3.8.5-blue.svg)](https://www.python.org/downloads/release/python-376/)
[![pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white)](https://github.com/pre-commit/pre-commit)
[![Conventional Commits](https://img.shields.io/badge/Conventional%20Commits-1.0.0-yellow.svg)](https://conventionalcommits.org)

An analysis of the impact of the COVID-19 pandemic on the NYC Taxi industry.

## Introduction

This software project investigates the impact of the the COVID-19 pandemic on
the NYC Taxi Industry. It seeks to answer the following questions:

1. What has been the economic impact of the pandemic on NYC taxi revenue over
   time?
2. What was the most expensive trip? Between what zones? Conversely, what was
   the cheapest trip? What is the difference between these before and during the
   peak impact of the pandemic?
3. What's the most popular payment method? Did this change because of the
   pandemic?
4. What’s the most expensive day of the week to travel on? Did this change
   because of the pandemic?

## Getting Started

### System Requirements

This project supports 2 major operating systems:

* [Linux][Linux]
* [macOS][macOS]

To use or test this project, the following software must first be installed on your
system:

* [Python][Python] v3.8.5 or higher

In addition, this project has 3 third-party Python package dependencies:

* [matplotlib][matplotlib]
* [pandas][pandas]
* [seaborn][seaborn]

These packages come preloaded with the [Anaconda][Anaconda] distribution of
Python.

### Installation

To install this project, run the following command:

```shell
$ git clone https://github.com/djrlj694/nyc-taxi-analysis.git
```

## Files

Files in this project are organized as follows:

```bash
.
├── .editorconfig
├── .gitattributes
├── .gitignore
├── .make/
│   ├── features/
│   │   ├── formatting.mk
│   │   └── helping.mk
│   └── platforms/
│       └── Python.mk
├── .pre-commit-config.yaml
├── .vscode/
│   └── settings.json
├── CODE_OF_CONDUCT.md
├── CONTRIBUTING.md
├── LICENSE
├── README.md
├── bin/
│   ├── extract_headers.sh
│   ├── study.sh
│   └── test.sh
├── data/
│   ├── 01_raw/
│   ├── 02_intermediate/
│   │   └── header_summary_tripdata.csv
│   └── 03_processed/
├── docs/
├── etc/
│   ├── content/
│   │   ├── sample_email_body.html
│   │   ├── sample_email_body.md.jinja2
│   │   └── sample_email_body.txt
│   ├── data/
│   │   └── sample_3x3_data.csv
│   └── settings/
│       └── study_etl.yaml
├── notebooks/
├── pyproject.toml
├── references/
├── results/
└── src/
    ├── bash/
    │   ├── functions/
    │   │   └── python.sh
    │   ├── utilities/
    │   │   └── sources.sh
    │   └── variables/
    │       ├── default.env
    │       └── python.env
    ├── python/
    │   ├── __version__.py
    │   └── packages/
    │       ├── etl/
    │       │   ├── __init__.py
    │       │   └── source.py
    │       ├── file/
    │       │   ├── __init__.py
    │       │   ├── csv.py
    │       │   ├── data.py
    │       │   ├── delimited.py
    │       │   ├── file.py
    │       │   ├── jinja2.py
    │       │   ├── markdown.py
    │       │   ├── sqlite.py
    │       │   └── yaml.py
    │       ├── study/
    │       │   ├── __main__.py
    │       │   └── ui/
    │       │       └── cli.py
    │       └── test/
    │           ├── __init__.py
    │           └── test_file.py
    └── sql/
```

### Source Code

The source code for this project consists of a single Python script file,
`main.py`, that does the following:

1. Downloads source data;
2. Extracts key measurements and categorical data;
3. Shapes the data via integration and the derivation of new data in preparation
   for visualization and summarization;
4. Appropriately labels processed data set with descriptive variable names;
5. Creates artifacts in the form of visualizations and summaries comprising the
   final results set.

### Source Data

All source data used in this project can be found using the NYC NYC Taxi and
Limousine Commission (TLC) [trip record data][TLC]. The data consists of trip
record time series spanning across 4 market sources:

1. Yellow Taxi (January 2009 - July 2021)
2. Green Taxi (August 2013 - July 2021)
3. For-Hire Vehicle (January 2015 - July 2021)
4. High Volume For-Hire Vehicle (February 2019 - July 2021)

A full description of this data is available at:

`https://www1.nyc.gov/site/tlc/about/tlc-trip-record-data.page`


### Target Data

TODO: List the final target data processed after running `main.py`.

### Results

The following figures are visual summaries of daily counts of new positive
incidents of COVID-19 in the United States.

TODO: List figures representing visual summaries.

### Documentation

One documentation file is required to be included in the GitHub repository for
this project:

* `README.md`: This file, the intention of which is to clearly and understandably
explain how all of the scripts work and how they are connected with the other
analysis files cited here.

## Protocol

1. Extract data.
    1. Download the source data as a CSV file.
    2. Read the source data into a `pandas` data frame.
    3. Save a raw copy of the source data.
2. Transform data.
    1. Rename data columns.
    2. Add data columns.
3. Visualize data.
    1. Set graphic figure defaults.
    2. Generate and save graphic figures.

## Known Issues

Currently, there are no known issues.  If you discover any, please kindly submit
a [pull request](CONTRIBUTING.md).

## Contributing

Code and codeless (e.g., documentation) contributions toward improving the
COVID-19 project are welcome. See [CONTRIBUTING.md](CONTRIBUTING.md) for more
information on how to become a contributor.

## License

This project is released under the [MIT License](LICENSE).

## References

See [REFERENCES.md](REFERENCES.md) for a list of these.

[Anaconda]: https://www.anaconda.com/products/individual
[Linux]: https://www.linuxfoundation.org
[macOS]: https://www.apple.com/macos/
[matplotlib]: https://matplotlib.org
[Python]: https://www.python.org
[pandas]: https://pandas.pydata.org
[seaborn]: https://seaborn.pydata.org
[TLC]: https://www1.nyc.gov/site/tlc/about/tlc-trip-record-data.page
