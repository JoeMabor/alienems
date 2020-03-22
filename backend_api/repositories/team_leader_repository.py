from domain.usecases.repositories.team_leader_repository import TeamLeaderRepoPort
from domain.entities.team_leader import TeamLeaderEntity
from ..models import TeamLeader
from backend_api.utilities import DataConverters


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
            return None

    def save_team_leader(self, tl_entity: TeamLeaderEntity):
        team_leader = TeamLeader(
            id=tl_entity.id,
            leader_id=tl_entity.leader.id,
            team_id=tl_entity.team.id,
            created_at=tl_entity.created_at,
            updated_at=tl_entity.updated_at
        )
        team_leader.save()
        team_leader.refresh_from_db()
        return DataConverters.to_team_leader_entity(team_leader)


