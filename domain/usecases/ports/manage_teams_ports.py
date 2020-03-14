"""
Interfaces/ports for manage team use cases. These interfaces enforce Interface inversion Principle which make
use case controllers that depend on them stable
"""

from abc import ABC
from ...entities.team import TeamEntity


class ManageTeamUseCasePort(ABC):

    def retrieve_all_teams(self):
        pass

    def retrieve_team(self, team_pk: int):
        pass

    def create_team(self, team_entity: TeamEntity):
        pass

    def update_team(self, team_entity: TeamEntity):
        """
        Interface
        :param team_entity: TeamEntity
        :return:
        """
        pass

    def delete_team(self, team_pk: int):
        """
        Interface
        :param team_pk:
        :return:
        """
        pass