"""
Employee entity with  employee business rules.
"""
import decimal
import datetime
from .validators import NotEmployeeEntityType
from .validators import EmployeeWorkTimeOutOfRange
from .validators import EmployeeDoesNotHaveATeam


class EmployeeEntity:
    def __init__(self,
                 name: str,
                 employee_id: str,
                 hourly_rate: decimal.Decimal,
                 employee_type: int,
                 id: int = None,
                 created_at: datetime.datetime = None,
                 updated_at: datetime.datetime = None,
                 is_a_leader: bool = None,
                 total_work_hours: int = None,
                 team_id: int = None,

                 ):

        self._id = id
        self._name = name
        self._employee_id = employee_id
        self._hourly_rate = hourly_rate
        self._employee_type = employee_type
        self._created_at = created_at
        self._updated_at = updated_at
        self._total_work_hours = total_work_hours
        self._is_a_leader = is_a_leader
        self._team_id = team_id
        if total_work_hours is not None:
            self._pay = self.calculate_pay()
        else:
            self._pay = None


    @property
    def id(self):
        return self._id

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

    @property
    def employee_id(self):
        return self._employee_id

    @employee_id.setter
    def employee_id(self, employee_id):
        self._employee_id = employee_id

    @property
    def hourly_rate(self):
        return self._hourly_rate

    @hourly_rate.setter
    def hourly_rate(self, rate):
        self._hourly_rate = rate

    @property
    def employee_type(self):
        return self._employee_type

    @employee_type.setter
    def employee_type(self, employee_type):
        self._employee_type = employee_type

    @property
    def created_at(self):
        return self._created_at

    @property
    def updated_at(self):
        return self._updated_at

    @updated_at.setter
    def updated_at(self, time):
        self._updated_at = time

    @property
    def pay(self):
        return self._pay

    @property
    def is_a_leader(self):
        return self._is_a_leader

    def set_team_id(self, team_id):
        self._team_id = team_id

    @staticmethod
    def set_employee(employee):

        # not None or null
        if isinstance(employee, EmployeeEntity):
            return employee
        else:
            raise NotEmployeeEntityType()

    def calculate_pay(self):
        print(F"Total hours: {self._total_work_hours }")
        if self._total_work_hours > 0 and self._total_work_hours <= 40:
            # calculate employee pay
            pay = self._total_work_hours * self._hourly_rate
            if self._is_a_leader:
                # leader get paid 10 % more
                pay += pay * 0.1
            return pay
        else:
            raise EmployeeWorkTimeOutOfRange()

    def is_part_time(self):
        """
        Return true if employee is a part time
        :return:
        """
        if self._employee_type == 2:
            return True
        else:
            return False



