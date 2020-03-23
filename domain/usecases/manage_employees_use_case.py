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
from ..entities.team import TeamEntity
from ..entities.team_leader import TeamLeaderEntity
from ..entities.validators import WorkArrangementPercentageNull
from ..entities.validators import ObjectEntityDoesNotExist
from ..entities.validators import EmployeeIDIsNotUnique
from ..entities.team_employee import TeamEmployeeEntity
import domain.entities.validators as domain_validators
import domain.usecases.data_models.request_data_models as request_data_models
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
        employee_entity = self._employee_repo.retrieve_by_id(employee_pk=employee_pk)
        if employee_entity is None:
            raise ObjectEntityDoesNotExist("Employee does not exist")
        return employee_entity

    def update_employee(self, request_data: request_data_models.UpdateEmployeeRequestData):
        employee_entity = self._employee_repo.retrieve_by_id(employee_pk=request_data.id)
        if employee_entity is None:
            raise ObjectEntityDoesNotExist("Employee does not exist")
        employee_entity.name = request_data.name
        employee_entity.employee_id = request_data.employee_id
        employee_entity.hourly_rate = request_data.hourly_rate
        employee_entity.updated_at = datetime.datetime.now()
        return self._employee_repo.save(employee_entity)

    def create_employee(self, request_data: request_data_models.CreateEmployeeRequestData):
        """
        Create new employee along with employee work work arrangement amd work time is employee is part time
        :param request_data:
        :return:
        """
        # check if new employee DI exist in the database
        if self._employee_repo.is_employee_id_unique(employee_id=request_data.employee_id) is False:
            raise EmployeeIDIsNotUnique()
        team = self._team_repo.team_exists(request_data.team_id)
        if team is None:
            raise domain_validators.TeamDoesNotExist()

        employee_entity = self._create_new_employee_entity(request_data)
        if employee_entity.is_part_time():
            if request_data.work_arrangement is None:
                raise WorkArrangementPercentageNull()
            work_arrangement = WorkArrangementEntity(
                percent=request_data.work_arrangement,
                team=team
            )
            new_employee = self._add_part_time_employee(employee_entity=employee_entity,
                                                        work_arrangement=work_arrangement)
        else:
            new_employee = self._add_full_time_employee(employee_entity, team)
        # add team employee
        # check if team exist and team employee
        new_te_entity = TeamEmployeeEntity(
            employee=new_employee,
            team=team,
            created_at=datetime.datetime.now(),
            updated_at=datetime.datetime.now()
        )
        self._team_employee_repo.save_team_employee(new_te_entity)
        # check if team has a leader
        if team.has_a_leader:
            # team has a leader already
            pass
        else:
            # no team leader, make new team member a leader
            new_tl_entity = TeamLeaderEntity(
                leader=new_employee,
                team=team,
                created_at=datetime.datetime.now(),
                updated_at=datetime.datetime.now()
            )
            tl_entity = self._team_leader_repo.save_team_leader(new_tl_entity)
            new_employee.is_a_leader = True
        return new_employee

    def delete_employee(self, employee_pk: int):
        employee = self._employee_repo.employee_exists(employee_pk)
        if employee is None:
            raise ObjectEntityDoesNotExist("Employee doesnt exists")
            # delete
        return self._employee_repo.delete(employee_pk)

    def _add_part_time_employee(self, employee_entity: EmployeeEntity, work_arrangement: WorkArrangementEntity):
        employee = self._employee_repo.save(employee_entity)
        work_arrangement.employee = employee
        print(F"work arrange percent: {work_arrangement.percent}")
        saved_wa_entity = self._work_arrangement_repo.save(work_arrangement)
        print(F"work Arrangement: {saved_wa_entity}")
        if saved_wa_entity:
            work_hours = WorkArrangementEntity.calculate_work_time_hours(saved_wa_entity.percent)
            work_time = WorkTimeEntity(hours=work_hours, employee=employee, work_arrangement=saved_wa_entity)
            wt_model = self._work_time_repo.save_work_time(work_time)
            employee.set_work_time_hours(wt_model.hours)
        return employee

    def _add_full_time_employee(self, employee_entity: EmployeeEntity, team: TeamEntity):
        employee = self._employee_repo.save(employee_entity)
        work_arrangement = WorkArrangementEntity(
            percent=100,
            remarks="Full Time employee",
            employee=employee,
            team=team
        )
        saved_wa_entity = self._work_arrangement_repo.save(work_arrangement)
        if saved_wa_entity:
            work_time = WorkTimeEntity(hours=40, employee=employee, work_arrangement=saved_wa_entity)
            print(F"Work hours in use case: {work_time.hours}")
            wt_model = self._work_time_repo.save_work_time(work_time)
            employee.set_work_time_hours(wt_model.hours)
        return employee

    def _create_new_employee_entity(self, request_data: request_data_models.CreateEmployeeRequestData):
        """Create new employee entity"""
        return EmployeeEntity(
            name=request_data.name,
            employee_id=request_data.employee_id,
            employee_type=request_data.employee_type,
            hourly_rate=request_data.hourly_rate,
            created_at=datetime.datetime.now(),
            updated_at=datetime.datetime.now()

        )


