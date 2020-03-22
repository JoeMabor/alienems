
from .ports.team_employee_port import TeamEmployeeUseCasePort
from .repositories.team_employees_repository import TeamEmployeeRepoPort
from .repositories.team_repository import TeamRepoPort
from .repositories.employee_repository import EmployeeRepoPort
from ..entities.team_employee import TeamEmployeeEntity
import domain.entities.validators as domain_validators
import domain.usecases.data_models.request_data_models as request_data_models
import datetime


class TeamEmployeeUSeCase(TeamEmployeeUseCasePort):
    """

    Implementation of TeamEmployeeUseCasePort
    """
    def __init__(self,
                 team_employee_repo: TeamEmployeeRepoPort,
                 team_repo: TeamRepoPort,
                 employee_repo: EmployeeRepoPort
                 ):
        self._team_employee_repo = team_employee_repo
        self._team_repo = team_repo
        self._employee_repo = employee_repo

    def retrieve_all_teams_employees(self):
        return self._team_employee_repo.retrieve_all_teams_employees()

    def retrieve_team_employee(self, te_pk: int):
        return self._team_employee_repo.retrieve_team_employees(te_pk)

    def add_team_employee(self, request_data: request_data_models.CreateTeamLeaderOrEmployeeRequestData):
        """
        Add new team employee to repository. If a team an employee is being added to doesn't have a leader, the
        employee becomes a leader
        :param request_data:
        :return:
        """
        team = self._team_repo.team_exists(request_data.team_id)
        if team:
            employee = self._employee_repo.employee_exists(employee_pk=request_data.employee_id)
            if employee:

                if self._team_employee_repo.is_a_member(team_pk=request_data.team_id,
                                                        employee_pk=request_data.employee_id):
                    raise domain_validators.EmployeeIsATeamMember()
                else:
                    print("Not a member")
                    # save team new team employee
                    new_te_entity = TeamEmployeeEntity(
                        team=team,
                        employee=employee,
                        created_at=datetime.datetime.now(),
                        updated_at=datetime.datetime.now()
                    )
                    team_employee = self._team_employee_repo.save_team_employee(new_te_entity)
                    if team.leader:
                        pass
                    else:
                        team.leader = employee
                        self._team_repo.save(team)
                    return team_employee
            else:
                domain_validators.EmployeeDoesNotExist()
        else:
            raise domain_validators.TeamDoesNotExist()

    def remove_team_employee(self, te_pk):
        team_employee = self._team_employee_repo.team_employee_exists(te_pk)
        if team_employee:
            if self._team_employee_repo.employee_has_more_teams(employee_pk=team_employee.employee.id):
                # delete
                self._team_employee_repo.delete_team_employee(te_pk)
            else:
                raise domain_validators.EmployeeHasOneTeam()
        else:
            raise domain_validators.ObjectEntityDoesNotExist("Team Employee doesnt exists")
