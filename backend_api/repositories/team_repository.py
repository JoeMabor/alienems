from domain.usecases.repositories.team_repository import TeamRepoPort
from domain.entities.team import TeamEntity
from backend_api.models import Team, TeamLeader
from .helpers import DataConverter


class TeamRepoPortImp(TeamRepoPort):
    """
    Implementation of team repository in django
    """

    def retrieve_all(self):
        team_objects = Team.objects.all()
        team_models = []
        for team in team_objects:
            team_models.append(DataConverter.to_team_entity(team))
        return team_models

    def retrieve_by_id(self, team_pk):
        try:
            team_obj = Team.objects.get(pk=team_pk)
        except Team.DoesNotExist:
            raise Team.DoesNotExist
        return DataConverter.to_team_entity(team_obj)

    def save(self, team_entity: TeamEntity):
        team_model = DataConverter.from_team_entity(team_entity)
        print(F"Team: {team_model.created_at}")
        team_model.save()
        team_model.refresh_from_db()
        new_team_entity = DataConverter.to_team_entity(team_model)
        print(F"New team entity: {new_team_entity.name}")
        return new_team_entity

    def delete(self, team_pk):
        try:
            team = Team.objects.get(pk=team_pk)
            team.delete()
            team_entity = DataConverter.to_team_entity(team)
            return team_entity
        except Team.DoesNotExist:
            raise Team.DoesNotExist

    def team_exists(self, team_pk):
        try:
            team_obj = Team.objects.get(pk=team_pk)
            return DataConverter.to_team_entity(team_obj)
        except Team.DoesNotExist:
            return None

    def has_a_leader(self, team_pk: int):
        try:
            team_leader = TeamLeader.objects.get(team_id=team_pk)
            return True
        except TeamLeader.DoesNotExist:
            return False
