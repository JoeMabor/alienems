"""
Contain Interface class for that defines high level business rules of manage employees use case
"""
from ...entities.employee import EmployeeEntity
from ...entities.work_arrangment import WorkArrangementEntity
from ..data_models.manage_employees_data_models import UpdateEmployeeMRequestData, CreateEmployeeRequestData
from abc import ABC,  abstractmethod


class ManageEmployeeUseCasePort(ABC):

    @abstractmethod
    def retrieve_all_employees(self):
        """
        Retrieve all employees in a repository
        :return:
        """
        pass

    @abstractmethod
    def retrieve_employee(self, employee_pk: int):
        """
        Retrieve an employee of a given primary key
        :param employee_pk:
        :return:
        """
        pass

    @abstractmethod
    def create_employee(self, request_data: CreateEmployeeRequestData):
        """
        Create new employee
        :param request_data:
        :return: EmployeeEntity
        """
        pass

    @abstractmethod
    def update_employee(self, request_data: UpdateEmployeeMRequestData):
        """
        Update changes to an employee
        :param request_data: UpdateEmployeeMRequestData
        :return: EmployeeEntity
        """
        pass

    @abstractmethod
    def delete_employee(self, employee_pk: int):
        """
        Delete employee of a given primary key from a repository
        :param employee_pk:
        :return:
        """
        pass
