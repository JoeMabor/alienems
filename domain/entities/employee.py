"""
Employee entity with  employee business rules.
"""
import decimal
import datetime
from .validators import NotEmployeeEntityType
from .validators import EmployeeWorkTimeOutOfRange, EmployeeIDLengthNot5
from .validators import EmployeeDoesNotHaveATeam
import decimal


class EmployeeEntity:
    def __init__(self,
                 name: str,
                 employee_id: str,
                 hourly_rate,
                 employee_type: int,
                 is_a_leader: bool = False,
                 id: int = None,
                 created_at: datetime.datetime = None,
                 updated_at: datetime.datetime = None,
                 total_work_hours: int = None
                 ):

        self._id = id
        self._name = name
        self._employee_id = employee_id
        self._hourly_rate = decimal.Decimal(hourly_rate)
        self._employee_type = employee_type
        self._created_at = created_at
        self._updated_at = updated_at
        self._total_work_hours = total_work_hours
        self._is_a_leader = is_a_leader
        self._pay = None
        self._bonus_percent = decimal.Decimal(value=0.10)
        self._weeks_in_month = 4  # assume number of weeks in a month is 4

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, id: int):
        self._id = id

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
        length = len(str(employee_id))
        if length != 5:
            raise EmployeeIDLengthNot5()
        self._employee_id = employee_id

    @property
    def hourly_rate(self):
        return self._hourly_rate

    @hourly_rate.setter
    def hourly_rate(self, rate):
        # try to convert to float and raise TypeError exception if it fails
        try:
            r = float(rate)
        except ValueError:
            raise ValueError("Invalid input")
        if rate < 0:
            raise ValueError("Hourly rate can not be negative")
        self._hourly_rate = rate

    @property
    def employee_type(self):
        return self._employee_type

    @employee_type.setter
    def employee_type(self, employee_type):
        try:
            r = float(employee_type)
        except ValueError:
            raise ValueError("Invalid input")
        if not (employee_type == 1 or employee_type == 2):
            raise ValueError("Employee can be of type 1-FUll time or type 2- Part time")
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
        try:
            if hours < 0 or hours > 40:
                raise EmployeeWorkTimeOutOfRange()
            self._total_work_hours = hours
        except TypeError:
            raise TypeError("Invalid input")

    @property
    def is_a_leader(self):
        return self._is_a_leader

    @is_a_leader.setter
    def is_a_leader(self, is_leader: bool):
        self._is_a_leader = is_leader

    def calculate_pay(self):
        """Calculate monthly pay. weekly total hours * hourly rate * number of weeks in a month"""
        # calculate employee pay
        pay = self._total_work_hours * self._hourly_rate * self._weeks_in_month
        if self._is_a_leader:
            # leader get paid 10 % more
            pay += self.add_leadership_bonus(pay)
            print(F"Pay: {round(pay, 2)}")
        return pay.quantize(2)

    def is_part_time(self):
        """
        Return true if employee is a part time
        :return:
        """
        if self._employee_type == 2:
            return True
        else:
            return False

    def add_leadership_bonus(self, pay):
        try:
            if pay < 0:
                raise ValueError("Pay can not be negative number")
            bonus = pay * self._bonus_percent
        except TypeError:
            raise TypeError("Pay can not be non number")
        return bonus.quantize(2)



