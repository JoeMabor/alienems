"""
Controller for  team leaders use case. Acts as boundary layer that convert requests and responses to and from
TeamLeaderUseCase and the view.
"""
from ...usecases.ports.team_leaders_port import TeamLeaderUseCasePort
from ...entities.team_leader import TeamLeaderEntity
from ...usecases.data_models.manage_team_data_models import TeamLeaderOrEmployeeRequestData


class TeamLeadersController:
    def __init__(self, use_case: TeamLeaderUseCasePort):
        self._use_case = use_case

    def retrieve_all_teams_leaders(self):
        """
        Get all team leaders with their respective teams
        :return: List of team
        """
        return self._use_case.retrieve_all_teams_leaders()

    def retrieve_team_leader(self, leader_pk: int):
        """
        Get a team of a given primary key
        :param leader_id:
        :return
        """
        return self._use_case.retrieve_team_leader(leader_pk)

    def change_team_leader(self, request_data: TeamLeaderOrEmployeeRequestData):
        """
        map change team leader request to change team leader function in team use case
        :param request_data:
        :return:
        """
        return self._use_case.change_team_leader(request_data)

    def assign_team_leader(self, request_data: TeamLeaderOrEmployeeRequestData):
        """
        map request to assign assign a leader to a team
        :param request_data:
        :return:
        """
        return self._use_case.assign_team_leader(request_data)