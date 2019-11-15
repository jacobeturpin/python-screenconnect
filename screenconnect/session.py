""" Session objects """

from json import dumps

from screenconnect.enumerations import SessionEvent, SessionType


class Session:
    """ Object for interacting with ScreenConnect Sessions """

    def __init__(self, api, session_id, name, **kwargs):
        """ Instantiates a new session object """

        self._api = api
        self.session_id = session_id
        self.name = name

        # Need to convert integer into SessionType Enum
        self.session_type = SessionType(kwargs.get("SessionType", -1))
        self.host = kwargs.get("host")
        self.is_public = kwargs.get("is_public")
        self.code = kwargs.get("code")
        self.legacy_encryption_key = kwargs.get("legacy_encryption_key")
        self.custom_properties = kwargs.get("custom_property_values")

        """
            GuestInfo
            GuestInfoUpdateTime
            QueuedEventType
            QueuedEventHost
            QueuedEventData
            QueuedEventConnectionID
            LastEventTime
            IsEnded
            Notes
            GuestNetworkAddress
            GuestClientVersion
            Attributes
            ActiveConnections
            LastAlteredVersion
        """

        self.get_details()

    def __repr__(self):
        return "{0}(id: {1}, name: {2}, type: {3})".format(
            self.__class__.__name__, self.session_id, self.name, self.session_type.name
        )

    def get_details(self):
        """ Gets specific details about session """

        # path = "/Services/PageService.ashx/GetSessionDetails"
        pass

    def modify_details(self, **kwargs):
        """ Alter the details or settings of the session """

        pass

    def _add_event_to_sessions(self, event):
        """ Adds a SessionEvent record to one or more Sessions

        ScreenConnect API

        - sessionGroupName
        - sessionIDs
        - sessionEventType
        - data
        """

        path = "/Services/PageService.ashx/AddEventToSessions"

        # Attempting to pass empty session group
        # This throws server FaultException b/c SessionGroup doesn't
        # exist

        # Just throwing a hard-coded value in here for testing purposes
        payload = dumps(["All Sessions", [self.session_id], event.value, ""])
        self._api.make_request("POST", path, data=payload)

    def end(self):
        self._add_event_to_sessions(SessionEvent.EndedSession)


class SessionGuestInfo:
    def __init__(self, **kwargs):

        """
            - guest network address
            - guest machine name
            - guest machine domain
            - guest processor name
            - guest processor virtual count
            - guest system memory total megabytes
            - guest system memory available megabytes
            - guest screenshot content type
            - guest info update time
            - guest screenshot content
            - base time

        """

        super().__init__(**kwargs)
