"""
Team entity that has pure team business rules. This decouple business rules database dependency
"""
from .employee import EmployeeEntity


class TeamEntity:
    def __init__(self, name: str, description: str,  id=None, leader: EmployeeEntity = None):
        self._id = id
        self._name = name
        self._description = description
        self._leader = leader

    @property
    def id(self):
        return self._id

    @property
    def name(self):
        return self._name

    @property
    def description(self):
        return self._description

    @property
    def leader(self):
        return self._leader

    @leader.setter
    def leader(self, leader):
        self._leader = leader

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