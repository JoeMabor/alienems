from domain.entities.work_time import WorkTimeEntity
from domain.usecases.repositories.work_time_repository import WorkTimeRepoPort
from ..models import WorkTime
from .helpers import DataConverter


class WorkTimeRepoImpl(WorkTimeRepoPort):
    """
    Django implementation of work time repositry. Map to django WorkTime ORM model
    """

    def retrieve_all_work_times(self):
        work_time_objs = WorkTime.objects.all()
        work_time_entities = []
        for work_time in work_time_objs:
            work_time_entities.append(DataConverter.to_work_time_entity(work_time))
        return work_time_entities

    def retrieve_work_time(self, wt_pk: int):
        work_time_obj = WorkTime.objects.get(pk=wt_pk)
        return DataConverter.to_work_time_entity(work_time_obj)

    def save_work_time(self, wt_entity: WorkTimeEntity):
        wt_model = WorkTime(employee_id=wt_entity.employee.id, hours=wt_entity.hours)
        wt_model.save()
        wt_model.refresh_from_db()
        return DataConverter.to_work_time_entity(wt_model)
