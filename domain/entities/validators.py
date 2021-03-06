
class TeamHasALeader(Exception):
    """
    Exception thrown if a user attempt to assign a leader to a team that already has a leader
    """
    def __init__(self, message="Team already has a leader"):
        super(TeamHasALeader, self).__init__(message)
        self.message = message


class UpdateOfTeamLeaderOfWrongTeam(Exception):
    """
    Exception thrown if a user attempt to update team leader but provided team is not the team whose leader needed to
    be changed
    """
    def __init__(self, message="Provided team is not of team leader being changed"):
        super(UpdateOfTeamLeaderOfWrongTeam, self).__init__(message)
        self.message = message


class EmployeeIsNotALeader(Exception):
    """
    Exception thrown if a user attempt to retrieve  a leader of given team primary key
    """
    def __init__(self, message="Employee of the given id is not a leader"):
        super(EmployeeIsNotALeader, self).__init__(message)
        self.message = message


class EmployeeIsATeamMember(Exception):
    """
    Exception thrown if a user attempt to retrieve  a leader of given team primary key
    """
    def __init__(self, message="Employee of the given id already a team team member"):
        super(EmployeeIsATeamMember, self).__init__(message)
        self.message = message


class EmployeeHasOneTeam(Exception):
    """
    Exception thrown if a user attempt to retrieve  a leader of given team primary key
    """
    def __init__(self, message="Can not remove team employee when employee is a member of one team only"):
        super(EmployeeHasOneTeam, self).__init__(message)
        self.message = message


class EmployeeNotATeamMember(Exception):
    """
    Exception thrown if a user attempt to retrieve  a leader of given team primary key
    """
    def __init__(self, message="Employee is not a member of the given team"):
        super(EmployeeNotATeamMember, self).__init__(message)
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


class EmployeeDoesNotExist(Exception):
    def __init__(self, message="Employee with the given id does not exist"):
        super(EmployeeDoesNotExist, self).__init__(message)
        self.message = message


class TeamDoesNotExist(Exception):
    def __init__(self, message="Team with the given id does not exist"):
        super(TeamDoesNotExist, self).__init__(message)
        self.message = message


class EmployeeIDIsNotUnique(Exception):
    def __init__(self, message="New  employee ID  already exist"):
        super(EmployeeIDIsNotUnique, self).__init__(message)
        self.message = message


class MultipleWorksForFullTimeEmployee(Exception):
    def __init__(self, message="Employee is full time. Only part time employees can have multiple work arrangements"):
        super(MultipleWorksForFullTimeEmployee, self).__init__(message)
        self.message = message


class MultipleWorkArrangementInOneTeam(Exception):
    def __init__(self, message="Employee can not have multiple work arrangement in one team"):
        super(MultipleWorkArrangementInOneTeam, self).__init__(message)
        self.message = message


class Max40HoursExceeded(Exception):
    def __init__(self, message="Employee work arrangement percent can not exceed 40 max work hours"):
        super(Max40HoursExceeded, self).__init__(message)
        self.message = message


class EmployeeIDLengthNot5(Exception):
    def __init__(self, message="Length of an employee ID must be 5"):
        super(EmployeeIDLengthNot5, self).__init__(message)
        self.message = message
