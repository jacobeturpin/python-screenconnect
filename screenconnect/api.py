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

    def _reset_auth_account(self, auth):
        ''' Resets the designated account for authorization '''

        user, pwd = auth

        if self.user == user and self.pwd == pwd:
            return None

        self.user, self.__pwd = auth

    def _make_request(self, url, verb, data = None):
        ''' Requests a url to perform an action '''
        pass

    def create_session(self, session_type, name, is_public, code,
                       custom_properties):

        path = self.url + '/Services/PageService.ashx/CreateSession'
        payload = [session_type, name, is_public, code, custom_properties]
        result = requests.post(path, data = dumps(payload),
                               auth=(self.user, self.__pwd))

        # Need to create session object and return that instead
        return result.status_code

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