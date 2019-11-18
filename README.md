# python-screenconnect An unofficial Python wrapper around the ScreenConnect API

*Currently undergoing initial development*

## Introduction

This library provides a pure Python interface for the ScreenConnect API. Note
that it's undergoing initial development.

## Requirements

* Python 3.5+ and dependencies listed on `requirements.txt`
* An installed and publicly-accessible
  [ScreenConnect](https://www.screenconnect.com/) server

## Installation

You can install latest release from PyPI by running:

```shell
pip install screenconnect
```

Or if you prefer to install from source, clone this repository and run:

```shell
pip install .
```

## Getting Started

```python
>>> import screenconnect
>>> sc = screenconnect.ScreenConnect('https://examplesite.screenconnect.com', auth=('user', 'pass'))
>>> sc.server_version
'6.2.12646.6275'
>>> sc.get_eligible_hosts()
['Cloud Account Administrator', 'Tech 1', 'Tech 2']
```

## Running Tests

*Coming soon*
