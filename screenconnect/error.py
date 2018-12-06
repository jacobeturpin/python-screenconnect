"""Errors specific to this library"""


class ScreenConnectError(Exception):
    """ Base class for ScreenConnect errors """

    @property
    def message(self):
        """ Returns provided message to construct error """
        return self.args[0]
