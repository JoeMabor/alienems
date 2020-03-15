from .employee import EmployeeEntity
from domain.entities.validators import WorkArrangementPercentageOutOfRange
from domain.entities.validators import WorkArrangementPercentageNull
from domain.entities.validators import NotEmployeeEntityType
from domain.entities.validators import EmployeeIsNull


class WorkArrangementEntity:
    """
    Employee work time entity
    """
    def __init__(self, percent: int, id: int = None,  employee_id: int = None,  remarks: str = None):
        self._id = id
        if percent is None:
            raise WorkArrangementPercentageNull()
        self._percent = percent
        self._employee_id = employee_id
        self._remarks = remarks

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
    def employee_id(self):
        if self._employee_id:
            return self._employee_id
        else:
            raise EmployeeIsNull("Work arrangement employee id can not be null")

    @employee_id.setter
    def employee_id(self, employee_id):
        self._employee_id = employee_id

    @property
    def remarks(self):
        return self._remarks

    def validate_percentage(self, percentage: int):
        if percentage > 0 and percentage < 100:
            return True
        else:
            return False

    def __str__(self):
        return F"{self._percent}"

