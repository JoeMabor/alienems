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


class TestTeamEmployeesUseCase(unittest.TestCase):
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
            employee=self.employee_1,
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
        self.use_case = self.use_case_factory.use_cases.team_employees_use_case()

    def test_retrieve_team_employees(self):
        """Retrieve all teams employees in the repository"""
        # test if response list length is 2
        team_employees = self.use_case.retrieve_all_teams_employees()
        self.assertEqual(len(team_employees), 1)
        # test first team id is 1
        self.assertEqual(team_employees[0].id, 1)

    def test_retrieve_team_employee(self):
        team_employee = self.use_case.retrieve_team_employee(1)
        self.assertEqual(team_employee.id, 1)
        self.assertEqual(team_employee.employee.name, "Brol")

    def test_retrieve_not_available_team_employee(self):
        with self.assertRaises(domain_exceptions.ObjectEntityDoesNotExist):
            self.use_case.retrieve_team_employee(2)

    def test_add_team_employee(self):
        """test adding team leader to a team without a team leader"""

        request_data = request_data_models.CreateTeamLeaderOrEmployeeRequestData(
            team_id=2,
            employee_id=2
        )

        new_team_employee = self.use_case.add_team_employee(request_data)
        self.assertEqual(len(self.use_case.retrieve_all_teams_employees()), 2)
        self.assertIsInstance(new_team_employee, TeamEmployeeEntity)
        self.assertEqual(new_team_employee.team.name, "Greys")
        self.assertEqual(new_team_employee.employee.id, 2)
        self.assertEqual(new_team_employee.employee.name, "Scox")

    def test_add_team_employee_invalid_requests(self):
        # add team employee with employee that doesnt exist
        with self.assertRaises(domain_exceptions.EmployeeDoesNotExist):
            request_data = request_data_models.CreateTeamLeaderOrEmployeeRequestData(
                team_id=2,
                employee_id=3,
            )
            self.use_case.add_team_employee(request_data)

        # add team employee with  team that doesn't exist
        with self.assertRaises(domain_exceptions.TeamDoesNotExist):
            request_data = request_data_models.CreateTeamLeaderOrEmployeeRequestData(
                team_id=3,
                employee_id=3,
            )
            self.use_case.add_team_employee(request_data)

        # add team employee to a team that already have a member of the team
        with self.assertRaises(domain_exceptions.EmployeeIsATeamMember):
            request_data = request_data_models.CreateTeamLeaderOrEmployeeRequestData(
                team_id=1,
                employee_id=1,
            )
            self.use_case.add_team_employee(request_data)

    def test_remove_team_employee(self):
        # first add employee to another team ( Employee must be in at least one team.)
        request_data = request_data_models.CreateTeamLeaderOrEmployeeRequestData(
            team_id=2,
            employee_id=1
        )
        new_team_employee = self.use_case.add_team_employee(request_data)
        deleted_team_employee = self.use_case.remove_team_employee(1)
        self.assertEqual(deleted_team_employee.id, 1)
        with self.assertRaises(domain_exceptions.ObjectEntityDoesNotExist):
            self.use_case.remove_team_employee(1)

    def test_remove_not_team_employee_invalid_requests(self):
        # remove Remove an employee that is only in one team from the team
        with self.assertRaises(domain_exceptions.EmployeeHasOneTeam):
            self.use_case.remove_team_employee(1)
        # attempt to delete team employee that is not in the repository
        with self.assertRaises(domain_exceptions.ObjectEntityDoesNotExist):
            self.use_case.remove_team_employee(3)


if __name__ == '__main__':
    unittest.main()




