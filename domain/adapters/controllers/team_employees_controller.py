"""
Controller for  team employees use case. Acts as boundary layer that convert requests and responses to and from
TeamLeaderUseCase and the view.
"""
from ...usecases.ports.team_employee_port import TeamEmployeeUseCasePort
import domain.usecases.data_models.request_data_models as request_data_models


class TeamEmployeeController:
    def __init__(self, use_case: TeamEmployeeUseCasePort):
        self._use_case = use_case

    def retrieve_all_teams_employees(self):
        """
        Get all team employees with their respective teams
        :return: List of team
        """
        return self._use_case.retrieve_all_teams_employees()

    def retrieve_team_employee(self, te_pk: int):
        """
        Get a team employee of a given primary key
        :param te_pk:
        :return
        """
        return self._use_case.retrieve_team_employee(te_pk)

    def add_team_employee(self, request_data: request_data_models.TeamLeaderOrEmployeeRequestData):
        """
        map request to assign assign a employee to a team
        :param request_data:
        :return:
        """
        return self._use_case.add_team_employee(request_data)

    def remove_team_employee(self, te_pk):
        """
        Remove an employee from a team
        :param te_pk:
        :return:
        """
        return self._use_case.remove_team_employee(te_pk)

