from .ports.team_leaders_port import TeamLeaderUseCasePort
from .repositories.team_leader_repository import TeamLeaderRepoPort
from .repositories.team_repository import TeamRepoPort
from .repositories.employee_repository import EmployeeRepoPort
import domain.entities.validators as domain_validators
from .data_models.manage_team_data_models import TeamLeaderOrEmployeeRequestData


class TeamLeadersUseUseCase(TeamLeaderUseCasePort):
    def __init__(self, team_leader_repo: TeamLeaderRepoPort, team_repo: TeamRepoPort, employee_repo: EmployeeRepoPort):
        self._team_leader_repo = team_leader_repo
        self._team_repo = team_repo
        self._employee_repo = employee_repo

    def retrieve_all_teams_leaders(self):
        """
        Retrieve all team leaders of all teams
        :return:
        """
        return self._team_leader_repo.retrieve_all_team_leaders()

    def assign_team_leader(self, request_data: TeamLeaderOrEmployeeRequestData):
        """
        Assign team leader to a team without a leader
        :param request_data:
        :return:
        """
        # check if team exists in repository
        if self._team_repo.team_exists(team_pk=request_data.team_id):
            # team is in repository
            if self._team_repo.has_a_leader(team_pk=request_data.team_id):
                raise domain_validators.TeamHasALeader()
            # check is employee exist in repository before assigning him/her as a leader
            employee = self._employee_repo.employee_exists(employee_pk=request_data.employee_id)
            if employee:
                tl_entity = self._team_leader_repo.save_team_leader(team_pk=request_data.team_id,
                                                                    employee_pk=request_data.employee_id)
                employee.is_a_leader = True
                self._employee_repo.save(employee_entity=employee)
                return tl_entity

            else:
                raise domain_validators.EmployeeDoesNotExist()
        else:
            raise domain_validators.TeamDoesNotExist()

    def retrieve_team_leader(self, tl_pk: int):
        """
        Retrieving a team leader for a given team primary key
        :param tl_pk:
        :return:
        """
        return self._team_leader_repo.retrieve_team_leader(tl_pk)

    def change_team_leader(self, request_data: TeamLeaderOrEmployeeRequestData):
        """
        Change  a leader of a team to a new leader
        :param request_data:
        :return:
        """
        # check if team exists in repository
        if self._team_repo.team_exists(team_pk=request_data.team_id):
            # team is in repository
            # check is employee exist in repository before assigning him/her as a leader
            employee = self._employee_repo.employee_exists(employee_pk=request_data.employee_id)
            if employee:
                tl_entity = self._team_leader_repo.save_team_leader(team_pk=request_data.team_id,
                                                                    employee_pk=request_data.employee_id)
                return tl_entity
            else:
                raise domain_validators.EmployeeDoesNotExist()
        else:
            raise domain_validators.TeamDoesNotExist()

