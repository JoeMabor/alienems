"""
Interface for work arrangements repository. Manages multiple work arrangements for part time employee
"""
from abc import ABC,  abstractmethod
from ...entities.work_arrangment import WorkArrangementEntity


class WorkArrangementRepoPort(ABC):
    """
    Interface class for managing work leader
    """

    @abstractmethod
    def retrieve_all_work_arrangements(self):
        """
        For retrieving all instances of work leader table
        :return:
        """
        pass

    @abstractmethod
    def retrieve_work_arrangement(self, wa_pk: int):
        """
        Retrieving work arrangement instance using primary key (te_pk)
        :param wa_pk: int
        :return: TeamLeaderEntity
        """
        pass

    @abstractmethod
    def save_work_arrangement(self, wa_entity: WorkArrangementEntity):
        """
        :param wa_entity: WorkArrangementEntity
        :return: WorkArrangementEntity
        """
        pass

    @abstractmethod
    def update_work_arrangement(self, wa_entity: WorkArrangementEntity):
        """
        Update work leader
        :param wa_entity: WorkArrangementEntity
        :return:
        """
        pass

    @abstractmethod
    def delete_work_arrangement(self, wa_pk: int):
        """
        Delete work leader
        :param wa_pk: int
        :return: WorkArrangementEntity
        """
        pass
