#from enumerations import SessionType

from screenconnect.enumerations import SessionType

class Session():
    """ Object for interacting with ScreenConnect Sessions """

    def __init__(self, api, id, name, **kwargs):
        """ Instantiates a new session object """

        # Used to handle positional arguments
        f = lambda x: kwargs.get(x, None)

        self.api = api
        self.id = id
        self.name = name

        '''
        # Need to convert integer into SessionType Enum
        self.session_type = None
        self.host = f('host')
        self.is_public = f('is_public')
        self.code = f('code')
        self.legacy_encryption_key = f('legacy_encryption_key')
        self.custom_properties = f('custom_property_values')

        
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

    def get_details(self):
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
        self.api._make_request('POST', path, data = event) 

    def end(self):
        self._add_event_to_sessions()


class SessionGuestInfo():

    def __init__(self, **kwargs):
        return super().__init__(**kwargs)