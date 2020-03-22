"""
Interfaces/ports for manage team use cases. These interfaces enforce Dependency Inversion Principle
"""

from abc import ABC, abstractmethod
import domain.usecases.data_models.request_data_models as request_data_models


class ManageTeamUseCasePort(ABC):

    @abstractmethod
    def retrieve_all_teams(self):
        pass

    @abstractmethod
    def retrieve_team(self, team_pk: int):
        pass

    @abstractmethod
    def create_team(self, request_data: request_data_models.CreateTeamRequestData):
        pass

    @abstractmethod
    def update_team(self, request_data: request_data_models.CreateTeamRequestData):
        """
        Interface
        :param request_data:
        :return:
        """
        pass

    @abstractmethod
    def delete_team(self, team_pk: int):
        """
        Interface
        :param team_pk:
        :return:
        """
        pass