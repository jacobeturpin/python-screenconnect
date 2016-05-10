


class Session():
    ''' Object for interacting with ScreenConnect Sessions '''

    def __init__(self, id, name, **kwargs):
        ''' Instantiates a new session object '''

        #Used to handle positional arguments
        f = lambda x: kwargs.get(x, None)

        self.id = id
        self.name = name

    def modify(self, **kwargs):
        ''' Alter the details or settings of the session '''
        pass

    def end(self):
        pass
