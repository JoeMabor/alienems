from .employee import EmployeeEntity
from domain.entities.validators import WorkArrangementPercentageOutOfRange
from domain.entities.validators import WorkArrangementPercentageNull
from .employee import EmployeeEntity
from .team import TeamEntity
from domain.entities.validators import NotEmployeeEntityType
from domain.entities.validators import EmployeeIsNull


class WorkArrangementEntity:
    """
    Employee work time entity
    """
    def __init__(self, percent: int, team: TeamEntity, id: int = None,  employee: EmployeeEntity = None,  remarks: str = None):
        self._id = id
        if percent is None:
            raise WorkArrangementPercentageNull()
        self._percent = percent
        self._employee = employee
        self._remarks = remarks
        self._team = team

    @property
    def id(self):
        return self._id

    @property
    def percent(self):
        if self.validate_percentage(self._percent):
            return self._percent
        else:
            raise WorkArrangementPercentageOutOfRange()

    @property
    def employee(self):
        if self._employee:
            return self._employee
        else:
            raise EmployeeIsNull("Work arrangement employee id can not be null")

    @employee.setter
    def employee(self, employee):
        self._employee = employee

    @property
    def team(self):
        return self._team

    @property
    def remarks(self):
        return self._remarks

    def validate_percentage(self, percentage: int):
        if percentage > 0 and percentage <= 100:
            return True
        else:
            return False

    @staticmethod
    def calculate_work_time_hours(percentage):
        # part time employees work is work arrangement percentage of 40 hours
        return int((percentage/100) * 40)

    def __str__(self):
        return F"{self._percent}"

