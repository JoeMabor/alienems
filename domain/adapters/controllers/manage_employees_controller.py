"""
Controller for manage employee use case. Acts as boundary layer that convert requests and responses to and from
ManageEmployeeUseCase and the view.
"""
from ...usecases.ports.manage_employees_ports import ManageEmployeeUseCasePort
from ...entities.employee import EmployeeEntity
from ...entities.work_arrangment import WorkArrangementEntity
from ...usecases.data_models.manage_employees_data_models import EmployeePresenterData
from ...usecases.data_models.manage_employees_data_models import CreateEmployeeRequestData
from ...usecases.data_models.manage_employees_data_models import UpdateEmployeeMRequestData


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

    def create_employee(self, request_data: CreateEmployeeRequestData):
        """
        Save new employee entity in the repository and return TeamEntity
        :param request_data: TeamEntity
        :return: TeamEntity
        """
        employee_entity = self._to_employee_entity(request_data)
        if employee_entity.is_part_time():
            work_arrangement_entity = self._to_work_arrangement_entity(request_data)
        else:
            work_arrangement_entity = None
        return self._use_case.create_employee(employee_entity=employee_entity, work_arrangement=work_arrangement_entity)

    def update_employee(self, request_data: UpdateEmployeeMRequestData):
        """
        Update new employee entity in the repository and return TeamEntity
        :param employee_entity: TeamEntity
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

    def _to_employee_entity(self, request_data: CreateEmployeeRequestData):
        return EmployeeEntity(
            name=request_data.name,
            employee_id=request_data.employee_id,
            employee_type=request_data.employee_type,
            hourly_rate=request_data.hourly_rate,
            team_id=request_data.team_id

        )

    def _to_work_arrangement_entity(self, request_data: CreateEmployeeRequestData):

        return WorkArrangementEntity(
            percent=request_data.work_arrangement
        )

    def _from_employee_entity(self, employee_entity:EmployeeEntity):
        return EmployeePresenterData(
            id=employee_entity.id,
            name=employee_entity.name,
            employee_id=employee_entity.employee_id,
            hourly_rate=employee_entity.hourly_rate,
            employee_type=employee_entity.employee_type,
            created_at=employee_entity.created_at,
            updated_at=employee_entity.updated_at,
            is_a_leader=employee_entity.is_a_leader,
            pay=employee_entity.pay

        )
