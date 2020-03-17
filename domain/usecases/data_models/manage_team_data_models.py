"""
Data models for manage team use case
"""
from .manage_employees_data_models import EmployeePresenterData
import datetime


class CreateTeamRequestData:
    def __init__(self,name, id: int = None, description= None, leader_id = None):
        self.id = id
        self.name = name
        self.description = description
        self.leader_id = leader_id


class PresentTeamRequestData:
    def __init__(self,
                 name,
                 created_at: datetime.datetime,
                 updated_at: datetime.datetime,
                 description=None,
                 leader: EmployeePresenterData = None
                 ):
        self.name = name
        self.description = description
        self.created_at = created_at
        self.updated_at = updated_at
        print(F"Team leader in Data model: {leader}")
        kkk
        self.leader = leader


class PresentTeamLeaderRequestData:
    """
    Data format to present Team leader
    """
    def __init__(self, leader: EmployeePresenterData, team: PresentTeamRequestData):
        self.leader = leader
        self.team = team


class TeamLeaderRequestData:
    """
    Data request for assigning  a team leader.
    """
    def __init__(self, team_id, employee_id):
        self.team_id = team_id
        self.employee_id = employee_id


