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
    def __init__(self,
                 percent: int,
                 team: TeamEntity,
                 id: int = None,
                 employee: EmployeeEntity = None,
                 remarks: str = None):
        self._id = id
        self.validate_percentage(percent)
        self._percent = percent
        self._employee = employee
        self._remarks = remarks
        self._team = team

    @property
    def id(self):
        return self._id

    @property
    def percent(self):
        return self._percent

    @percent.setter
    def percent(self, percent):
        self._percent = self.validate_percentage(percent)

    @property
    def employee(self):
        return self._employee

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
        """Validate percentage and return the percentage value if it doesnt raise exception"""
        try:
            if percentage < 0 or percentage > 100:
                raise WorkArrangementPercentageOutOfRange()
            else:
                return percentage
        except TypeError:
            raise TypeError("Invalid input")

    @staticmethod
    def calculate_work_time_hours(percentage):
        # part time employees work is work arrangement percentage of 40 hours
        try:
            if percentage < 0 or percentage > 100:
                raise WorkArrangementPercentageOutOfRange()
            else:
                return int((percentage/100) * 40)
        except TypeError:
            raise TypeError("Invalid input")

    def __str__(self):
        return F"{self._percent}"

