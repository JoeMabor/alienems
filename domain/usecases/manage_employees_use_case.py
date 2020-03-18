"""
Implementation of abstract business logic of manage employee
"""

from .ports.manage_employees_ports import ManageEmployeeUseCasePort
from .repositories.employee_repository import EmployeeRepoPort
from .repositories.team_employees_repository import TeamEmployeeRepoPort
from .repositories.team_leader_repository import TeamLeaderRepoPort
from .repositories.team_repository import TeamRepoPort
from .repositories.work_arrangement_repository import WorkArrangementRepoPort
from .repositories.work_time_repository import WorkTimeRepoPort
from ..entities.employee import EmployeeEntity
from ..entities.work_arrangment import WorkArrangementEntity
from ..entities.work_time import WorkTimeEntity
from ..entities.validators import WorkArrangementPercentageNull
from ..entities.validators import ObjectEntityDoesNotExist
from .data_models.manage_employees_data_models import UpdateEmployeeMRequestData
import datetime


class ManageEmployeeUseCase(ManageEmployeeUseCasePort):

    def __init__(self,
                 employee_repo: EmployeeRepoPort,
                 team_employee_repo: TeamEmployeeRepoPort,
                 team_leader_repo: TeamLeaderRepoPort,
                 work_time_repo: WorkTimeRepoPort,
                 work_arrangement_repo: WorkArrangementRepoPort,
                 team_repo: TeamRepoPort
                 ):
        self._employee_repo = employee_repo
        self._work_arrangement_repo = work_arrangement_repo
        self._work_time_repo = work_time_repo
        self._team_employee_repo = team_employee_repo
        self._team_leader_repo = team_leader_repo
        self._team_repo = team_repo

    def retrieve_all_employees(self):
        """
        Retrieve all employees in repository
        :return:
        """
        return self._employee_repo.retrieve_all()

    def retrieve_employee(self, employee_pk: int):
        return self._employee_repo.retrieve_by_id(employee_pk=employee_pk)

    def update_employee(self, request_data: UpdateEmployeeMRequestData):
        employee_entity = self._employee_repo.retrieve_by_id(employee_pk=request_data.id)
        employee_entity.name = request_data.name
        employee_entity.employee_id = request_data.employee_id
        employee_entity.hourly_rate = request_data.hourly_rate
        employee_entity.updated_at = datetime.datetime.now()
        return self._employee_repo.save(employee_entity)

    def create_employee(self, employee_entity: EmployeeEntity, team_pk, work_arrangement: WorkArrangementEntity = None):
        """
        Create new employee along with employee work work arrangement amd work time is employee is part time
        :param employee_entity: EmployeeEntity
        :param work_arrangement: WorkArrangementEntity
        :param team_pk:
        :return:
        """
        # employee = self._employee_repo.save(employee_entity)
        if employee_entity.is_part_time():
            if work_arrangement is None:
                raise WorkArrangementPercentageNull()
            new_employee = self._add_part_time_employee(employee_entity=employee_entity, work_arrangement=work_arrangement)
        else:
            new_employee = self._add_full_time_employee(employee_entity)
        team = self._team_repo.team_exists(team_pk)
        if team:
            # check if team exist and team employee
            self._team_employee_repo.save_team_employee(team_pk=team_pk, employee_pk=new_employee.id)
            # check if team has a leader
            if self._team_repo.has_a_leader(team_pk):
                # team has a leader already
                pass
            else:
                # no team leader, make new team member a leader
                tl_entity = self._team_leader_repo.save_team_leader(team_pk=team_pk,
                                                                    employee_pk=new_employee.id)
                new_employee = self._employee_repo.save(employee_entity=new_employee)
        return new_employee

    def delete_employee(self, employee_pk: int):
        if self._employee_repo.employee_exists(employee_pk):
            # delete
            return self._employee_repo.delete(employee_pk)
        else:
            raise ObjectEntityDoesNotExist("Employee doesnt exists")

    def _add_part_time_employee(self, employee_entity: EmployeeEntity, work_arrangement: WorkArrangementEntity):
        employee = self._employee_repo.save(employee_entity)
        work_arrangement.employee = employee
        print(F"work arrange percent: {work_arrangement.percent}")
        wa_entity = self._work_arrangement_repo.save_work_arrangement(work_arrangement)
        work_hours = self._calculate_work_time_hours(wa_entity.percent )
        work_time = WorkTimeEntity(hours=work_hours, employee=employee)
        wt_model = self._work_time_repo.save_work_time(work_time)
        employee.set_work_time_hours(wt_model.hours)
        return employee

    def _add_full_time_employee(self, employee_entity: EmployeeEntity):
        employee = self._employee_repo.save(employee_entity)
        work_time = WorkTimeEntity(hours=40, employee=employee)
        print(F"Work hours in use case: {work_time.hours}")
        wt_model = self._work_time_repo.save_work_time(work_time)
        employee.set_work_time_hours(wt_model.hours)
        return employee

    def _calculate_work_time_hours(self, percentage):
        # part time employees work is work arrangement percentage of 40 hours
        return int((percentage/100) * 40)


