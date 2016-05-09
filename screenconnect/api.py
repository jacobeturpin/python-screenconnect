''' A library that provides a Python interface to the ScreenConnect API '''

import urllib

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

    def _get_authentication_cookie(self):
        ''' Captures and stored the authentication cookie for specified
        user '''

        # Need to resolve
        r = urllib.request.urlopen(self.url)
        self._auth_cookie = r.getheader('Set-Cookie')