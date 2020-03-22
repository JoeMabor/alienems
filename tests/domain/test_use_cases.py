import unittest
from tests.domain.repo.memory_repository_implementation import MemoryDB
from tests.domain.repo.memory_repository_implementation import TeamRepository
from tests.domain.repo.memory_repository_implementation import EmployeeRepository
from domain.entities.employee import EmployeeEntity
from domain.entities.team import TeamEntity
from domain.usecases.manage_teams_use_case import ManageTeamUseCase
import domain.entities.validators as domain_exceptions
import domain.usecases.data_models.request_data_models as request_data_models
import datetime


class TestManageTeamUseCase(unittest.TestCase):
    """Test cases for manage team"""
    def setUp(self):
        self.created_at = datetime.datetime.now()
        self.updated_at = datetime.datetime.now()
        self.created_at = datetime.datetime.now()
        self.updated_at = datetime.datetime.now()
        self.employee = EmployeeEntity(
            id=1,
            name="Brol",
            employee_id="00001",
            hourly_rate=50.00,
            employee_type=1,
            is_a_leader=True,
            created_at=self.created_at,
            updated_at=self.updated_at,
            total_work_hours=40
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
            1: self.employee
        }
        db = MemoryDB(teams=teams, employees=employees)
        team_repo = TeamRepository(db)
        employee_repo = EmployeeRepository(db)
        self.use_case = ManageTeamUseCase(team_repo=team_repo, employee_repo=employee_repo)

    def test_retrieve_all_teams(self):
        """Retrieve all teams in the repository"""
        # test if response list length is 2
        self.assertEqual(len(self.use_case.retrieve_all_teams()), 2)
        # test first team id is 1
        teams = self.use_case.retrieve_all_teams()
        # test first team id is 1
        self.assertEqual(teams[0].id, 1)
        self.assertEqual(teams[1].id, 2)

    def test_retrieve_team(self):
        team_1 = self.use_case.retrieve_team(1)
        self.assertEqual(team_1.id, 1)
        self.assertEqual(team_1.name, "Flatwoods monster")
        team_2 = self.use_case.retrieve_team(2)
        self.assertEqual(team_2.id, 2)

    def test_retrieve_team_not_available(self):
        with self.assertRaises(domain_exceptions.ObjectEntityDoesNotExist):
            self.use_case.retrieve_team(3)

    def test_create_team(self):
        # description and leader are None
        request_1 = request_data_models.CreateTeamRequestData(
            name="Nordic",
            description="Humanoids with stereotypical Nordic features",
        )

        new_team_1 = self.use_case.create_team(request_1)
        # check one more team is added
        self.assertEqual(len(self.use_case.retrieve_all_teams()), 3)
        self.assertIsInstance(new_team_1, TeamEntity)
        self.assertEqual(new_team_1.name, "Nordic")
        self.assertIsNotNone(new_team_1.created_at)
        self.assertIsNotNone(new_team_1.updated_at)
        self.assertIsNone(new_team_1.leader)
        self.assertFalse(new_team_1.has_a_leader)
        # create team with a leader
        request_2 = request_data_models.CreateTeamRequestData(
            name="Nordic",
            description="Humanoids with stereotypical Nordic features",
            leader_id=1
        )
        new_team_2 = self.use_case.create_team(request_2)
        self.assertIsNotNone(new_team_2.leader)
        self.assertTrue(new_team_2.has_a_leader)

    def test_update_team(self):
        request_data = request_data_models.UpdateTeamRequestData(
            id=1,
            name="Flatwoods monster",
            description="Tall humanoid blah blah ..."  # updated
        )
        updated_team = self.use_case.update_team(request_data)
        self.assertIsInstance(updated_team, TeamEntity)
        self.assertEqual(updated_team.description, "Tall humanoid blah blah ...")

    def test_update_not_available_team(self):
        # update team not in repository
        with self.assertRaises(domain_exceptions.ObjectEntityDoesNotExist):
            request_data = request_data_models.UpdateTeamRequestData(
                id=4,
                name="Flatwoods monster",
                description="Tall humanoid blah blah ..."  # updated
            )
            self.use_case.update_team(request_data)

    def test_delete_team(self):
        deleted_team = self.use_case.delete_team(team_pk=1)
        self.assertEqual(deleted_team.id, 1)
        with self.assertRaises(domain_exceptions.ObjectEntityDoesNotExist):
            self.use_case.retrieve_team(1)

    def test_delete_unavailable_team(self):
        with self.assertRaises(domain_exceptions.ObjectEntityDoesNotExist):
            self.use_case.delete_team(team_pk=3)






if __name__ == '__main__':
    unittest.main()




