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
    def retrieve_all_teams_employees(self):
        """
        For retrieving all instances of tem employee table
        :return:
        """
        pass

    @abstractmethod
    def retrieve_team_employees(self, team_pk: int):
        """
        Retrieving team employee instance using primary key (te_pk)
        :param team_pk: int
        :return: TeamEmployeeEntity
        """
        pass

    @abstractmethod
    def save_team_employee(self, te_entity: TeamEmployeeEntity):
        """
        :param te_entity:
        :return:
        """
        pass

    @abstractmethod
    def delete_team_employee(self, te_pk):
        """
        Delete team employee
        :param te_pk:
        :return:
        """
        pass

    @abstractmethod
    def is_a_member(self, team_pk : int, employee_pk: int):
        """
        Check if employee is already a member in a team
        :param employee_pk:
        :return:
        """

    @abstractmethod
    def team_employee_exists(self, te_pk):
        """
        Check if a team employee of a given team employee id exist in repository
        :param te_pk:
        :return:
        """
        pass

    @abstractmethod
    def employee_has_more_teams(self, employee_pk):
        """
        Check if a team employee of a given team employee id exist in repository
        :param employee_pk:
        :return:
        """
        pass

