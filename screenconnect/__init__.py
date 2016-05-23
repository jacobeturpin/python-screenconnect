""" A library that provides a Python interface to the ScreenConnect API """

from __future__ import absolute_import


# Add Meta Here

__title__ = 'screenconnect'
__author__ = 'Jacob Turpin'


from .session import Session
from .session_group import SessionGroup
from .enumerations import SessionType
from .api import ScreenConnect
