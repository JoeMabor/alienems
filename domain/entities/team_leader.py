from .employee import EmployeeEntity
from .team import TeamEntity
import datetime


class TeamLeaderEntity:
    """
    Entity that represent a team leader
    """
    def __init__(self,
                 leader: EmployeeEntity,
                 team: TeamEntity,
                 id: int=None,
                 created_at: datetime.datetime = None,
                 updated_at: datetime.datetime = None
                 ):
        self._id = id
        self._leader = leader
        self._team = team
        self._created_at = created_at
        self._updated_at = updated_at

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, id: int):
        self._id = id

    @property
    def team(self):
        return self._team

    @property
    def leader(self):
        return self._leader

    @property
    def created_at(self):
        return self._created_at

    @property
    def updated_at(self):
        return self._updated_at
