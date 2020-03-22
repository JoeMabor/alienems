from ...usecases.ports.work_times_port import WorkTimeUseCasPort


class WorkTimeController:
    def __init__(self, use_case: WorkTimeUseCasPort):
        self._use_case = use_case

    def retrieve_all_work_times(self):
        return self._use_case.retrieve_all_work_times()

    def retrieve_work_time(self, wt_pk):
        return self._use_case.retrieve_work_time(wt_pk)
