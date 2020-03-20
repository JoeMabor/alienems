"""
Interface/port for  team repository.
"""

from abc import ABC, abstractmethod
from ...entities.team import TeamEntity


class TeamRepoPort(ABC):

    @abstractmethod
    def retrieve_all(self):
        pass

    @abstractmethod
    def retrieve_by_id(self, team_pk):
        pass

    @abstractmethod
    def save(self, team_entity: TeamEntity):
        pass

    @abstractmethod
    def delete(self, team_pk: int):
        pass

    @abstractmethod
    def team_exists(self, team_pk: int):
        """
        Check if tean is in the repository
        :param team_pk: team primary key id
        :return:
        """
        pass

    @abstractmethod
    def has_a_leader(self, team_pk: int):
        """
        Check if a team in the repository already has a leader
        :param team_pk:
        :return:
        """
