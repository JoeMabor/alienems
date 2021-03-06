from .ports.work_arrangements_port import WorkArrangementUseCasePort
import domain.usecases.data_models.request_data_models as request_data_models
from .repositories.work_arrangement_repository import WorkArrangementRepoPort
from .repositories.work_time_repository import WorkTimeRepoPort
from .repositories.employee_repository import EmployeeRepoPort
from .repositories.team_repository import TeamRepoPort
from .repositories.team_employees_repository import TeamEmployeeRepoPort
from .repositories.team_leader_repository import TeamLeaderRepoPort
from ..entities.work_arrangment import WorkArrangementEntity
from ..entities.work_time import WorkTimeEntity
from ..entities.team_employee import TeamEmployeeEntity
from ..entities.team_leader import TeamLeaderEntity
import domain.entities.validators as domain_validators
import datetime


class WorkArrangementUseCase(WorkArrangementUseCasePort):
    """
    Implementation of WorkArrangementUseCasePort
    """
    def __init__(
            self,
            work_arrangement_repo: WorkArrangementRepoPort,
            work_time_repo: WorkTimeRepoPort,
            employee_repo: EmployeeRepoPort,
            team_repo: TeamRepoPort,
            team_employee_repo: TeamEmployeeRepoPort,
            team_leader_repo: TeamLeaderRepoPort
    ):
        self._work_arrangement_repo = work_arrangement_repo
        self._work_time_repo = work_time_repo
        self._employee_repo = employee_repo
        self._team_repo = team_repo
        self._team_employee_repo = team_employee_repo
        self._team_leader_repo = team_leader_repo

    def retrieve_all_work_arrangements(self):
        """
        Retrieve all work arrangements
        :return:
        """
        return self._work_arrangement_repo.retrieve_all()

    def retrieve_work_arrangement(self, wa_pk):
        work_arrangement = self._work_arrangement_repo.retrieve_by_pk(wa_pk)
        if work_arrangement is None:
            raise domain_validators.ObjectEntityDoesNotExist("Work arrangement does not exist")
        return work_arrangement

    def add_work_arrangement(self, request_data: request_data_models.CreateWorkArrangementData):
        """
        Add new work arrangement of an employee
        :param request_data:
        :return:
        """
        employee = self._employee_repo.employee_exists(request_data.employee_id)
        if employee is None:
            raise domain_validators.ObjectEntityDoesNotExist("Employee does not exist")
        # check if employee is part time: can not add multiple work arrangement for full time employees
        if not employee.is_part_time():
            raise domain_validators.MultipleWorksForFullTimeEmployee()
        team = self._team_repo.team_exists(request_data.team_id)
        # check if team exist in repository
        if team is None:
            raise domain_validators.TeamDoesNotExist()

        total_percent = self._work_arrangement_repo.get_employee_work_arrangements_percent(employee_pk=employee.id)
        if total_percent + request_data.percent > 100:
            raise domain_validators.Max40HoursExceeded()

        # check if an employee is a team employee
        if self._team_employee_repo.is_a_member(team_pk=team.id, employee_pk=employee.id):
            if self._work_arrangement_repo.has_work_arrangement_with_team(employee_pk=employee.id, team_pk=team.id):
                # employee can not have more than 1 work arrangement in on team
                raise domain_validators.MultipleWorkArrangementInOneTeam()
        else:
            # add team employee if an employee is not a team employee
            new_te_entity = TeamEmployeeEntity(
                employee=employee,
                team=team,
                created_at=datetime.datetime.now(),
                updated_at=datetime.datetime.now()
            )
            self._team_employee_repo.save_team_employee(new_te_entity)
            # check if team has a leader otherwise make an employee a team leader
            if team.has_a_leader:
                # team already have a leader
                pass
            else:
                # No leader, make new employee the leader by default
                new_tl_entity = TeamLeaderEntity(
                    leader=employee,
                    team=team,
                    created_at=datetime.datetime.now(),
                    updated_at=datetime.datetime.now()
                )
                self._team_leader_repo.save_team_leader(new_tl_entity)

        # create work arrangement entity
        work_arrangement = WorkArrangementEntity(
            percent=request_data.percent,
            remarks=request_data.remarks,
            employee=employee,
            team=team
        )
        # save new work arrangement
        new_wa_entity = self._work_arrangement_repo.save(work_arrangement)
        # save respective work time
        work_hours = WorkArrangementEntity.calculate_work_time_hours(request_data.percent)
        work_time = WorkTimeEntity(hours=work_hours, employee=employee, work_arrangement=new_wa_entity)
        self._work_time_repo.save_work_time(work_time)
        # get employee with update work times and pay
        employee_with_updated_pay = self._employee_repo.retrieve_by_id(new_wa_entity.employee.id)
        new_wa_entity.employee = employee_with_updated_pay
        return new_wa_entity

    def update_work_arrangement(self, request_data: request_data_models.UpdateWorkArrangementData):
        """
        Update existing work arrangement
        :param request_data:
        :return:
        """
        work_arrangement_entity = self._work_arrangement_repo.work_arrangement_exists(wa_pk=request_data.id)
        if work_arrangement_entity is None:
            raise domain_validators.ObjectEntityDoesNotExist("Work arrangement does not exist in repository")

        employee = self._employee_repo.employee_exists(request_data.employee_id)
        if employee is None:
            raise domain_validators.ObjectEntityDoesNotExist("Employee doesn't exist")
        # check if employee is part time: can not add multiple work arrangement for full time employees
        if not employee.is_part_time():
            raise domain_validators.MultipleWorksForFullTimeEmployee()
        team = self._team_repo.team_exists(request_data.team_id)
        # check if team exist in repository
        if team is None:
            raise domain_validators.TeamDoesNotExist()
        total_percent = self._work_arrangement_repo.get_employee_work_arrangements_percent(employee_pk=employee.id)
        if (total_percent - work_arrangement_entity.percent) + request_data.percent > 100:
            raise domain_validators.Max40HoursExceeded()

        # check if an employee is a team employee
        if self._team_employee_repo.is_a_member(team_pk=team.id, employee_pk=employee.id):
            if self._work_arrangement_repo.has_work_arrangement_with_team(employee_pk=request_data.id,
                                                                          team_pk=team.id) and \
                    request_data.id != employee.id:
                # employee can not have more than 1 work arrangement in on team if work arrangement team is updated
                raise domain_validators.MultipleWorkArrangementInOneTeam()
        else:
            # add team employee if an employee is not a team employee
            new_te_entity = TeamEmployeeEntity(
                employee=employee,
                team=team,
                created_at=datetime.datetime.now(),
                updated_at=datetime.datetime.now()
            )
            self._team_employee_repo.save_team_employee(new_te_entity)
            # check if team has a leader otherwise make an employee a team leader
            if team.has_a_leader:
                pass
            else:
                new_tl_entity = TeamLeaderEntity(
                    leader=employee,
                    team=team,
                    created_at=datetime.datetime.now(),
                    updated_at=datetime.datetime.now()
                )
                self._team_leader_repo.save_team_leader(new_tl_entity)

        # create updated work arrangement entity
        work_arrangement = WorkArrangementEntity(
            id=request_data.id,
            percent=request_data.percent,
            remarks=request_data.remarks,
            employee=employee,
            team=team
        )
        # save new work arrangement
        new_wa_entity = self._work_arrangement_repo.save(work_arrangement)
        # get and update respective work time
        work_time = self._work_time_repo.retrieve_by_work_arrangement_pk(work_arrangement_pk=new_wa_entity.id)
        work_hours = WorkArrangementEntity.calculate_work_time_hours(request_data.percent)
        print(F"work time {work_time}")
        if work_time:
            # work time in repository: update it
            work_time.hours = work_hours
        else:
            # work time not in database: create new one
            work_time = WorkTimeEntity(hours=work_hours, employee=employee, work_arrangement=new_wa_entity)
        self._work_time_repo.save_work_time(work_time)
        # get employee with update work times and pay
        employee_with_updated_pay = self._employee_repo.retrieve_by_id(new_wa_entity.employee.id)
        new_wa_entity.employee = employee_with_updated_pay
        return new_wa_entity

    def delete_work_arrangement(self, wa_pk):
        work_arrangement = self._work_arrangement_repo.retrieve_by_pk(wa_pk)
        if work_arrangement is None:
            raise domain_validators.ObjectEntityDoesNotExist("Work arrangement does not exist")
        return self._work_arrangement_repo.delete(wa_pk=wa_pk)


