"""
Interfaces/ports for manage team use cases. These interfaces enforce Interface inversion Principle which make
use case controllers that depend on them stable
"""

from abc import ABC, abstractmethod
from ...entities.team_leader import TeamLeaderEntity
from ..data_models.manage_team_data_models import TeamLeaderRequestData


class TeamLeaderUseCasePort(ABC):

    @abstractmethod
    def retrieve_all_teams_leaders(self):
        """
        Assigning team leader to a team without a leader
        :return:
        """
        pass

    @abstractmethod
    def retrieve_team_leader(self, leader_id: int):
        """
        Retrieve team leader.
        :param leader_id:
        :return:
        """
        pass

    @abstractmethod
    def assign_team_leader(self, request_data: TeamLeaderRequestData):
        """
         Assign team leader to a team that doesn't have a team leader
        :param request_data:
        :return:
        """
        pass

    @abstractmethod
    def change_team_leader(self, request_data: TeamLeaderRequestData):
        pass
