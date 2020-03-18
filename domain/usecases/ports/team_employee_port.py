"""
Interfaces/ports for manage team employees use cases. These interfaces enforce Interface inversion Principle which make
use case controllers that depend on them stable
"""

from abc import ABC, abstractmethod
from ...entities.team_employee import TeamEmployeeEntity
from ..data_models.manage_team_data_models import TeamLeaderOrEmployeeRequestData


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
    def add_team_employee(self, request_data: TeamLeaderOrEmployeeRequestData):
        """
         Assign team employee to a team that doesn't have a team employee
        :param request_data:
        :return:
        """
        pass

    @abstractmethod
    def remove_team_employee(self, request_data: TeamLeaderOrEmployeeRequestData):
        pass
