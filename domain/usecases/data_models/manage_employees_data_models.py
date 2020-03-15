import decimal
import datetime


class EmployeePresenterData:
    """
    Employee data to to be presented to the view
    """
    def __init__(self,
                 id: int,
                 name: str,
                 employee_id: str,
                 hourly_rate: decimal.Decimal,
                 employee_type: int,
                 created_at: datetime.datetime,
                 updated_at: datetime.datetime,
                 pay,
                 is_a_leader
                 ):

        self.id = id
        self.name = name
        self.employee_id = employee_id
        self.hourly_rate = hourly_rate
        self.employee_type = employee_type
        self.created_at = created_at
        self.updated_at = updated_at
        self.is_a_leader = is_a_leader
        self.pay = pay


class CreateWorkArrangementData:
    """
    Data model for create new work arrangement
    """
    def __init__(self, percentage):
        pass


class CreateEmployeeRequestData:
    """
    Data model for creating new employees
    """
    def __init__(self,
                 name: str,
                 employee_id: str,
                 hourly_rate: decimal.Decimal,
                 employee_type: int,
                 team_id: int,
                 work_arrangement: int = None,
                 ):
        self.name = name
        self.employee_id = employee_id
        self.hourly_rate = hourly_rate
        self.employee_type = employee_type
        self.team_id = team_id
        self.work_arrangement = work_arrangement


class UpdateEmployeeMRequestData:
    """
    Data model for employee update requests. Can only update employee name, ID and hourly rate

    """
    def __init__(self,
                 id:int,
                 name: str,
                 employee_id: str,
                 hourly_rate: decimal.Decimal,
                 ):
        self.id = id
        self.name = name
        self.employee_id = employee_id
        self.hourly_rate = hourly_rate








