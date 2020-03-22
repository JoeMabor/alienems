"""
This module defines all data model for requests that controllers will accept and pass to use cases
"""

import decimal
import datetime


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


class CreateWorkArrangementData:
    """
    Data model for create new work arrangement
    """
    def __init__(self, percent, employee_id, team_id, remarks=None):
        self.percent = percent
        self.remarks = remarks
        self.employee_id = employee_id
        self.team_id = team_id


class UpdateWorkArrangementData:
    """
    Data model for create new work arrangement
    """
    def __init__(self, id, percent, employee_id, team_id, remarks=None):
        self.id = id
        self.percent = percent
        self.remarks = remarks
        self.employee_id = employee_id
        self.team_id = team_id


class CreateTeamRequestData:
    def __init__(self, name, description=None, leader_id=None):
        self.name = name
        self.description = description
        self.leader_id = leader_id


class UpdateTeamRequestData:
    def __init__(self, id: int, name, description= None):
        self.id = id
        self.name = name
        self.description = description


class TeamLeaderOrEmployeeRequestData:
    """
    Data request for assigning  a team leader, adding and removing team employee
    """
    def __init__(self, team_id, employee_id):
        self.team_id = team_id
        self.employee_id = employee_id


class UpdateTeamLeaderRequestData:
    """
    Data request for assigning  a team leader, adding and removing team employee
    """
    def __init__(self, id, team_id, employee_id):
        self.id = id
        self.team_id = team_id
        self.employee_id = employee_id
