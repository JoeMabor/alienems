"""
Interface/port for  employee repository.
"""
from ...entities.employee import EmployeeEntity

from abc import ABC


class EmployeeRepoPort(ABC):

    def retrieve_all(self):
        """
        Return all instances of Employees entities
        :return: employees entities
        """
        pass

    def retrieve_by_id(self, id):
        """
        Return an install of employee entity using id field
        :param id: employee primary key id
        :return: employee entity
        """
        pass

    def save(self, employee_entity: EmployeeEntity):
        """
        Save new employee in repository
        :param employee_entity: EmployeeEntity
        :return: EmployeeEntity
        """
        pass

    def employee_exists(self, id):
        """
        Check if employee is in the repository
        :param id: employee primary key id
        :return: True or False
        """
        pass



