from .ports.manage_teams_ports import ManageTeamUseCasePort
from .repositories.team_repository import TeamRepoPort
from .repositories.employee_repository import EmployeeRepoPort
from ..entities.team import TeamEntity
from domain.entities.validators import ObjectEntityDoesNotExist
from .data_models.manage_team_data_models import CreateTeamRequestData


class ManageTeamUseCase(ManageTeamUseCasePort):
    def __init__(self, team_repo: TeamRepoPort, employee_repo:EmployeeRepoPort):
        self._team_repo = team_repo
        self._employee_repo = employee_repo

    def retrieve_all_teams(self):
        return self._team_repo.retrieve_all()

    def retrieve_team(self, team_pk: int):
        return self._team_repo.retrieve_by_id(team_pk=team_pk)

    def create_team(self, request_data: CreateTeamRequestData):
        """
        Create team a new team. Check if team leader is given and save it
        :param request_data:
        :return:
        """
        team_entity = TeamEntity(name=request_data.name, description=request_data.description)
        if request_data.leader_id is not None:
            # team leader is not null
            # save team leader first
            leader = self._employee_repo.retrieve_by_id(request_data.leader_id)
            team_entity.leader = leader

        return self._team_repo.save(team_entity)

    def update_team(self, request_data: CreateTeamRequestData):
        """
        Interface
        :param request_data:
        :return:
        """
        old_team = self._team_repo.retrieve_by_id(request_data.id)
        old_team.name = request_data.name
        old_team.description = request_data.description
        if request_data.leader_id is not None:
            old_team.leader = self._employee_repo.retrieve_by_id(request_data.leader_id)
        return self._team_repo.save(old_team)

    def delete_team(self, team_pk: int):
        """
        Function for deleting a team
        :param team_pk:
        :return:
        """
        if self._team_repo.team_exists(team_pk):
            return self._team_repo.delete(team_pk)
        else:
            raise ObjectEntityDoesNotExist("Team doesnt exists")
