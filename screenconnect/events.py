


class SessionEvent():
    """ Object to describe events attributed to a ScreenConnect
        Session
    """

    def __init__(self, **kwargs):

        '''
            - id
            - event type
            - time
            - host
            - data

        '''


        return super().__init__(**kwargs)


class SessionConnectionEvent(SessionEvent):
    """ Object that extends SessionEvent by having an associated
        Connection
    """

    def __init__(self, **kwargs):

        '''
            - connection
        '''

        return super().__init__(**kwargs)
