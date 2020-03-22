from abc import ABC, abstractmethod


class WorkTimeUseCasPort(ABC):
    """
    Interface that defines business logic for work time
    """

    @abstractmethod
    def retrieve_all_work_times(self):
        """
        Retrieve all work times of respective employees
        :return:
        """
    @abstractmethod
    def retrieve_work_time(self, wt_pk):
        """
        Retrieve work time of a given primary key
        :param wt_pk:
        :return:
        """