"""
Controller for manage team use case. Acts as boundary layer that convert requests and responses to and from
ManageTeamUseCase and the view.
"""
from ...usecases.ports.manage_teams_ports import ManageTeamUseCasePort
from ...entities.team import TeamEntity


class ManageTeamController:
    def __init__(self, use_case: ManageTeamUseCasePort):
        self._use_case = use_case

    def retrieve_all_teams(self):
        """
        Get all teams
        :return: List of team
        """
        return self._use_case.retrieve_all_teams()

    def retrieve_team(self, team_pk: int):
        """
        Get a team of a given primary key
        :param team_pk: team primary key of a team
        :return:
        """
        return self._use_case.retrieve_team(team_pk=team_pk)

    def create_team(self, team_entity: TeamEntity):
        """
        Save new team entity in the repository and return TeamEntity
        :param team_entity: TeamEntity
        :return: TeamEntity
        """
        return self._use_case.create_team(team_entity)

    def update_team(self, team_entity: TeamEntity):
        """
        Update new team entity in the repository and return TeamEntity
        :param team_entity: TeamEntity
        :return: TeamEntity
        """
        return self._use_case.update_team(team_entity)

    def delete_team(self, team_pk: int):
        """
        Delete new team entity in the repository and return TeamEntity
        :param team_entity: TeamEntity
        :return: TeamEntity
        """
        return self._use_case.delete_team(team_pk)
