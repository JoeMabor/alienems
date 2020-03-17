"""
Interface/port for  employee repository.
"""
from ...entities.employee import EmployeeEntity

from abc import ABC,  abstractmethod


class EmployeeRepoPort(ABC):

    @abstractmethod
    def retrieve_all(self):
        """
        Return all instances of Employees entities
        :return: employees entities
        """
        pass

    @abstractmethod
    def retrieve_by_id(self, employee_pk):
        """
        Return an install of employee entity using id field
        :param employee_pk: employee primary key id
        :return: employee entity
        """
        pass

    @abstractmethod
    def save(self, employee_entity: EmployeeEntity):
        """
        Save new employee in repository
        :param employee_entity: EmployeeEntity
        :return: EmployeeEntity
        """
        pass

    @abstractmethod
    def delete(self, employee_pk: int):
        """
        delete an employee in repository
        :param employee_pk: employee primary key
        :return: EmployeeEntity
        """
        pass

    @abstractmethod
    def employee_exists(self, employee_pk):
        """
        Check if employee is in the repository
        :param employee_pk: employee primary key id
        :return: True or False
        """
        pass



