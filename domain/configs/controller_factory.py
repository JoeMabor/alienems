"""
Module for configuration of django app. Create and inject dependencies
"""
# use cases
import domain.usecases.manage_teams_use_case as manage_use_cases
# controllers
import domain.adapters.controllers.manage_team_controller as team_controllers
from domain.usecases.repositories.team_repository import TeamRepoPort
from domain.usecases.repositories.employee_repository import EmployeeRepoPort


class ControllerFactory:
    def __init__(self, team_repo: TeamRepoPort,
                 employee_repo: EmployeeRepoPort
                 ):
        self._team_repo = team_repo
        self._employee_repo = employee_repo

    def manage_team_controller(self):
        return manage_use_cases.ManageTeamUseCase(
            team_repo=self._team_repo,
            employee_repo=self._employee_repo
        )

