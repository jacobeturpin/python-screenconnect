# python-screenconnect: An unofficial Python wrapper around the ConnectWise Control (formerly ScreenConnect) API

*Currently undergoing initial development*

## Introduction

This library provides a pure Python interface for the ConnectWise Control (formerly ScreenConnect) API. Please note,
this project is undergoing initial development.

## Notices About Use of this Package

Two caveats must be made about the use of this package:

First, this project hooks directly into the various web services that come with a new installation of
ConnectWise Control. However, these APIs are considered to exist for private use by the ConnectWise
Control application. Thus, these APIs are not considered to be stable and may change from
release to release. If needing APIs that are guaranteed to be highly stable, please use the
provided [Extension Development framework](https://docs.connectwise.com/ConnectWise_Control_Documentation/Developers) 
from the ConnectWise Control team.

Second, this project is an unofficial implementation. ConnectWise is not officially involved in
this package's development in any capacity, and does not guaranteed long term support. For all other questions
about use please consult the [project license](LICENSE). 

## Requirements

* Python 3.5+ and dependencies listed on `requirements.txt`
* An installed and publicly accessible
  [ConnectWise Control](https://www.connectwise.com/software/control) server

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
