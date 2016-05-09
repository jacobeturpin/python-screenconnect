

class SessionGroup():

    def __init__(self, api, name, session_type):
        ''' Instantiates a session group object '''

        self.api = api
        self.name = name
        self.session_type = session_type