"""
Employee entity with  employee business rules.
"""
import decimal
import datetime


class EmployeeEntity:
    def __init__(self,
                 id: int,
                 name: str,
                 employee_id: str,
                 hourly_rate: decimal.Decimal,
                 employee_type: int,
                 created_at: datetime.datetime,
                 updated_at: datetime.datetime
                 ):

        self._id = id
        self._name = name
        self._employee_id = employee_id
        self._hourly_rate = hourly_rate
        self._employee_type = employee_type
        self._created_at = created_at
        self._updated_at = updated_at

    @property
    def id(self):
        return self._id

    @property
    def name(self):
        return self._name

    @property
    def employee_id(self):
        return self._employee_id

    @property
    def hourly_rate(self):
        return self._hourly_rate

    @property
    def employee_type(self):
        return self._employee_type

    @property
    def created_at(self):
        return self._created_at

    @property
    def updated_at(self):
        return self._updated_at

