
class HasALeader(Exception):
    """
    Exception thrown if a user attempt to assign a leader to a team that already has a leader
    """
    def __init__(self, message="Team already has a leader"):
        super(HasALeader, self).__init__(message)
        self.message = message


class ObjectEntityDoesNotExist(Exception):
    """
    Exception thrown if a user attempt to assign a leader to a team that already has a leader
    """
    def __init__(self, message="Object doesn't exist"):
        super(ObjectEntityDoesNotExist, self).__init__(message)
        self.message = message
