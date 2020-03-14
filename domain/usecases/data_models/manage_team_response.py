"""
Manage team response data model classes
"""


class TeamModel:
    def __init__(self, id: int, name: str, description: str):
        self._id = id
        self._name = name
        self._description = description

    @property
    def id(self):
        return self._id

    @property
    def name(self):
        return self._name

    @property
    def description(self):
        return self._description

#
# class TeamsModel:
#     def __init__(self, teams_objects):
#         self._teams = []
#
#
#     @property
#     def teams(self):
#         return self._teams
#
#     def create_team_models(self):
#