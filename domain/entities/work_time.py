
from domain.entities.validators import EmployeeWorkTimeOutOfRange
from .employee import EmployeeEntity
from .work_arrangment import WorkArrangementEntity


class WorkTimeEntity:
    """
    Employee work time entity
    """
    def __init__(self,  hours: int, employee: EmployeeEntity, work_arrangement, id: int = None):
        self._id = id
        self._hours = hours
        self._employee = employee
        self._work_arrangement = work_arrangement

    @property
    def id(self):
        return self._id

    @property
    def hours(self):
        return self._hours

    @hours.setter
    def hours(self, hours):
        self._hours = self.validates_hours(hours)

    @property
    def employee(self):
        return self._employee

    @employee.setter
    def employee(self, employee):
        self._employee = employee

    @property
    def work_arrangement(self):
        return self._work_arrangement

    def validates_hours(self, hours: int):
        try:
            if hours < 0 or hours > 40:
                raise EmployeeWorkTimeOutOfRange()
            else:
                return hours
        except TypeError:
            raise TypeError("Invalid inputs")
