"""
Employee entity with  employee business rules.
"""
import decimal
import datetime
from .validators import NotEmployeeEntityType
from .validators import EmployeeWorkTimeOutOfRange
from .validators import EmployeeDoesNotHaveATeam
import decimal


class EmployeeEntity:
    def __init__(self,
                 name: str,
                 employee_id: str,
                 hourly_rate: decimal.Decimal,
                 employee_type: int,
                 is_a_leader: bool = False,
                 id: int = None,
                 created_at: datetime.datetime = None,
                 updated_at: datetime.datetime = None,
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
        self._pay = None
        self._bonus_percent = decimal.Decimal(value=0.10)

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
        if self._total_work_hours is not None:
            self._pay = self.calculate_pay()
        return self._pay

    def set_work_time_hours(self, hours):
        self._total_work_hours = hours

    @property
    def is_a_leader(self):
        return self._is_a_leader

    @is_a_leader.setter
    def is_a_leader(self, is_leader: bool):
        self._is_a_leader = is_leader

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
        if self._total_work_hours >=0 and self._total_work_hours <= 40:
            # calculate employee pay
            pay = self._total_work_hours * self._hourly_rate
            if self._is_a_leader:
                # leader get paid 10 % more
                pay += self._add_leadership_bonus(pay)
            return pay
        else:
            print(F"Employee id:{self._id} Hours: {self._total_work_hours}")
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

    def _add_leadership_bonus(self, pay):
        bonus = pay * self._bonus_percent
        return decimal.Decimal(bonus)



