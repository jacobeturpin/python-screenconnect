from enumerations import SessionType


class Session():
    ''' Object for interacting with ScreenConnect Sessions '''

    def __init__(self, id, name, **kwargs):
        ''' Instantiates a new session object '''

        # Used to handle positional arguments
        f = lambda x: kwargs.get(x, None)

        self.id = id
        self.name = name

        # Need to convert integer into SessionType Enum
        self.session_type = SessionType.Access #placeholder

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


    def modify(self, **kwargs):
        ''' Alter the details or settings of the session '''
        pass

    def end(self):
        pass


class SessionGuestInfo():

    def __init__(self, **kwargs):
        return super().__init__(**kwargs)