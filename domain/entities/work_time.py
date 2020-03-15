
from domain.entities.validators import EmployeeWorkTimeOutOfRange


class WorkTimeEntity:
    """
    Employee work time entity
    """
    def __init__(self,  hours: int, employee_id: int, id: int = None):
        self._id = id
        self._hours = hours
        self._employee_id = employee_id

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
    def employee_id(self):
        return self._employee_id

    @employee_id.setter
    def employee_id(self, employee_id):
        self._employee_id = employee_id

    def validates_hours(self, hours: int):
        print(F"Hours: {hours}")
        if hours > 0 and hours <= 40:
            return True
        else:
            return False
