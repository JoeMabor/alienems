import unittest
from domain.entities.employee import EmployeeEntity
from domain.entities.team import TeamEntity
from domain.entities.team_employee import TeamEmployeeEntity
from domain.entities.team_leader import TeamLeaderEntity
from tests.domain.repo.memory_repository_implementation import MemoryDB
from tests.domain.app_config import UnittestsUseCasesFactory
import domain.entities.validators as domain_exceptions
import domain.usecases.data_models.request_data_models as request_data_models
import copy
import datetime


class TestTeamLeadersUseCase(unittest.TestCase):
    """Test cases for manage team leaders"""
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

        teams = {
            1: self.team_1,
            2: self.team_2
        }
        employees = {
            1: self.employee_1,
            2: self.employee_2
        }

        team_employee = TeamEmployeeEntity(
            id=1,
            team=self.team_1,
            employee=self.employee_2,
            created_at=self.created_at,
            updated_at=self.updated_at
        )
        team_employees = {1: team_employee}

        team_leader = TeamLeaderEntity(
            id=1,
            team=self.team_1,
            leader=self.employee_1,
            created_at=self.created_at,
            updated_at=self.updated_at
        )
        team_leaders = {1: team_leader}

        self.db = MemoryDB(
            teams=teams,
            employees=employees,
            team_employees=team_employees,
            team_leaders=team_leaders
        )
        # copy object to avoid using the same db object in all test cases
        self.use_case_factory = UnittestsUseCasesFactory(db=copy.deepcopy(self.db))
        self.use_case = self.use_case_factory.use_cases.team_leaders_use_case()

    def test_retrieve_team_leaders(self):
        """Retrieve all teams leaders in the repository"""
        # test if response list length is 2
        team_leaders = self.use_case.retrieve_all_teams_leaders()
        self.assertEqual(len(team_leaders), 1)
        # test first team id is 1
        self.assertEqual(team_leaders[0].id, 1)

    def test_retrieve_team_leader(self):
        team_leader = self.use_case.retrieve_team_leader(1)
        self.assertEqual(team_leader.id, 1)
        self.assertEqual(team_leader.leader.name, "Brol")

    def test_retrieve_not_available_team_leader(self):
        with self.assertRaises(domain_exceptions.ObjectEntityDoesNotExist):
            self.use_case.retrieve_team_leader(2)

    def test_assign_team_leader_employee(self):
        """test adding team leader to a team without a team leader"""

        request_data = request_data_models.CreateTeamLeaderOrEmployeeRequestData(
            team_id=2,
            employee_id=2
        )

        new_team_leader = self.use_case.assign_team_leader(request_data)
        self.assertEqual(len(self.use_case.retrieve_all_teams_leaders()), 2)
        self.assertIsInstance(new_team_leader, TeamLeaderEntity)
        self.assertEqual(new_team_leader.team.name, "Greys")
        self.assertEqual(new_team_leader.leader.id, 2)
        self.assertEqual(new_team_leader.leader.name, "Scox")

    def test_assign_team_leader_invalid_requests(self):
        # assign team leader with employee that doesnt exist
        with self.assertRaises(domain_exceptions.EmployeeDoesNotExist):
            request_data = request_data_models.CreateTeamLeaderOrEmployeeRequestData(
                team_id=2,
                employee_id=3,
            )
            self.use_case.assign_team_leader(request_data)

        # assign team leader with  team that doesn't exist
        with self.assertRaises(domain_exceptions.TeamDoesNotExist):
            request_data = request_data_models.CreateTeamLeaderOrEmployeeRequestData(
                team_id=3,
                employee_id=3,
            )
            self.use_case.assign_team_leader(request_data)

        # assign team leader to a team that already have a leader
        with self.assertRaises(domain_exceptions.TeamHasALeader):
            request_data = request_data_models.CreateTeamLeaderOrEmployeeRequestData(
                team_id=1,
                employee_id=2,
            )
            self.use_case.assign_team_leader(request_data)

    def test_change_team_leader(self):
        # change team 1 leader from employee 1 to employee two
        request_data = request_data_models.UpdateTeamLeaderRequestData(
            id=1,
            team_id=1,
            employee_id=2,
        )
        new_team_leader = self.use_case.change_team_leader(request_data)
        self.assertIsInstance(new_team_leader, TeamLeaderEntity)
        self.assertEqual(new_team_leader.team.id, 1)
        self.assertEqual(new_team_leader.leader.id, 2)

    def test_change_team_leader_in_valid_requests(self):
        # Change team leader with team leader that doesnt exist
        with self.assertRaises(domain_exceptions.ObjectEntityDoesNotExist):
            request_data = request_data_models.UpdateTeamLeaderRequestData(
                id=3,
                team_id=2,
                employee_id=3,
            )
            self.use_case.change_team_leader(request_data)

        # Change team leader with employee that doesnt exist
        with self.assertRaises(domain_exceptions.EmployeeDoesNotExist):
            request_data = request_data_models.UpdateTeamLeaderRequestData(
                id=1,
                team_id=2,
                employee_id=3,
            )
            self.use_case.change_team_leader(request_data)

        # Change team leader with  team that doesn't exist
        with self.assertRaises(domain_exceptions.TeamDoesNotExist):
            request_data = request_data_models.UpdateTeamLeaderRequestData(
                id=1,
                team_id=3,
                employee_id=1,
            )
            self.use_case.change_team_leader(request_data)


if __name__ == '__main__':
    unittest.main()




