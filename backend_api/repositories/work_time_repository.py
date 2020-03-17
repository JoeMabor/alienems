from domain.entities.work_time import WorkTimeEntity
from domain.usecases.repositories.work_time_repository import WorkTimeRepoPort
from ..models import WorkTime
from .helpers import DataConverter

class WorkTimeRepoImpl(WorkTimeRepoPort):
    """
    Django implementation of work time repositry. Map to django WorkTime ORM model
    """

    def retrieve_all_work_times(self):
        pass

    def retrieve_work_time(self, wt_pk: int):
        pass

    def save_work_time(self, wt_entity: WorkTimeEntity):
        wt_model = WorkTime(employee_id=wt_entity.employee.id, hours=wt_entity.hours)
        wt_model.save()
        wt_model.refresh_from_db()
        return DataConverter.to_work_time_entity(wt_model)

    def update_work_time(self, wt_entity: WorkTimeEntity):
        pass

    def delete_work_time(self, wt_pk: int):
        pass
