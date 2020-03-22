from .ports.team_leaders_port import TeamLeaderUseCasePort
from .repositories.team_leader_repository import TeamLeaderRepoPort
from .repositories.team_repository import TeamRepoPort
from .repositories.employee_repository import EmployeeRepoPort
import domain.entities.validators as domain_validators
from domain.entities.team_leader import TeamLeaderEntity
import domain.usecases.data_models.request_data_models as request_data_models
import datetime


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

    def assign_team_leader(self, request_data: request_data_models.CreateTeamLeaderOrEmployeeRequestData):
        """
        Assign team leader to a team without a leader
        :param request_data:
        :return:
        """
        # check if team exists in repository
        team = self._team_repo.team_exists(team_pk=request_data.team_id)
        if team:
            # team is in repository
            if self._team_repo.has_a_leader(team_pk=request_data.team_id):
                raise domain_validators.TeamHasALeader()
            # check is employee exist in repository before assigning him/her as a leader
            employee = self._employee_repo.employee_exists(employee_pk=request_data.employee_id)
            if employee:
                # create new team
                new_tl_entity = TeamLeaderEntity(
                    leader=employee,
                    team=team,
                    created_at=datetime.datetime.now(),
                    updated_at=datetime.datetime.now()
                )
                saved_tl_entity = self._team_leader_repo.save_team_leader(new_tl_entity)
                employee.is_a_leader = True
                return saved_tl_entity

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

    def change_team_leader(self, request_data: request_data_models.UpdateTeamLeaderRequestData):
        """
        Change  a leader of a team to a new leader
        :param request_data:
        :return:
        """
        # check if team exists in repository
        old_team_leader = self._team_leader_repo.retrieve_team_leader(request_data.id)
        if old_team_leader is None:
            raise domain_validators.ObjectEntityDoesNotExist("Team leader does not exist")
        team = self._team_repo.team_exists(team_pk=request_data.team_id)
        if team is None:
            raise domain_validators.TeamDoesNotExist()
        # team is in repository
        # check is employee exist in repository before assigning him/her as a leader
        employee = self._employee_repo.employee_exists(employee_pk=request_data.employee_id)
        if employee is None:
            raise domain_validators.EmployeeDoesNotExist()
        updated_tl_entity = TeamLeaderEntity(
            id=old_team_leader.id,
            leader=employee,
            team=team,
            created_at=old_team_leader.created_at,
            updated_at=datetime.datetime.now()
        )
        tl_entity = self._team_leader_repo.save_team_leader(updated_tl_entity)
        return tl_entity


