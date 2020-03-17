from .employee import EmployeeEntity
from .team import TeamEntity


class TeamLeaderEntity:
    """
    Entity that represent a team leader
    """
    def __init__(self, leader: EmployeeEntity, teams: list):
        self._leader = leader
        self._teams = teams

    @property
    def teams(self):
        return self._teams

    @property
    def leader(self):
        return self._leader
