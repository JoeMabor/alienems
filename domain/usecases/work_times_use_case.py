from .ports.work_times_port import WorkTimeUseCasPort
from .repositories.work_time_repository import WorkTimeRepoPort


class WorkTimeUseCase(WorkTimeUseCasPort):
    """
    Implementation of work time
    """
    def __init__(self, work_time_repo: WorkTimeRepoPort):
        self._work_time_repo = work_time_repo

    def retrieve_all_work_times(self):
        return self._work_time_repo.retrieve_all_work_times()

    def retrieve_work_time(self, wt_pk):
        return self._work_time_repo.retrieve_work_time(wt_pk)
