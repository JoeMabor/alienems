"""
Interfaces/ports for manage team leaders use cases. These interfaces enforce IDependency Inversion Principle
"""

from abc import ABC, abstractmethod
import domain.usecases.data_models.request_data_models as request_data_models


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
    def assign_team_leader(self, request_data: request_data_models.TeamLeaderOrEmployeeRequestData):
        """
         Assign team leader to a team that doesn't have a team leader
        :param request_data:
        :return:
        """
        pass

    @abstractmethod
    def change_team_leader(self, request_data: request_data_models.UpdateTeamLeaderRequestData):
        pass
