import unittest
from domain.entities.employee import EmployeeEntity
from domain.entities.team import TeamEntity
from domain.entities.team_employee import TeamEmployeeEntity
from domain.entities.team_leader import TeamLeaderEntity
from domain.entities.work_arrangment import WorkArrangementEntity
from domain.entities.work_time import WorkTimeEntity
from tests.domain.repo.memory_repository_implementation import MemoryDB
from tests.domain.app_config import UnittestsUseCasesFactory
import domain.entities.validators as domain_exceptions
import copy
import datetime


class TestManageWorkTimesUseCase(unittest.TestCase):
    """Test cases for manage team"""
    def setUp(self):
        self.created_at = datetime.datetime.now()
        self.updated_at = datetime.datetime.now()
        self.created_at = datetime.datetime.now()
        self.updated_at = datetime.datetime.now()
        self.employee_1 = EmployeeEntity(
            id=1,
            name="Brol",
            employee_id="00001",
            hourly_rate=50.00,
            employee_type=2,
            is_a_leader=True,
            created_at=self.created_at,
            updated_at=self.updated_at,
        )

        self.employee_2 = EmployeeEntity(
            id=2,
            name="Scox",
            employee_id="00001",
            hourly_rate=50.00,
            employee_type=2,
            is_a_leader=False,
            created_at=self.created_at,
            updated_at=self.updated_at,
            total_work_hours=20
        )

        self.team_1 = TeamEntity(
            id=1,
            name="Flatwoods monster",
            description="Tall humanoid with a spade-shaped head.",
            leader=None,
            created_at=self.created_at,
            updated_at=self.updated_at
        )

        self.team_2 = TeamEntity(
            id=2,
            name="Greys",
            description="Grey-skinned humanoids, usually 3–4 feet tall, hairless, with large heads.",
            leader=None,
            created_at=self.created_at + datetime.timedelta(seconds=10),
            updated_at=self.updated_at + datetime.timedelta(seconds=10)
        )

        self.work_arrangement = WorkArrangementEntity(
            id=1,
            percent=85,
            team=self.team_1,
            employee=self.employee_2
        )
        self.work_time = WorkTimeEntity(
            id=1,
            hours=34,
            employee=self.employee_2,
            work_arrangement=self.work_arrangement
        )
        teams = {
            1: self.team_1,
            2: self.team_2
        }
        employees = {
            1: self.employee_1,
            2: self.employee_2
        }
        work_arrangements = {1: self.work_arrangement}
        work_times = {1: self.work_time}
        team_employee = TeamEmployeeEntity(
            team=self.team_1,
            employee=self.employee_2,
            created_at=self.created_at,
            updated_at=self.updated_at
        )
        team_employees = {1: team_employee}

        team_leader = TeamLeaderEntity(
            team=self.team_1,
            leader=self.employee_1,
            created_at=self.created_at,
            updated_at=self.updated_at
        )
        team_leaders = {1: team_leader}

        self.db = MemoryDB(
            teams=teams,
            employees=employees,
            work_arrangements=work_arrangements,
            work_time=work_times,
            team_employees=team_employees,
            team_leaders=team_leaders
        )
        # copy object to avoid using the same db object in all test cases
        self.use_case_factory = UnittestsUseCasesFactory(db=copy.deepcopy(self.db))
        self.use_case = self.use_case_factory.use_cases.work_time_use_case()

    def test_retrieve_all_work_arrangements(self):
        """Retrieve all teams in the repository"""
        # test if response list length is 2
        work_times = self.use_case.retrieve_all_work_times()
        self.assertEqual(len(work_times), 1)
        # test first team id is 1
        self.assertEqual(work_times[0].id, 1)

    def test_retrieve_work_arrangement(self):
        work_time = self.use_case.retrieve_work_time(1)
        self.assertEqual(work_time.id, 1)
        self.assertEqual(work_time.hours, 34)

    def test_retrieve_employee_not_work_arrangements(self):
        with self.assertRaises(domain_exceptions.ObjectEntityDoesNotExist):
            self.use_case.retrieve_work_time(2)


if __name__ == '__main__':
    unittest.main()




