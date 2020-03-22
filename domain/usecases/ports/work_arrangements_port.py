"""
 Module with interface class that define high level business logic for work arrangements.
 Work arrangements allow part time workers to have more than one job in the company.
"""
from abc import ABC, abstractmethod
import domain.usecases.data_models.request_data_models as request_data_models


class WorkArrangementUseCasePort(ABC):
    """
    Interface class that define high level business rules for managing employees work arrangements.
    """

    @abstractmethod
    def retrieve_all_work_arrangements(self):
        """
        Retrieves all work arrangements in the repository
        :return:
        """

    @abstractmethod
    def retrieve_work_arrangement(self, wa_pk):
        """
        Retrieve work arrangement of a given primary key
        :param wa_pk:
        :return:
        """
        pass

    @abstractmethod
    def add_work_arrangement(self, request_data: request_data_models.CreateWorkArrangementData):
        """
        Add new work arrangement
        :param request_data:
        :return:
        """
        pass

    @abstractmethod
    def update_work_arrangement(self, request_data: request_data_models.UpdateWorkArrangementData):
        """
        Update existing work arrangement
        :param request_data:
        :return:
        """
        pass

    @abstractmethod
    def delete_work_arrangement(self, wa_pk):
        """
        Delete existing work arrangement of a given primary key
        :param wa_pk:
        :return:
        """
        pass
