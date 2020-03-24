"""
Controller for manage employee use case. Acts as boundary layer that validates requests and map them to and from
ManageEmployeeUseCase and the view.
"""
from ...usecases.ports.manage_employees_ports import ManageEmployeeUseCasePort
import domain.usecases.data_models.request_data_models as request_data_models


class ManageEmployeesController:
    def __init__(self, use_case: ManageEmployeeUseCasePort):
        self._use_case = use_case

    def retrieve_all_employees(self):
        """
        Get all employees
        :return: List of team
        """
        return self._use_case.retrieve_all_employees()

    def retrieve_employee(self, employee_pk: int):
        """
        Get a team of a given primary key
        :param employee_pk: team primary key of a team
        :return:
        """

        return self._use_case.retrieve_employee(employee_pk=employee_pk)

    def create_employee(self, request_data: request_data_models.CreateEmployeeRequestData):
        """
        Save new employee entity in the repository and return TeamEntity
        :param request_data: TeamEntity
        :return: TeamEntity
        """

        return self._use_case.create_employee(request_data)

    def update_employee(self, request_data: request_data_models.UpdateEmployeeRequestData):
        """
        Update new employee entity in the repository and return TeamEntity
        :param request_data:
        :return: TeamEntity
        """
        return self._use_case.update_employee(request_data)

    def delete_employee(self, employee_pk: int):
        """
        Delete new team entity in the repository and return TeamEntity
        :param employee_pk: TeamEntity
        :return: TeamEntity
        """
        self._use_case.delete_employee(employee_pk)
