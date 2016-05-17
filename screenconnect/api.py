""" A library that provides a Python interface to the ScreenConnect API """

from __future__ import print_function

import sys
import time
import requests
from datetime import datetime
from json import dumps

from session import Session


class ScreenConnect():
    """ A python interface into the ScreenConnect API """

    def __init__(self,
                 url,
                 auth = None):
        """ Instantiate a new ScreenConnect object 
        
        Arguments:
        url -- publicly accessible url for the ScreenConnect web server 
        auth -- (user, pwd)
        """

        # Need to do some basic sanitation to remove unnecessary 
        # trailing slash
        self.url = url
        self.user, self.__pwd = auth

    def _reset_auth_account(self, auth):
        """ Resets the designated account for authorization """

        user, pwd = auth
        if self.user == user and self.pwd == pwd:
            return None
        self.user, self.__pwd = auth

    def _make_request(self, verb, path, data = None):
        """ Performs request with optional payload to a specified path """
        
        url = self.url + path
        response = requests.request(verb, url, auth = (self.user, self.__pwd),
                                    data = data)
        return response.json()

    # ------------ SESSION METHODS ------------

    def create_session(self, session_type, name, is_public, code,
                       custom_properties):
        """ Creates a new ScreenConnect session """

        path = '/Services/PageService.ashx/CreateSession'
        payload = [session_type, name, is_public, code, custom_properties]
        result = self._make_request('POST', path, data = dumps(payload))
        return Session(self, result, name)
        

    def get_guest_session_info(self):
        pass
    
    def get_host_session_info(self):
        pass

    def update_sessions(self):
        pass

    def transfer_sessions(self):
        pass

    def end_session(self):
        pass

    # ------------ SESSION GROUP METHODS ------------

    def create_session_group(self):
        pass

    def get_session_groups(self):
        """ Retrieves all session groups """

        path = '/Services/SessionGroupService.ashx/GetSessionGroups'
        result = self._make_request('GET', path)
        return result

    def save_session_groups(self):
        pass

    # ------------ MISC METHODS ------------

    def send_email(self):
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