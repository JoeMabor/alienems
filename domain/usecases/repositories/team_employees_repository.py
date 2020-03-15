"""
Interface for team employee repository
"""
from abc import ABC,  abstractmethod
from ...entities.team_employee import TeamEmployeeEntity


class TeamEmployeeRepoPort(ABC):
    """
    Interface class for managing team employee
    """

    @abstractmethod
    def retrieve_all_team_employees(self):
        """
        For retrieving all instances of tem employee table
        :return:
        """
        pass

    @abstractmethod
    def retrieve_team_employee(self, te_pk:int):
        """
        Retrieving team employee instance using primary key (te_pk)
        :param te_pk: int
        :return: TeamEmployeeEntity
        """
        pass

    @abstractmethod
    def create_team_employee(self, te_entity: TeamEmployeeEntity):
        """
        :param te_entity: TeamEmployeeEntity
        :return: TeamEmployeeEntity
        """
        pass

    @abstractmethod
    def update_team_employee(self, te_entity: TeamEmployeeEntity):
        """
        Update team employee
        :param te_entity: TeamEmployeeEntity
        :return:
        """
        pass

    @abstractmethod
    def delete_team_employee(self, te_pk: int):
        """
        Delete team employee
        :param te_pk: int
        :return: TeamEmployeeEntity
        """
        pass