from domain.usecases.repositories.team_leader_repository import TeamLeaderRepoPort
from domain.entities.team_leader import TeamLeaderEntity
from ..models import TeamLeader
from .helpers import DataConverters


class TeamLeaderRepoImpl(TeamLeaderRepoPort):
    """
    Django implementation of team leader repository. Maps to both Employee and Team models. It could be a separate table
    but is it of no use as each team should have only one leader
    """

    def retrieve_all_team_leaders(self):
        """
        Retrieve all teams and get their respective leaders as employee entities
        :return:
        """
        team_leaders = TeamLeader.objects.all()
        leader_entities = []
        for team_leader in team_leaders:
            leader_entities.append(DataConverters.to_team_leader_entity(team_leader))
        return leader_entities

    def retrieve_team_leader(self, tl_pk: int):
        """
        Retrieve team leader and all teams it leader
        :param tl_pk:
        :return:
        """
        try:
            team_leader = TeamLeader.objects.get(pk=tl_pk)
            return DataConverters.to_team_leader_entity(team_leader)
        except TeamLeader.DoesNotExist:
            raise TeamLeader.DoesNotExist

    def save_team_leader(self, team_pk: int, employee_pk: int):
        team_leader = TeamLeader(leader_id=employee_pk, team_id=team_pk)
        team_leader.save()
        team_leader.refresh_from_db()
        return DataConverters.to_team_leader_entity(team_leader)


