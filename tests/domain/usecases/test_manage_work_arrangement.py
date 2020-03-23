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
import domain.usecases.data_models.request_data_models as request_data_models
import copy
import datetime


class TestManageWorkArrangementsUseCase(unittest.TestCase):
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
        self.use_case = self.use_case_factory.use_cases.work_arrangements_use_case()

    def test_retrieve_all_work_arrangements(self):
        """Retrieve all teams in the repository"""
        # test if response list length is 2
        work_arrangements = self.use_case.retrieve_all_work_arrangements()
        self.assertEqual(len(work_arrangements), 1)
        # test first team id is 1
        self.assertEqual(work_arrangements[0].id, 1)

    def test_retrieve_work_arrangement(self):
        work_arrangements = self.use_case.retrieve_work_arrangement(1)
        self.assertEqual(work_arrangements.id, 1)
        self.assertEqual(work_arrangements.percent, 85)

    def test_retrieve_employee_not_work_arrangements(self):
        with self.assertRaises(domain_exceptions.ObjectEntityDoesNotExist):
            self.use_case.retrieve_work_arrangement(2)

    def test_create_arrangement_not_team_employee(self):
        """Add work arrangement for an employee is not a team member. An employee will be added to team employee"""

        request_data = request_data_models.CreateWorkArrangementData(
            percent=10,
            employee_id=2,
            team_id=2,
            remarks="Additional work arrangement"
        )

        new_wa = self.use_case.add_work_arrangement(request_data)
        # check one more team is added
        self.assertEqual(len(self.use_case.retrieve_all_work_arrangements()), 2)
        self.assertIsInstance(new_wa, WorkArrangementEntity)
        self.assertEqual(new_wa.percent,  10)
        self.assertEqual(new_wa.employee.id, 2)
        self.assertEqual(new_wa.employee.id, 2)
        wt_use_case = self.use_case_factory.use_cases.work_time_use_case()
        # assert 1 work work time is added
        work_times = wt_use_case.retrieve_all_work_times()
        self.assertEqual(len(work_times), 2) # there is already one repository
        # assert work time employee is the same with added employee
        self.assertEqual(work_times[0].employee.id, 2)
        # assert work time work arrangement  is the same with specified added work arrangement
        self.assertEqual(work_times[1].work_arrangement.id, new_wa.id)
        # assert work time hours for full time employee is 40
        self.assertEqual(work_times[1].hours, 4)  # 4 hours 10% * 40
        # add new employee in the same team

    def test_create_arrangement_team_employee(self):
        """Add work arrangement for an employee is already a team member"""

        # Full time employee
        request_data = request_data_models.CreateWorkArrangementData(
            percent=85,
            employee_id=1,
            team_id=1,
            remarks="Additional work arrangement"
        )

        new_wa = self.use_case.add_work_arrangement(request_data)
        # check one more team is added
        self.assertEqual(len(self.use_case.retrieve_all_work_arrangements()), 2)
        self.assertIsInstance(new_wa, WorkArrangementEntity)
        self.assertEqual(new_wa.percent,  85)
        self.assertEqual(new_wa.employee.id, 1)
        self.assertEqual(new_wa.employee.id, 1)
        wt_use_case = self.use_case_factory.use_cases.work_time_use_case()
        # assert 1 work work time is added
        work_times = wt_use_case.retrieve_all_work_times()
        self.assertEqual(len(work_times), 2) # there is already one repository
        # assert work time employee is the same with added employee
        self.assertEqual(work_times[0].employee.id, 2)
        # assert work time work arrangement  is the same with specified added work arrangement
        self.assertEqual(work_times[1].work_arrangement.id, new_wa.id)
        # assert work time hours for full time employee is 40
        self.assertEqual(work_times[1].hours, 34)  # 4 hours 85% * 40
        # add new employee in the same team

    def test_work_arrangement_in_valid_requests(self):
        # add work arrangement with employee that doesnt exist
        with self.assertRaises(domain_exceptions.ObjectEntityDoesNotExist):
            request_data = request_data_models.CreateWorkArrangementData(
                percent=85,
                employee_id=3,
                team_id=1,
                remarks="Additional work arrangement"
            )
            self.use_case.add_work_arrangement(request_data)

        # add employee work arrangement in   team that doesn't exist
        with self.assertRaises(domain_exceptions.TeamDoesNotExist):
            request_data = request_data_models.CreateWorkArrangementData(
                percent=85,
                employee_id=1,
                team_id=3,
                remarks="Additional work arrangement"
            )
            self.use_case.add_work_arrangement(request_data)

        # add employee work arrangement with percent that total to more than 40 hours total employee work time
        with self.assertRaises(domain_exceptions.Max40HoursExceeded):
            request_data = request_data_models.CreateWorkArrangementData(
                percent=30,
                employee_id=2,
                team_id=2,
                remarks="Additional work arrangement"
            )
            self.use_case.add_work_arrangement(request_data)

        # Add employee work arrangement in the same team employee already have work arrangement
        with self.assertRaises(domain_exceptions.MultipleWorkArrangementInOneTeam):
            request_data_3 = request_data_models.CreateWorkArrangementData(
                percent=5,
                employee_id=2,
                team_id=1,
                remarks="Additional work arrangement"
            )
            self.use_case.add_work_arrangement(request_data_3)

    def test_update_work_arrangement_in_the_same_team(self):
        # can only update name, employee_id and hourly rate here.
        # Employee work time and work arrangement can be updated in respective use cases
        request_data = request_data_models.UpdateWorkArrangementData(
            id=1,
            percent=75,
            employee_id=2,
            team_id=1
        )
        updated_wa = self.use_case.update_work_arrangement(request_data)
        self.assertIsInstance(updated_wa, WorkArrangementEntity)
        self.assertEqual(updated_wa.percent, 75)

    def test_update_work_arrangement_change_to_another_team(self):
        # can only update name, employee_id and hourly rate here.
        # Employee work time and work arrangement can be updated in respective use cases
        request_data = request_data_models.UpdateWorkArrangementData(
            id=1,
            percent=75,
            employee_id=2,
            team_id=2
        )
        updated_wa = self.use_case.update_work_arrangement(request_data)
        self.assertIsInstance(updated_wa, WorkArrangementEntity)
        self.assertEqual(updated_wa.percent, 75)
        self.assertEqual(updated_wa.team.id, 2)

    def test_update_work_arrangement_in_valid_requests(self):
        # update work arrangement  that doesnt exist
        with self.assertRaises(domain_exceptions.ObjectEntityDoesNotExist):
            request_data = request_data_models.UpdateWorkArrangementData(
                id=2,
                percent=85,
                employee_id=3,
                team_id=1
            )
            self.use_case.update_work_arrangement(request_data)

        # update work arrangement with employee that doesnt exist
        with self.assertRaises(domain_exceptions.ObjectEntityDoesNotExist):
            request_data = request_data_models.UpdateWorkArrangementData(
                id=1,
                percent=85,
                employee_id=3,
                team_id=1
            )
            self.use_case.update_work_arrangement(request_data)

        # update employee work arrangement in   team that doesn't exist
        with self.assertRaises(domain_exceptions.TeamDoesNotExist):
            request_data = request_data_models.UpdateWorkArrangementData(
                id=1,
                percent=85,
                employee_id=1,
                team_id=3,
                remarks="Additional work arrangement"
            )
            self.use_case.update_work_arrangement(request_data)

        # update employee work arrangement with percent that total to more than 40 hours total employee work time
        with self.assertRaises(domain_exceptions.Max40HoursExceeded):
            request_data = request_data_models.UpdateWorkArrangementData(
                id=1,
                percent=130,
                employee_id=2,
                team_id=2,
                remarks="Additional work arrangement"
            )
            self.use_case.update_work_arrangement(request_data)

    def test_delete_work_arrangement(self):
        deleted_wa = self.use_case.delete_work_arrangement(1)
        self.assertEqual(deleted_wa.id, 1)
        with self.assertRaises(domain_exceptions.ObjectEntityDoesNotExist):
            self.use_case.retrieve_work_arrangement(1)

    def test_delete_not_available_employee(self):
        # update team not in repository
        with self.assertRaises(domain_exceptions.ObjectEntityDoesNotExist):
            self.use_case.delete_work_arrangement(3)


if __name__ == '__main__':
    unittest.main()




