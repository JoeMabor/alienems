"""
Module for configuration of django app. Create and inject dependencies
"""
# use cases
from domain.usecases.manage_teams_use_case import ManageTeamUseCase
from domain.usecases.manage_employees_use_case import ManageEmployeeUseCase
# controllers
from domain.adapters.controllers.manage_teams_controller import ManageTeamController
from domain.adapters.controllers.manage_employees_controller import ManageEmployeesController
from domain.usecases.repositories.team_repository import TeamRepoPort
from domain.usecases.repositories.team_employees_repository import TeamEmployeeRepoPort
from domain.usecases.repositories.team_leader_repository import TeamLeaderRepoPort
from domain.usecases.repositories.employee_repository import EmployeeRepoPort
from domain.usecases.repositories.work_arrangement_repository import WorkArrangementRepoPort
from domain.usecases.repositories.work_time_repository import WorkTimeRepoPort


class ControllerFactory:
    def __init__(self, team_repo: TeamRepoPort,
                 employee_repo: EmployeeRepoPort,
                 team_employee_repo: TeamEmployeeRepoPort,
                 team_leader_repo: TeamLeaderRepoPort,
                 work_time_repo: WorkTimeRepoPort,
                 work_arrangement_repo: WorkArrangementRepoPort,
                 ):
        self._team_repo = team_repo
        self._employee_repo = employee_repo
        self._work_arrangement_repo = work_arrangement_repo
        self._work_time_repo = work_time_repo
        self._team_employee_repo = team_employee_repo
        self._team_leader_repo = team_leader_repo

    def manage_teams_controller(self):
        """
        Create  manages team controller ans inject repositories dependencies to the ManageTeamUSeCase
        :return:
        """
        return ManageTeamController(
            ManageTeamUseCase(
                team_repo=self._team_repo,
                employee_repo=self._employee_repo
            )

        )

    def manage_employee_controller(self):
        """
        Create  manage employees controller ans inject repositories dependencies to the ManageEmployeeUSeCase
        :return:
        """
        return ManageEmployeesController(ManageEmployeeUseCase(
            employee_repo=self._employee_repo,
            work_arrangement_repo=self._work_arrangement_repo,
            work_time_repo=self._work_time_repo,
            team_employee_repo=self._team_employee_repo,
            team_leader_repo=self._team_leader_repo
        ))
