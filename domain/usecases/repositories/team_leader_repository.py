"""
Interface for team leader repository
"""
from abc import ABC,  abstractmethod
from ...entities.team_leader import TeamLeaderEntity


class TeamLeaderRepoPort(ABC):
    """
    Interface class for managing team leader
    """

    @abstractmethod
    def retrieve_all_team_leaders(self):
        """
        For retrieving all instances of team leader table
        :return:
        """
        pass

    @abstractmethod
    def retrieve_team_leader(self, tl_pk: int):
        """
        Retrieving team leader instance using primary key (te_pk)
        :param tl_pk: int
        :return: TeamLeaderEntity
        """
        pass

    @abstractmethod
    def save_team_leader(self, team_pk: int, employee_pk):
        """
        Create/assign team leader
        :param team_pk:
        :param employee_pk:
        :return:
        """
        pass
