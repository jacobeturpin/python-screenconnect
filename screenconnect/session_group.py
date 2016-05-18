"""  """

from screenconnect import ScreenConnect, SessionType

class SessionGroup():

    def __init__(self, api, **kwargs):
        """ Instantiates a session group object 
        
        Arguments:
        api -- object used to enact any changes/modifications
        name -- the name defined for the Session Group
        session_type -- the enumeration used to describe the type of session
        is_system -- describes whether the Session Group is user-modifiable
        session_filter -- definition by which the group is populated
        subgroup_expressions -- criteria for any further session organization
        """

        f = lambda x: kwargs.get(x)

        self.api = api

        self.name = f('Name')
        self.session_type = SessionType(f('SessionType'))
        self.is_system = f('IsSystem')
        self.session_filter = f('SessionFilter')
        self.subgroup_expressions = f('SubgroupExpressions')

    def modify(self, **kwargs):
        """ Alter the details or settings of the session group """
        pass

    def end(self):
        pass