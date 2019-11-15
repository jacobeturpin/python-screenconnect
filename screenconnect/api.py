""" A library that provides a Python interface to the ScreenConnect API """

import re
from json import dumps

import requests

from screenconnect.session import Session
from screenconnect.session_group import SessionGroup
from screenconnect.error import ScreenConnectError


class ScreenConnect:
    """ A python interface into the ScreenConnect API """

    def __init__(self, url, auth=None):
        """ Instantiate a new ScreenConnect object

        Arguments:
            url -- publicly accessible url for the ScreenConnect web server
            auth -- (user, pwd)
        """

        # Need to do some basic sanitation to remove unnecessary trailing slash
        self.url = url
        self.user, self.__pwd = auth

    def __repr__(self):
        return "{0}(url: {1}, user: {2})".format(
            self.__class__.__name__, self.url, self.user
        )

    @property
    def server_version(self):
        raw_server = self.make_request("HEAD", return_json=False).headers.get("Server")

        try:
            return re.search("ScreenConnect/([0-9][0-9.]*[0-9])*", raw_server).group(1)
        except AttributeError:
            raise ScreenConnectError("Unable to determine server version")

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

    def make_request(self, verb, path="", data=None, params=None, return_json=True):
        """ Performs request with optional payload to a specified path

        The purpose of

        Arguments:
            verb -- HTTP verb to use when making the request
            path -- relative path to append to the object's url
            data -- optional payload to send with the request
        """

        url = self.url + path
        response = requests.request(
            verb, url, auth=(self.user, self.__pwd), data=data, params=params
        )
        status_code = response.status_code

        if status_code == 200:
            return response.json() if return_json else response
        elif status_code == 403:
            raise ScreenConnectError("Bad or missing credentials provided")
        elif status_code == 404:
            raise ScreenConnectError("Invalid URL provided")
        else:
            raise ScreenConnectError("Unknown error")

    # ------------ SESSION METHODS ------------

    def create_session(self, session_type, name, is_public, code, custom_properties):
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

        # TODO: propagate missing values to Session object

        path = "/Services/PageService.ashx/CreateSession"
        payload = [session_type.value, name, is_public, code, custom_properties]
        result = self.make_request("POST", path, data=dumps(payload))
        return Session(self, result, name)

    def get_guest_session_info(self, session_codes=[], session_ids=[], version=0):
        """ Retrieves information about a session from the Guest perspective

        ScreenConnect API -- ~/Services/PageService.ashx/GetGuestSessionInfo

        Arguments:
        """

        path = "/Services/PageService.ashx/GetGuestSessionInfo"
        payload = [session_codes, session_ids, version]
        response = self.make_request("GET", path, data=dumps(payload))
        return [
            Session(self, _["SessionID"], _["Name"], **_)
            for _ in response.get("Sessions", [])
        ]

    def get_host_session_info(
        self,
        session_type=0,
        session_group_path=[],
        session_filter=None,
        find_session_id=None,
        version=0,
    ):
        """ Retrieves information about a session from the Host perspective

        ScreenConnect API -- ~/Services/PageService.ashx/GetHostSessionInfo

        Arguments:
        """

        path = "/Services/PageService.ashx/GetHostSessionInfo"
        payload = [
            session_type,
            session_group_path,
            session_filter,
            find_session_id,
            version,
        ]
        response = self.make_request("GET", path, data=dumps(payload))
        return [
            Session(self, _["SessionID"], _["Name"], **_)
            for _ in response.get("Sessions", [])
        ]

    def update_sessions(
        self,
        session_group_name,
        session_ids,
        names,
        is_publics,
        codes,
        custom_property_values,
    ):
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
        path = "/Services/PageService.ashx/UpdateSessions"
        self.make_request("POST", path)
        pass

    def transfer_sessions(self, session_group_name, session_ids, to_host):
        """ Updates the "ownership" quality of one or more ScreenConnect sessions
            within the same session group

        ScreenConnect API -- ~/Services/PageService.ashx/TransferSessions

        Arguments:
            session_group_name --
        """

        path = "/Services/PageService.ashx/TransferSessions"
        payload = [session_group_name, session_ids, to_host]
        self.make_request("POST", path, data=dumps(payload))

    # ------------ SESSION GROUP METHODS ------------

    def get_session_groups(self):
        """ Retrieves all session groups """

        path = "/Services/SessionGroupService.ashx/GetSessionGroups"
        result = self.make_request("GET", path)
        return [SessionGroup(self, **x) for x in result]

    def save_session_groups(self, session_groups):
        """ Saves all session groups """

        path = "/Services/SessionGroupService.ashx/SaveSessionGroups"
        payload = list(
            [_.to_dict() for _ in session_groups]
        )  # needs to be nested for some reason
        self.make_request("POST", path, data=dumps(payload))

    # ------------ MISC METHODS ------------

    def get_session_report(
        self,
        report_type=None,
        select_fields=None,
        group_fields=None,
        report_filter=None,
        aggregate_filter=None,
        item_limit=None,
        transform=True,
    ):
        """ Get a report based upon session criteria """

        path = "/Report.json"

        params = {
            "ReportType": report_type,
            "SelectFields": select_fields,
            "GroupFields": group_fields,
            "Filter": report_filter,
            "AggregateFilter": aggregate_filter,
            "ItemLimit": item_limit,
        }

        response = self.make_request(
            "GET", path, params={k: v for k, v in params.items() if v}
        )

        if transform:
            response = [dict(zip(response["FieldNames"], x)) for x in response["Items"]]

        return response

    # ------------ MISC METHODS ------------

    def send_email(self, to, subject=None, body=None, is_html=False):
        """ Sends an email through the ScreenConnect mail service"""

        path = "/Services/MailService.ashx/SendEmail"
        payload = dumps([to, subject, body, is_html])
        self.make_request("POST", path, data=payload)

    def get_eligible_hosts(self):
        """ Retrieves list of all accounts with login in past 24 hours """

        path = "/Services/PageService.ashx/GetEligibleHosts"
        return self.make_request("GET", path)

    def get_toolbox(self):
        """ Retrieves toolbox items """

        path = "/Services/PageService.ashx/GetToolbox"
        return self.make_request("GET", path)
