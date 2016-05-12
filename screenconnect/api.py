''' A library that provides a Python interface to the ScreenConnect API '''

from __future__ import print_function

import sys
import time
import requests
from datetime import datetime


class ScreenConnect():
    ''' A python interface into the ScreenConnect API '''

    def __init__(self,
                 url,
                 auth = None):
        ''' Instantiate a new ScreenConnect object 
        
        url = publicly accessible url for your ScreenConnect web server 
        auth = (user, pwd)
        '''

        self.url = url
        self.user, self.__pwd = auth
        self.__auth_expiration = datetime.min

    def _set_authentication(self):
        ''' Captures and stores the authentication cookie for specified
        user '''

        r = requests.get(self.url, auth = (self.user, self.__pwd))
        self.__auth_cookie = r.cookies
        #self.__auth_expiration = 

    def _reset_auth_account(self, auth):
        ''' Resets the designated account for authorization '''

        user, pwd = auth

        if self.user == user and self.pwd == pwd:
            return None

        self.user, self.pwd = auth
        self._auth_cookie = None

    def _make_request(self, url, verb, data = None):
        ''' Requests a url to perform an action '''
        pass

    def create_session(self):
        pass

    def end_session(self):
        pass

    def create_session_group(self):
        pass



    '''

        Likely the initial phase for v0.1

        SendEmail


        GetHostSessionInfo
        GetGuestSessionInfo
        GetSessionDetails
        CreateSession
        UpdateSessions
        GetEligibleHosts
        TransferSessions



        GetSessionGroups
        SaveSessionGroups

    '''