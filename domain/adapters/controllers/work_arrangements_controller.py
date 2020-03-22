from ...usecases.ports.work_arrangements_port import WorkArrangementUseCasePort
import domain.usecases.data_models.request_data_models as request_data_models


class WorkArrangementsController:
    """
    Maps work arrangement requests to respective work arrangement use case services. Can handle request validation too
    """
    def __init__(self, use_case: WorkArrangementUseCasePort):
        self._use_case = use_case

    def view_all_work_arrangements(self):
        return self._use_case.retrieve_all_work_arrangements()

    def view_work_arrangement(self, wa_pk):
        return self._use_case.retrieve_work_arrangement(wa_pk)

    def add_work_arrangement(self, request_data: request_data_models.CreateWorkArrangementData):
        """
        Add work arrangement
        :param request_data:
        :return:
        """
        return self._use_case.add_work_arrangement(request_data)

    def update_work_arrangement(self, request_data: request_data_models.UpdateWorkArrangementData):
        """
        Update work arrangement
        :param request_data:
        :return:
        """
        return self._use_case.update_work_arrangement(request_data)

    def remove_work_arrangement(self, wa_pk):
        self._use_case.delete_work_arrangement(wa_pk)
