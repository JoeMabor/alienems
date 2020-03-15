
class TeamLeaderEntity:
    """
    Entity that represent a team leader
    """
    def __init__(self, id: int, team_id, leader_id):
        self._id = id
        self._team = team_id
        self._leader = leader_id


    @property
    def id(self):
        return self._id

    @property
    def team(self):
        return self._team

    @property
    def leader(self):
        return self._leader
