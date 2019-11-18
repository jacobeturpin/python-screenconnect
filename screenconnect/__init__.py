""" A library that provides a Python interface to the ScreenConnect API """

from .session import Session
from .session_group import SessionGroup
from .enumerations import SessionType
from .api import ScreenConnect


__version__ = "0.1.0"


__all__ = [
    "Session",
    "SessionGroup",
    "SessionType",
    "ScreenConnect"
]
