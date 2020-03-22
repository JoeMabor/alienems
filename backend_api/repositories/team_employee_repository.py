from domain.usecases.repositories.team_employees_repository import TeamEmployeeRepoPort
from domain.entities.team_employee import TeamEmployeeEntity
from ..models import TeamEmployee
from backend_api.utilities import DataConverters
from django.db.models import Q


class TeamEmployeeRepoImpl(TeamEmployeeRepoPort):
    """
    Django ORM implementation of team employee repository.
    """

    def is_a_member(self, team_pk: int, employee_pk: int):
        # team employee exist in db then employee is already a team member
        try:
            team_employee = TeamEmployee.objects.get(Q(team_id=team_pk) & Q(employee_id=employee_pk))
            print(team_employee)
            return True
        except TeamEmployee.DoesNotExist:
            print(F"Team Id: {team_pk} employee id : {employee_pk}")
            return False

    def retrieve_all_teams_employees(self):
        # loop through team objects and each team employees
        team_employees_entities = []
        team_employees = TeamEmployee.objects.all()

        for te_model in team_employees:
            team_employees_entities.append(DataConverters.to_team_employee_entity(te_model))
        return team_employees_entities

    def retrieve_team_employees(self, te_pk: int):
        te_model = TeamEmployee.objects.get(pk=te_pk)
        return DataConverters.to_team_employee_entity(te_model)

    def save_team_employee(self, te_entity: TeamEmployeeEntity):
        te_model = TeamEmployee(
            team_id=te_entity.team.id,
            employee_id=te_entity.employee.id,
            created_at=te_entity.created_at,
            updated_at=te_entity.updated_at
        )
        te_model.save()
        print("Saved")
        te_model.refresh_from_db()
        return DataConverters.to_team_employee_entity(te_model)

    def delete_team_employee(self, te_pk: int):
        team_employee = TeamEmployee.objects.get(pk=te_pk)
        team_employee.delete()
        return DataConverters.to_team_employee_entity(team_employee)

    def team_employee_exists(self, te_pk):
        try:
            team_employee = TeamEmployee.objects.get(pk=te_pk)
            return DataConverters.to_team_employee_entity(team_employee)
        except TeamEmployee.DoesNotExist:
            return None

    def employee_has_more_teams(self, employee_pk):
        """
        Check if employee has more than one team.
        :param employee_pk:
        :return:
        """
        team_employees = TeamEmployee.objects.filter(employee_id=employee_pk)
        if len(team_employees) > 1:
            return True
        else:
            return False
