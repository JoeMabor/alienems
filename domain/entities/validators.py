
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


class WorkArrangementPercentageOutOfRange(Exception):
    def __init__(self, message="Employee work arrangement percentage must be more than 0 and less than 100"):
        super(WorkArrangementPercentageOutOfRange, self).__init__(message)
        self.message = message


class WorkArrangementPercentageNull(Exception):
    def __init__(self, message="Part time employee work arrangement percentage can not be empty/null"):
        super(WorkArrangementPercentageNull, self).__init__(message)
        self.message = message


class NotEmployeeEntityType(Exception):
    def __init__(self, message="Employee object is not of EmployeeEntity type"):
        super(NotEmployeeEntityType, self).__init__(message)
        self.message = message


class EmployeeIsNull(Exception):
    def __init__(self, message="Employee object is null"):
        super(EmployeeIsNull, self).__init__(message)
        self.message = message


class EmployeeWorkTimeOutOfRange(Exception):
    def __init__(self, message="Employee work time must be more than 0 and less than 40 "):
        super(EmployeeWorkTimeOutOfRange, self).__init__(message)
        self.message = message


class EntityIdIsNegative(Exception):
    def __init__(self, message="Entity ide can not be a negative integer"):
        super(EntityIdIsNegative, self).__init__(message)
        self.message = message


class EmployeeDoesNotHaveATeam(Exception):
    def __init__(self, message="An employee must have at least one team"):
        super(EmployeeDoesNotHaveATeam, self).__init__(message)
        self.message = message