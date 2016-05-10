''' A library that provides a Python interface to the ScreenConnect API '''

from __future__ import print_function

import sys
import time

try:
    # Python 3
    from urllib.parse import urlparse, urlunparse, urlencode
    from urllib.request import urlopen, Request
    from urllib.request import __version__ as urllib_version
    from base64 import b64encode
except ImportError:
    # Python 2.7+

    # Will focus on backporting to Python 2 once basic functionality
    # with Python 3 has been implemented

    from urlparse import urlparse, urlunparse
    from urllib2 import urlopen
    from urllib import urlencode
    from urllib import __version__ as urllib_version


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
        self.user, self.pwd = auth

    def _set_authentication(self):
        ''' Captures and stores the authentication cookie for specified
        user '''

        request = Request(self.url)
        request.add_header('Authorization', 'Basic ''{}:{}'.format(self.user, self.pwd))
        
        # Need to fix - always returns HTTP 500 Error
        r = urlopen(request)
        self._auth_cookie = r.getheader('Set-Cookie')

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