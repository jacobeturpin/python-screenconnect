"""  """

from screenconnect.enumerations import SessionType


class SessionGroup:
    """ Object for interacting with ScreenConnect Session Groups """

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

        self._api = api

        self.name = kwargs.get("Name")
        self.session_type = SessionType(kwargs.get("SessionType"))
        self.session_filter = kwargs.get("SessionFilter")
        self.subgroup_expressions = kwargs.get("SubgroupExpressions")

    def __repr__(self):
        return "{0}(name: {1}, type: {2}, filter: {3})".format(
            self.__class__.__name__, self.name, self.session_type, self.session_filter
        )

    def to_dict(self):
        """ Returns object as dict """
        return {
            "Name": self.name,
            "SessionType": self.session_type.value,
            "SessionFilter": self.session_filter,
            "SubgroupExpressions": self.subgroup_expressions,
        }

    def modify(self, **kwargs):
        """ Alter the details or settings of the session group """
        pass
