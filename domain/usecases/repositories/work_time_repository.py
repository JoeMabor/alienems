"""
Interface for work times repository.
"""
from abc import ABC,  abstractmethod
from ...entities.work_time import WorkTimeEntity


class WorkTimeRepoPort(ABC):
    """
    Interface class for managing work leader
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

    @abstractmethod
    def save_work_time(self, wt_entity: WorkTimeEntity):
        """
        :param wt_entity: WorkArrangementEntity
        :return: WorkArrangementEntity
        """
        pass

    @abstractmethod
    def update_work_time(self, wt_entity: WorkTimeEntity):
        """
        Update work leader
        :param wt_entity: WorkArrangementEntity
        :return:
        """
        pass

    @abstractmethod
    def delete_work_time(self, wt_pk: int):
        """
        Delete work leader
        :param wt_pk: int
        :return: WorkArrangementEntity
        """
        pass