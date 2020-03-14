"""
Interface/port for  team repository.
"""

from abc import ABC
from ...entities.team import TeamEntity


class TeamRepoPort(ABC):

    def retrieve_all(self):
        pass

    def retrieve_by_id(self, id):
        pass

    def save(self, team_entity: TeamEntity):
        pass

    def delete(self, team_pk: int):
        pass

    def team_exists(self, team_pk: int):
        """
        Check if tean is in the repository
        :param team_pk: team primary key id
        :return: True or False
        """
        pass
