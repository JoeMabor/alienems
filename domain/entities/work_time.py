
from domain.entities.validators import EmployeeWorkTimeOutOfRange
from .employee import EmployeeEntity


class WorkTimeEntity:
    """
    Employee work time entity
    """
    def __init__(self,  hours: int, employee: EmployeeEntity, id: int = None):
        self._id = id
        self._hours = hours
        self._employee = employee

    @property
    def id(self):
        return self._id

    @property
    def hours(self):
        if self.validates_hours(self._hours):

            return self._hours
        else:
            raise EmployeeWorkTimeOutOfRange()

    @property
    def employee(self):
        return self._employee

    @employee.setter
    def employee(self, employee):
        self._employee = employee

    def validates_hours(self, hours: int):
        print(F"Hours: {hours}")
        if hours > 0 and hours <= 40:
            return True
        else:
            return False
