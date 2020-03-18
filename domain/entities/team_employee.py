
from .employee import EmployeeEntity
from .team import TeamEntity


class TeamEmployeeEntity:
    def __init__(self, id: int, team: TeamEntity, employee: EmployeeEntity):
        self._id = id
        self._team = team
        self._employee = employee

    @property
    def id(self):
        return self._id

    @property
    def employee(self):
        return self._employee

    @property
    def team(self):
        return self._team
