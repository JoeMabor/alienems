import unittest
from domain.entities.employee import EmployeeEntity
from domain.entities.team import TeamEntity
from tests.domain.repo.memory_repository_implementation import MemoryDB
from tests.domain.app_config import UnittestsUseCasesFactory
import domain.entities.validators as domain_exceptions
import domain.usecases.data_models.request_data_models as request_data_models
import copy
import datetime


class TestManageEmployeesUseCase(unittest.TestCase):
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
            employee_type=1,
            is_a_leader=True,
            created_at=self.created_at,
            updated_at=self.updated_at,
            total_work_hours=40
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
        self.db = MemoryDB(teams=teams, employees=employees)
        # copy object to avoid using the same db object in all test cases
        self.use_case_factory = UnittestsUseCasesFactory(db=copy.deepcopy(self.db))
        self.use_case = self.use_case_factory.use_cases.manage_employee_use_case()

    def test_retrieve_all_employees(self):
        """Retrieve all teams in the repository"""
        # test if response list length is 2
        employees = self.use_case.retrieve_all_employees()
        self.assertEqual(len(employees), 2)
        # test first team id is 1

        # test first team id is 1
        self.assertEqual(employees[0].id, 1)
        self.assertEqual(employees[1].id, 2)

    def test_retrieve_employee(self):
        employee_1 = self.use_case.retrieve_employee(1)
        self.assertEqual(employee_1.id, 1)
        self.assertEqual(employee_1.name, "Brol")
        employee_2 = self.use_case.retrieve_employee(2)
        self.assertEqual(employee_2.id, 2)

    def test_retrieve_employee_not_available(self):
        with self.assertRaises(domain_exceptions.ObjectEntityDoesNotExist):
            self.use_case.retrieve_employee(3)

    def test_create_full_time_employee_valid_requests(self):

        # Full time employee
        request_data = request_data_models.CreateEmployeeRequestData(
            name="Crots",
            employee_id="00003",
            hourly_rate=50.50,
            employee_type=1,
            team_id=1
        )

        new_employee = self.use_case.create_employee(request_data)
        # check one more team is added
        self.assertEqual(len(self.use_case.retrieve_all_employees()), 3)
        self.assertIsInstance(new_employee, EmployeeEntity)
        self.assertEqual(new_employee.name, "Crots")
        self.assertIsNotNone(new_employee.created_at)
        self.assertIsNotNone(new_employee.updated_at)
        self.assertTrue(new_employee.is_a_leader)  # leader added if employee is added to team without employees
        # check correct work arrangement and work time are saved in repository
        wa_use_case = self.use_case_factory.use_cases.work_arrangements_use_case()
        work_arrangements = wa_use_case.retrieve_all_work_arrangements()
        # assert 1 work arrangement is added
        self.assertEqual(len(work_arrangements), 1)
        # assert work arrangement employee is the same with added employee
        self.assertEqual(work_arrangements[0].employee.employee_id, "00003")
        # assert work arrangement team is the same with specified employee team
        self.assertEqual(work_arrangements[0].team.id, 1)
        # assert work arrangement percent for full time employee is 100
        self.assertEqual(work_arrangements[0].percent, 100)
        wt_use_case = self.use_case_factory.use_cases.work_time_use_case()
        # assert 1 work work time is added
        work_times = wt_use_case.retrieve_all_work_times()
        self.assertEqual(len(work_times), 1)
        # assert work time employee is the same with added employee
        self.assertEqual(work_times[0].employee.employee_id, "00003")
        # assert work time work arrangement  is the same with specified added work arrangement
        self.assertEqual(work_times[0].work_arrangement.id, work_arrangements[0].id)
        # assert work time hours for full time employee is 40
        self.assertEqual(work_times[0].hours, 40)
        # add new employee in the same team
        request_data = request_data_models.CreateEmployeeRequestData(
            name="Zalzods",
            employee_id="00004",
            hourly_rate=60.50,
            employee_type=1,
            team_id=1
        )
        new_employee_2 = self.use_case.create_employee(request_data)
        self.assertIsInstance(new_employee_2, EmployeeEntity)
        self.assertEqual(new_employee_2.name, "Zalzods")
        self.assertIsNotNone(new_employee_2.created_at)
        self.assertIsNotNone(new_employee_2.updated_at)
        self.assertFalse(new_employee_2.is_a_leader)  # Team already have a leader

    def test_create_part_time_employee_valid_requests(self):
        # part time employee
        request_data = request_data_models.CreateEmployeeRequestData(
            name="Crots",
            employee_id="00003",
            hourly_rate=50.50,
            employee_type=2,
            team_id=1,
            work_arrangement=85
        )

        new_employee = self.use_case.create_employee(request_data)
        # check one more team is added
        self.assertEqual(len(self.use_case.retrieve_all_employees()), 3)
        self.assertIsInstance(new_employee, EmployeeEntity)
        self.assertEqual(new_employee.name, "Crots")
        self.assertIsNotNone(new_employee.created_at)
        self.assertIsNotNone(new_employee.updated_at)
        self.assertTrue(new_employee.is_a_leader)  # leader added if employee is added to team without employees
        # check correct work arrangement and work time are saved in repository
        wa_use_case = self.use_case_factory.use_cases.work_arrangements_use_case()
        work_arrangements = wa_use_case.retrieve_all_work_arrangements()
        # assert 1 work arrangement is added
        self.assertEqual(len(work_arrangements), 1)
        # assert work arrangement employee is the same with added employee
        self.assertEqual(work_arrangements[0].employee.employee_id, "00003")
        # assert work arrangement team is the same with specified employee team
        self.assertEqual(work_arrangements[0].team.id, 1)
        # assert work arrangement percent for part time employee is 85
        self.assertEqual(work_arrangements[0].percent, 85)
        wt_use_case = self.use_case_factory.use_cases.work_time_use_case()
        # assert 1 work work time is added
        work_times = wt_use_case.retrieve_all_work_times()
        self.assertEqual(len(work_times), 1)
        # assert work time employee is the same with added employee
        self.assertEqual(work_times[0].employee.employee_id, "00003")
        # assert work time work arrangement  is the same with specified added work arrangement
        self.assertEqual(work_times[0].work_arrangement.id, work_arrangements[0].id)
        # assert work time hours for full time employee is 40
        self.assertEqual(work_times[0].hours, 34)

    def test_create_employee_in_valid_requests(self):
        # add employee with with existing employee ID
        with self.assertRaises(domain_exceptions.EmployeeIDIsNotUnique):
            request_data = request_data_models.CreateEmployeeRequestData(
                name="Crots",
                employee_id="00001",  # adding in setup
                hourly_rate=50.50,
                employee_type=1,
                team_id=1
            )
            self.use_case.create_employee(request_data)

        # add employee with team that doesn't exist
        with self.assertRaises(domain_exceptions.TeamDoesNotExist):
            request_data = request_data_models.CreateEmployeeRequestData(
                name="Crots",
                employee_id="00003",  # adding in setup
                hourly_rate=50.50,
                employee_type=1,
                team_id=3
            )
            self.use_case.create_employee(request_data)

        # add part time employee without work arrangement
        with self.assertRaises(domain_exceptions.WorkArrangementPercentageNull):
            request_data = request_data_models.CreateEmployeeRequestData(
                name="Crots",
                employee_id="00003",  # adding in setup
                hourly_rate=50.50,
                employee_type=2,
                team_id=1
            )
            self.use_case.create_employee(request_data)

    def test_update_employee(self):
        # can only update name, employee_id and hourly rate here.
        # Employee work time and work arrangement can be updated in respective use cases
        request_data = request_data_models.UpdateEmployeeRequestData(
            id=1,
            name="Brol Grol",
            employee_id="00005",
            hourly_rate=100.00
        )

        updated_employee = self.use_case.update_employee(request_data)
        self.assertIsInstance(updated_employee, EmployeeEntity)
        self.assertEqual(updated_employee.name, "Brol Grol")
        self.assertEqual(updated_employee.employee_id, "00005")
        self.assertEqual(updated_employee.hourly_rate, 100.00)

    def test_update_not_available_employee(self):
        # update team not in repository
        with self.assertRaises(domain_exceptions.ObjectEntityDoesNotExist):
            request_data = request_data_models.UpdateEmployeeRequestData(
                id=3,
                name="Brol Grol",
                employee_id="00005",
                hourly_rate=100.00
            )
            self.use_case.update_employee(request_data)

    def test_delete_employee(self):
        deleted_employee = self.use_case.delete_employee(1)
        self.assertEqual(deleted_employee.id, 1)
        with self.assertRaises(domain_exceptions.ObjectEntityDoesNotExist):
            self.use_case.retrieve_employee(1)

    def test_delete_not_available_employee(self):
        # update team not in repository
        with self.assertRaises(domain_exceptions.ObjectEntityDoesNotExist):
            self.use_case.delete_employee(3)


if __name__ == '__main__':
    unittest.main()




