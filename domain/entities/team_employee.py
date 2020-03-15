
class TeamEmployeeEntity:
    def __init__(self, id: int, employee_id: int, team_id: int):
        self._id = id
        self._employee_id = employee_id
        self._team_id = team_id

    @property
    def id(self):
        return self._id

    @property
    def employee_id(self):
        return self._employee_id

    @property
    def team_id(self):
        return self._team_id
