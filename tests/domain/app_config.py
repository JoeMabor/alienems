from tests.domain.repo.memory_repository_implementation import MemoryDB
from tests.domain.repo.memory_repository_implementation import TeamRepository
from tests.domain.repo.memory_repository_implementation import EmployeeRepository
from tests.domain.repo.memory_repository_implementation import TeamEmployeeRepository
from tests.domain.repo.memory_repository_implementation import TeamLeaderRepository
from tests.domain.repo.memory_repository_implementation import WorkTimeRepository
from tests.domain.repo.memory_repository_implementation import WorkArrangementRepository
from domain.configs.use_case_factory import UseCaseFactory


class UnittestsUseCasesFactory:
    def __init__(self, db):
        self.db = db
        team_repo = TeamRepository(db)
        employee_repo = EmployeeRepository(db)
        work_arrangement_repo = WorkArrangementRepository(db)
        work_time_repo = WorkTimeRepository(db)
        team_employee_repo = TeamEmployeeRepository(db)
        team_leader_repo = TeamLeaderRepository(db)
        self._use_cases = UseCaseFactory(
            employee_repo=employee_repo,
            team_repo=team_repo,
            team_employee_repo=team_employee_repo,
            team_leader_repo=team_leader_repo,
            work_arrangement_repo=work_arrangement_repo,
            work_time_repo=work_time_repo
        )

    @property
    def use_cases(self):
        return self._use_cases
