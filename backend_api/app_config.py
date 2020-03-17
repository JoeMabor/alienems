from domain.configs.controller_factory import ControllerFactory
from .repositories.team_repository import TeamRepoPortImp
from .repositories.employee_repository import EmployeeRepoPortImp
from .repositories.team_leader_repository import TeamLeaderRepoImpl
from .repositories.team_employee_repository import TeamEmployeeRepoImpl
from .repositories.work_arrangement_repository import WorkArrangementRepoImpl
from .repositories.work_time_repository import WorkTimeRepoImpl

# injecting repositories dependencies in respective controllers
CONTROLLERS = ControllerFactory(
    team_repo=TeamRepoPortImp(),
    employee_repo=EmployeeRepoPortImp(),
    work_arrangement_repo=WorkArrangementRepoImpl(),
    work_time_repo=WorkTimeRepoImpl(),
    team_employee_repo=TeamEmployeeRepoImpl(),
    team_leader_repo=TeamLeaderRepoImpl()
)
