""" A library that provides a Python interface to the ScreenConnect API """

from __future__ import print_function

import requests
from json import dumps

from screenconnect.session import Session
from screenconnect.session_group import SessionGroup


class ScreenConnect:
    """ A python interface into the ScreenConnect API """

    def __init__(self, url, auth=None):
        """ Instantiate a new ScreenConnect object 
        
        Arguments:
            url -- publicly accessible url for the ScreenConnect web server
            auth -- (user, pwd)
        """

        # Need to do some basic sanitation to remove unnecessary 
        # trailing slash
        self.url = url
        self.user, self.__pwd = auth

    def __repr__(self):
        return '{0}({1})'.format(self.__class__.__name__, self.url)

    @property
    def server_version(self):
        return requests.get(self.url).headers.get('Server')

    def reset_auth_credentials(self, auth=(None, None)):
        """ Resets the designated account for authorization

        Argument:
            auth -- supplied credentials in (user, pwd); if no credentials
            are provided, they will default to none to revoke access
        """

        user, pwd = auth
        if self.user == user and self.__pwd == pwd:
            return None
        self.user, self.__pwd = auth

    def make_request(self, verb, path, data=None):
        """ Performs request with optional payload to a specified path

        Arguments:
            verb -- HTTP verb to use when making the request
            path -- relative path to append to the object's url
            data -- optional payload to send with the request
        """
        
        url = self.url + path
        response = requests.request(verb, url, auth=(self.user, self.__pwd),
                                    data=data)
        return response.json()

    # ------------ SESSION METHODS ------------

    def create_session(self, session_type, name, is_public, code,
                       custom_properties):
        """ Creates a new ScreenConnect session

        ScreenConnect API -- ~/Services/PageService.ashx/CreateSession

        Arguments:
            session_type -- type of ScreenConnect session
            name -- identifying name visible to users
            is_public -- boolean value on whether the session can be connected
            to form the Guest page
            code -- code that can be used to join from the Guest Page if applicable
            custom_properties -- list of 8 properties that can be used to define
            groups and filters for sessions
        """

        path = '/Services/PageService.ashx/CreateSession'
        payload = [session_type, name, is_public, code, custom_properties]
        result = self.make_request('POST', path, data=dumps(payload))
        return Session(self, result, name)

    def get_guest_session_info(self):
        """ Retrieves information about a session from the Guest perspective

        ScreenConnect API -- ~/Services/PageService.ashx/GetGuestSessionInfo

        Arguments:
        """

        path = '/Services/PageService.ashx/GetGuestSessionInfo'
        pass
    
    def get_host_session_info(self):
        """ Retrieves information about a session from the Host perspective

        ScreenConnect API -- ~/Services/PageService.ashx/GetHostSessionInfo

        Arguments:
        """

        path = '/Services/PageService.ashx/GetHostSessionInfo'
        pass

    def update_sessions(self, session_group_name, session_ids, names, is_publics,
                        codes, custom_property_values):
        """ Updates one or more ScreenConnect sessions within the same session group;
            all lists should be saved in the same respective order

        ScreenConnect API -- ~/Services/PageService.ashx/UpdateSessions

        Arguments:
            session_group_name -- name of the session group to which sessions belong
            session_ids -- list of session ids for the sessions to update
            names --  list of names
            is_publics -- list of boolean is_public statuses
            codes -- list of join code strings
            custom_property_values -- list of custom property value lists
        """

        pass

    def transfer_sessions(self, session_group_name, session_ids, to_host):
        """ Updates the "ownership" quality of one or more ScreenConnect sessions
            within the same session group

        ScreenConnect API -- ~/Services/PageService.ashx/TransferSessions

        Arguments:
            session_group_name --
        """

        path = '/Services/PageService.ashx/TransferSessions'
        pass

    # ------------ SESSION GROUP METHODS ------------

    def get_session_groups(self):
        """ Retrieves all session groups """

        path = '/Services/SessionGroupService.ashx/GetSessionGroups'
        result = self.make_request('GET', path)
        return [SessionGroup(self, **x) for x in result]

    def save_session_groups(self):
        """ Saves all session groups """

        path = '/Services/SessionGroupService.ashx/SaveSessionGroups'
        pass

    # ------------ MISC METHODS ------------

    def get_session_report(self, report_type, select_fields, group_fields,
                           report_filter, aggregate_filter, item_limit):
        """ Get a report based upon session criteria """

        path = '/Report.json'
        pass

    # ------------ MISC METHODS ------------

    def send_email(self):
        """ Sends an email through the ScreenConnect mail service"""

        path = '/Services/MailService.ashx/SendEmail'
        pass

    def get_eligible_hosts(self):
        """ Retrieves list of all accounts with login in past 24 hours """

        path = '/Services/PageService.ashx/GetEligibleHosts'
        pass

    def get_toolbox(self):
        """ Retrieves toolbox items """

        path = '/Services/PageService.ashx/GetToolbox'
        pass
