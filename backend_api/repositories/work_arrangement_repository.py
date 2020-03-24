from django.db.models import Q
from domain.usecases.repositories.work_arrangement_repository import WorkArrangementRepoPort
from domain.entities.work_arrangment import WorkArrangementEntity
from ..models import WorkArrangement
from backend_api.utilities import DataConverters


class WorkArrangementRepoImpl(WorkArrangementRepoPort):
    """
    Django implementation of intrface for work arrangement repository.
    """

    def retrieve_all(self):
        work_arrangements = WorkArrangement.objects.all()
        wa_entities = []
        for work_arrangement in work_arrangements:
            wa_entities.append(DataConverters.to_work_arrangement_entity(work_arrangement))
        return wa_entities

    def retrieve_by_pk(self, wa_pk: int):
        try:
            work_arrangement = WorkArrangement.objects.get(pk=wa_pk)
            return DataConverters.to_work_arrangement_entity(work_arrangement)
        except WorkArrangement.DoesNotExist:
            return None

    def save(self, wa_entity: WorkArrangementEntity):

        wa_model = WorkArrangement(
            id=wa_entity.id,
            percent=wa_entity.percent,
            employee_id=wa_entity.employee.id,
            team_id=wa_entity.team.id,
            remarks=wa_entity.remarks
                                   )
        wa_model.save()
        wa_model.refresh_from_db()
        return DataConverters.to_work_arrangement_entity(wa_model)

    def work_arrangement_exists(self, wa_pk: int):
        try:
            work_arrangement = WorkArrangement.objects.get(pk=wa_pk)
            return DataConverters.to_work_arrangement_entity(work_arrangement)
        except WorkArrangement.DoesNotExist:
            return None

    def delete(self, wa_pk: int):
        work_arrangement = WorkArrangement.objects.get(pk=wa_pk)
        work_arrangement.delete()
        return DataConverters.to_work_arrangement_entity(work_arrangement)

    def get_employee_work_arrangements_percent(self, employee_pk):
        work_arrangements = WorkArrangement.objects.filter(employee_id=employee_pk)
        # add new work arrangement percent (wa_percent) with all employee work arrangement percent(s) in the db
        # check if total percent(s) equals or less than 100 percent
        total_percent = 0
        for work_arrangement in work_arrangements:
            total_percent += work_arrangement.percent
        return total_percent

    def has_work_arrangement_with_team(self, employee_pk, team_pk):
        # check if employee already have work arrangement with a given team
        try:
            work_arrangement = WorkArrangement.objects.get(Q(employee_id=employee_pk)&Q(team_id=team_pk))
            return True
        except WorkArrangement.DoesNotExist:
            return False

