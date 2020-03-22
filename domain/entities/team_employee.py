
from .employee import EmployeeEntity
from .team import TeamEntity
import datetime

class TeamEmployeeEntity:
    def __init__(self,
                 team: TeamEntity,
                 employee: EmployeeEntity,
                 id: int = None,
                 created_at: datetime.datetime = None,
                 updated_at: datetime.datetime = None
                 ):
        self._id = id
        self._team = team
        self._employee = employee
        self._created_at = created_at
        self._updated_at = updated_at

    @property
    def id(self):
        return self._id

    @property
    def employee(self):
        return self._employee

    @property
    def team(self):
        return self._team

    @property
    def created_at(self):
        return self._created_at

    @property
    def updated_at(self):
        return self._updated_at
