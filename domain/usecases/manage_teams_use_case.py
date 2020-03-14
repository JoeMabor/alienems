from .ports.manage_teams_ports import ManageTeamUseCasePort
from .repositories.team_repository import TeamRepoPort
from ..entities.team import TeamEntity
from ..validators import HasALeader
from ..validators import ObjectEntityDoesNotExist


class ManageTeamUseCase(ManageTeamUseCasePort):
    def __init__(self, team_repo: TeamRepoPort, employee_repo):
        self._team_repo = team_repo
        self._employee_repo = employee_repo

    def retrieve_all_teams(self):
        return self._team_repo.retrieve_all()

    def retrieve_team(self, id):
        return self._team_repo.retrieve_by_id(id)

    def create_team(self, team_entity: TeamEntity):
        """
        Create team a new team. Check if team leader is given and save it
        :param team_entity:
        :return:
        """
        if team_entity.leader:
            # team leader is not null
            # save team leader first
            if team_entity.has_a_leader():
                raise HasALeader()
            else:
                # no team leader
                # assign team leader
                pass
        else:
            return self._team_repo.save(team_entity)

    def update_team(self, team_entity: TeamEntity):
        """
        Interface
        :param team_entity:
        :return:
        """
        return self._team_repo.save(team_entity)

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
