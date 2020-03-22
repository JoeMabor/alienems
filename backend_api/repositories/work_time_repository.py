from domain.entities.work_time import WorkTimeEntity
from domain.usecases.repositories.work_time_repository import WorkTimeRepoPort
from ..models import WorkTime
from backend_api.utilities import DataConverters


class WorkTimeRepoImpl(WorkTimeRepoPort):
    """
    Django implementation of work time repositry. Map to django WorkTime ORM model
    """

    def retrieve_all_work_times(self):
        work_time_objs = WorkTime.objects.all()
        work_time_entities = []
        for work_time in work_time_objs:
            work_time_entities.append(DataConverters.to_work_time_entity(work_time))
        return work_time_entities

    def retrieve_work_time(self, wt_pk: int):
        work_time_obj = WorkTime.objects.get(pk=wt_pk)
        return DataConverters.to_work_time_entity(work_time_obj)

    def save_work_time(self, wt_entity: WorkTimeEntity):
        wt_model = WorkTime(
            id=wt_entity.id,
            employee_id=wt_entity.employee.id,
            hours=wt_entity.hours,
            work_arrangement_id=wt_entity.work_arrangement.id
        )
        wt_model.save()
        wt_model.refresh_from_db()
        return DataConverters.to_work_time_entity(wt_model)

    def retrieve_by_work_arrangement_pk(self, work_arrangement_pk):
        try:
            work_time_obj = WorkTime.objects.get(work_arrangement_id=work_arrangement_pk)
            return DataConverters.to_work_time_entity(work_time_obj)
        except WorkTime.DoesNotExist:
            return None

