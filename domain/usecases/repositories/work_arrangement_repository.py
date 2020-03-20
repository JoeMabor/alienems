"""
Interface for work arrangements repository. Manages multiple work arrangements for part time employee
"""
from abc import ABC,  abstractmethod
from ...entities.work_arrangment import WorkArrangementEntity


class WorkArrangementRepoPort(ABC):
    """
    Interface class for managing work arrangements
    """

    @abstractmethod
    def retrieve_all(self):
        """
        For retrieving all instances of work leader table
        :return:
        """
        pass

    @abstractmethod
    def retrieve_by_pk(self, wa_pk: int):
        """
        Retrieving work arrangement instance using primary key (te_pk)
        :param wa_pk: int
        :return: TeamLeaderEntity
        """
        pass

    @abstractmethod
    def save(self, wa_entity: WorkArrangementEntity):
        """
        :param wa_entity: WorkArrangementEntity
        :return: WorkArrangementEntity
        """
        pass

    @abstractmethod
    def delete(self, wa_pk: int):
        """
        Delete work leader
        :param wa_pk: int
        :return: WorkArrangementEntity
        """
        pass

    @abstractmethod
    def get_employee_work_arrangements_percent(self, employee_pk: int):
        """
        Check if new work arrangement percentage time exceed work time of 40 hours. All employee work arrangements
        percentages must be less than or equals to 100 percentage (40hours)
        :param employee_pk:
        :return:
        """
        pass

    @abstractmethod
    def has_work_arrangement_with_team(self, employee_pk:int, team_pk:int):
        """
        Check if an employee already have work arrangement with a given team. Employee different work arrangements
        must be with different teams
        :param employee_pk:
        :param team_pk:
        :return:
        """
        pass

    @abstractmethod
    def work_arrangement_exists(self, wa_pk: int):
        """
        Check if work arrangement of  a given primary key exist
        :param wa_pk:
        :return:
        """
