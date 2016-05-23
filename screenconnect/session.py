""" Session objects """

from screenconnect.enumerations import SessionEvent

from json import dumps


class Session:
    """ Object for interacting with ScreenConnect Sessions """

    def __init__(self, api, id, name, **kwargs):
        """ Instantiates a new session object """

        # Used to handle positional arguments
        f = lambda x: kwargs.get(x, None)

        self.api = api
        self.id = id
        self.name = name

        # Need to convert integer into SessionType Enum
        self.session_type = None
        self.host = f('host')
        self.is_public = f('is_public')
        self.code = f('code')
        self.legacy_encryption_key = f('legacy_encryption_key')
        self.custom_properties = f('custom_property_values')

        '''
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
        '''

        self.get_details()

    def get_details(self):
        """ Gets specific details about session """

        path = '/Services/PageService.ashx/GetSessionDetails'
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

        path = '/Services/PageService.ashx/AddEventToSessions'

        # Attempting to pass empty session group
        # This throws server FaultException b/c SessionGroup doesn't
        # exist

        # Just throwing a hard-coded value in here for testing purposes
        payload = dumps(['All Sessions', [self.id], event.value, ''])
        self.api._make_request('POST', path, data=payload)

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
