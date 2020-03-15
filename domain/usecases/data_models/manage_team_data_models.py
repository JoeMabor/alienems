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
        self.leader = leader



