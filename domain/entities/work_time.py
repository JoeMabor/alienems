
from domain.entities.validators import EmployeeWorkTimeOutOfRange
from .employee import EmployeeEntity
from .work_arrangment import WorkArrangementEntity


class WorkTimeEntity:
    """
    Employee work time entity
    """
    # todo: add work arrangement
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
        if self.validates_hours(self._hours):

            return self._hours
        else:
            raise EmployeeWorkTimeOutOfRange()

    @hours.setter
    def hours(self, hours):
        if self.validates_hours(hours):

            self._hours = hours
        else:
            raise EmployeeWorkTimeOutOfRange()

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
        print(F"Hours: {hours}")
        if hours > 0 and hours <= 40:
            return True
        else:
            return False
