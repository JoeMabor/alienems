from domain.usecases.repositories.work_arrangement_repository import WorkArrangementRepoPort
from domain.entities.work_arrangment import WorkArrangementEntity
from ..models import WorkArrangement
from .helpers import DataConverter


class WorkArrangementRepoImpl(WorkArrangementRepoPort):
    """
    Django implementation of intrface for work arrangement repository.
    """

    def retrieve_all_work_arrangements(self):
        pass

    def retrieve_work_arrangement(self, wa_pk: int):
        pass

    def save_work_arrangement(self, wa_entity: WorkArrangementEntity):
        wa_model = WorkArrangement(percent=wa_entity.percent,
                                   employee_id=wa_entity.employee.id,
                                   remarks=wa_entity.remarks
                                   )
        wa_model.save()
        wa_model.refresh_from_db()
        return DataConverter.to_work_arrangement_entity(wa_model)

    def update_work_arrangement(self, wa_entity: WorkArrangementEntity):
        pass

    def delete_work_arrangement(self, wa_pk: int):
        pass
