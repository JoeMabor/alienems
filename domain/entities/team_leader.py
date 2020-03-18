from .employee import EmployeeEntity
from .team import TeamEntity


class TeamLeaderEntity:
    """
    Entity that represent a team leader
    """
    def __init__(self, id:int, leader: EmployeeEntity, team: TeamEntity):
        self._id = id
        self._leader = leader
        self._team = team

    @property
    def id(self):
        return self._id

    @property
    def team(self):
        return self._team

    @property
    def leader(self):
        return self._leader
