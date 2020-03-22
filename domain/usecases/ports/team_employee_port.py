"""
Interfaces/ports for manage team employees use cases. Dependency Inversion Principle
"""

from abc import ABC, abstractmethod
from ...entities.team_employee import TeamEmployeeEntity
import domain.usecases.data_models.request_data_models as request_data_models


class TeamEmployeeUseCasePort(ABC):

    @abstractmethod
    def retrieve_all_teams_employees(self):
        """
        Assigning team employee to a team without a employee
        :return:
        """
        pass

    @abstractmethod
    def retrieve_team_employee(self, team_pk: int):
        """
        Retrieve team employee.
        :param team_pk:
        :return:
        """
        pass

    @abstractmethod
    def add_team_employee(self, request_data: request_data_models.TeamLeaderOrEmployeeRequestData):
        """
         Assign team employee to a team that doesn't have a team employee
        :param request_data:
        :return:
        """
        pass

    @abstractmethod
    def remove_team_employee(self, request_data: request_data_models.TeamLeaderOrEmployeeRequestData):
        pass
