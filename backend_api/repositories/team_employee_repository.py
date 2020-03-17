from domain.usecases.repositories.team_employees_repository import TeamEmployeeRepoPort
from domain.entities.team_employee import TeamEmployeeEntity
from ..models import TeamEmployee
from ..models import Team
from .helpers import DataConverter


class TeamEmployeeRepoImpl(TeamEmployeeRepoPort):
    """
    Django ORM implementation of team employee repository.
    """

    def retrieve_all_team_employees(self):
        team_employees = TeamEmployee.objects.all()
        te_entities = []
        for team_employee in team_employees:
            te_entities.append(DataConverter.to_team_employee_entity(team_employee))
        return te_entities

    def retrieve_team_employee(self, te_pk: int):
        team_model = Team.objects.get(pk=te_pk)
        # todo: complete implementation

    def create_team_employee(self, team_pk: int, employee_pk: int):
        te_model = TeamEmployee(team_id=team_pk, employee_id=employee_pk)
        te_model.save()
        te_model.refresh_from_db()
        return DataConverter.to_team_employee_entity(te_model)

    def update_team_employee(self, te_entity: TeamEmployeeEntity):
        pass

    def delete_team_employee(self, te_pk: int):
        pass
