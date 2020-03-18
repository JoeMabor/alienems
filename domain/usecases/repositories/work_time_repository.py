"""
Interface for work times repository.
"""
from abc import ABC,  abstractmethod


class WorkTimeRepoPort(ABC):
    """
    Interface class for managing work leader. Work time is added when a employee or work arrangement is added.
    It can be changed when an employee work arrangement or type is changed
    """

    @abstractmethod
    def retrieve_all_work_times(self):
        """
        For retrieving all instances of work leader table
        :return:
        """
        pass

    @abstractmethod
    def retrieve_work_time(self, wt_pk: int):
        """
        Retrieving work time instance using primary key (te_pk)
        :param wt_pk: int
        :return: TeamLeaderEntity
        """
        pass
