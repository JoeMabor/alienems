from .ports.work_times_port import WorkTimeUseCasPort
from .repositories.work_time_repository import WorkTimeRepoPort
from domain.entities.validators import ObjectEntityDoesNotExist


class WorkTimeUseCase(WorkTimeUseCasPort):
    """
    Implementation of work time
    """
    def __init__(self, work_time_repo: WorkTimeRepoPort):
        self._work_time_repo = work_time_repo

    def retrieve_all_work_times(self):
        return self._work_time_repo.retrieve_all_work_times()

    def retrieve_work_time(self, wt_pk):
        work_time = self._work_time_repo.retrieve_work_time(wt_pk)
        if work_time is None:
            raise ObjectEntityDoesNotExist("work time does not exist")
        return work_time
