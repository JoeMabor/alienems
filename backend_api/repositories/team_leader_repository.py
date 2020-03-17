from domain.usecases.repositories.team_leader_repository import TeamLeaderRepoPort
from domain.entities.team_leader import TeamLeaderEntity
from ..models import Team, Employee
from .helpers import DataConverter
from django.db.models import Q


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
        leaders = Employee.objects.filter(is_a_leader=True)
        leader_entities = []
        for leader in leaders:
            leader_entities.append(DataConverter.to_employee_entity(leader))
        return leader_entities

    def retrieve_team_leader(self, leader_id: int):
        """
        Retrieve team leader and all teams it leader
        :param leader_id:
        :return:
        """
        employee = Employee.objects.get(pk=leader_id)
        teams = Team.objects.filter(leader=employee)
        print(F"Teams of {employee.name}: {teams}")
        return DataConverter.to_team_leader_entity(employee, teams)

    def save_team_leader(self, team_pk: int, employee_pk: int):
        team_model = Team.objects.get(pk=team_pk)
        team_model.leader_id = employee_pk
        team_model.save()
        team_model.refresh_from_db()
        teams = Team.objects.filter(leader_id=employee_pk)
        employee_obj = Employee.objects.get(pk=employee_pk)
        return DataConverter.to_team_leader_entity(employee_obj, teams)
