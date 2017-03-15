# python-screenconnect
An unofficial Python wrapper around the ScreenConnect API

*Currently undergoing initial development*

## Introduction

This library provides a pure Python interface for the ScreenConnect API. It's undergoing initial
development, but it is intended to work with Python 2.7 and Python 3.

## Requirements

* Python 2.7+
* An installed and publicly-accessible [ScreenConnect](https://www.screenconnect.com/) server
* [requests](https://pypi.python.org/pypi/requests/)
* [enum34](https://pypi.python.org/pypi/enum34) for versions needing Enum backported from 3.4
* [future](https://pypi.python.org/pypi/future) for Python 2

## Installation

The code is hosted at https://github.com/jacobeturpin/python-screenconnect.git

Checkout the code using the following:

```shell
$ git clone git://github.com/jacobeturpin/python-screenconnect.git
$ cd python-screenconnect
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
