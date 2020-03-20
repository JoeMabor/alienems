"""
Team entity that has pure team business rules. This decouple business rules database dependency
"""
from .employee import EmployeeEntity
from .validators import NotEmployeeEntityType
from .validators import EmployeeIsNull
import datetime


class TeamEntity:
    def __init__(self,
                 name: str,
                 description: str,
                 id=None,
                 leader: EmployeeEntity = None,
                 created_at: datetime.datetime = None,
                 updated_at: datetime.datetime = None
                 ):
        self._id = id
        self._name = name
        self._description = description
        self._created_at = created_at
        self._updated_at = updated_at
        self._leader = leader


    @property
    def id(self):
        return self._id

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

    @property
    def description(self):
        return self._description

    @description.setter
    def description(self, description):
        self._description = description

    @property
    def created_at(self):
        return self._created_at

    @property
    def updated_at(self):
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        self._updated_at = updated_at

    @updated_at.setter
    def updated_at(self, time):
        self._updated_at = time

    @property
    def leader(self):
        return self._leader

    @leader.setter
    def leader(self, leader):
        self._leader = leader

    @property
    def has_a_leader(self):
        """
        Check if a team has a leader
        :return:
        """
        if self._leader:
            return True
        else:
            return False

    def is_a_leader(self, employee):
        """
        Check is a given employee is a leader of a team instance
        :param employee:
        :return:
        """
        if self._leader.id == employee.id:
            return True
        else:
            return False

    @staticmethod
    def set_team(team):
        if team:
            # not None or null
            if isinstance(team, TeamEntity):
                return team
            else:
                raise NotEmployeeEntityType()
        raise EmployeeIsNull()
