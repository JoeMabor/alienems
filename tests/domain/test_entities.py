import unittest
from domain.entities.employee import EmployeeEntity
from domain.entities.team import TeamEntity
from domain.entities.work_arrangment import WorkArrangementEntity
from domain.entities.work_time import WorkTimeEntity
from domain.entities.team_employee import TeamEmployeeEntity
import domain.entities.validators  as domain_validators
import datetime


class TestTeamEntity(unittest.TestCase):
    """Test cases for TeamEntity"""
    def setUp(self):
        self.created_at = datetime.datetime.now()
        self.updated_at = datetime.datetime.now()
        self.leader = EmployeeEntity(
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
            name="Greys",
            description="Grey-skinned humanoids, usually 3–4 feet tall, hairless, with large heads."
        )

        self.team_2 = TeamEntity(
            id=1,
            name="Flatwoods monster",
            description="Tall humanoid with a spade-shaped head.",
            leader=self.leader,
            created_at=self.created_at,
            updated_at=self.updated_at
        )

    def test_id(self):
        """Test id gives correct values"""
        self.assertIsNone(self.team_1.id)
        self.assertEqual(self.team_2.id, 1)

    def test_name(self):
        """Test name given correct values"""
        self.assertEqual(self.team_1.name, "Greys")
        self.assertEqual(self.team_2.name, "Flatwoods monster")

    def test_description(self):
        """Test that description gives correct values"""
        self.assertEqual(self.team_1.description,
                         "Grey-skinned humanoids, usually 3–4 feet tall, hairless, with large heads.")
        self.assertEqual(self.team_2.description, "Tall humanoid with a spade-shaped head.")

    def test_leader(self):
        """Test that leader gives correct values and is of correct class"""
        self.assertIsNone(self.team_1.leader)
        self.assertIsInstance(self.team_2.leader, EmployeeEntity)
        self.assertEqual(self.team_2.leader, self.leader)

    def test_set_leader(self):
        """Test that leader gives correct values and is of correct class"""
        self.team_1.leader = self.leader
        self.assertIsInstance(self.team_1.leader, EmployeeEntity)
        self.assertEqual(self.team_1.leader, self.leader)

    def test_has_a_leader(self):
        """Test if team has a leader give correct boolean values"""
        self.assertFalse(self.team_1.has_a_leader)
        self.assertTrue(self.team_2.has_a_leader)

    def test_created_at(self):
        """Test if created_at give correct values"""
        self.assertIsNone(self.team_1.created_at)
        self.assertEqual(self.team_2.created_at, self.created_at)

    def test_updated_at(self):
        """Test if updated give correct values"""
        self.assertIsNone(self.team_1.updated_at)
        self.assertEqual(self.team_2.updated_at, self.updated_at)

    def test_updated_at_setter(self):
        """Test if updated_at setter set values correect"""
        new_updated_at_1 = datetime.datetime.now() + datetime.timedelta(days=1)
        new_updated_at_2 = datetime.datetime.now() + datetime.timedelta(days=2)
        self.team_1.updated_at = new_updated_at_1
        self.team_2.updated_at = new_updated_at_2
        self.assertEqual(self.team_1.updated_at, new_updated_at_1)
        self.assertEqual(self.team_2.updated_at, new_updated_at_2)


class TestEmployeeEntity(unittest.TestCase):
    """Test cases for EmployeeEntity"""

    def setUp(self):
        self.created_at = datetime.datetime.now()
        self.updated_at = datetime.datetime.now()
        self.employee_1 = EmployeeEntity(
            name="Scurrod",
            employee_id="00001",
            employee_type=1,
            hourly_rate=100.00
        )
        self.employee_2 = EmployeeEntity(
            id=1,
            name="Brol",
            employee_id="00002",
            hourly_rate=50.00,
            employee_type=2,
            is_a_leader=False,
            created_at=self.created_at,
            updated_at=self.updated_at,
            total_work_hours=20
        )

        self.employee_3 = EmployeeEntity(
            id=1,
            name="Brol",
            employee_id="00002",
            hourly_rate=50.00,
            employee_type=1,
            is_a_leader=True,
            created_at=self.created_at,
            updated_at=self.updated_at,
            total_work_hours=40
        )

    def test_id(self):
        """Test id gives correct values"""
        self.assertIsNone(self.employee_1.id)
        self.assertEqual(self.employee_2.id, 1)

    def test_name(self):
        """Test if name gives correct values"""
        self.assertEqual(self.employee_1.name, "Scurrod")
        self.assertEqual(self.employee_2.name, "Brol")

    def test_employee_id(self):
        """Test if employee id give correct values"""
        self.assertEqual(self.employee_1.employee_id, "00001")
        self.assertEqual(self.employee_2.employee_id, "00002")

    def test_hourly_rate(self):
        """Test if hourly rate gives correct values"""
        self.assertEqual(self.employee_1.hourly_rate, 100.00)
        self.assertEqual(self.employee_2.hourly_rate, 50.00)

    def test_employee_type(self):
        """Test if employee type gives correct values"""
        self.assertEqual(self.employee_1.employee_type, 1)
        self.assertEqual(self.employee_2.employee_type, 2)

    def test_created_at(self):
        """Test if created_at give correct values"""
        self.assertIsNone(self.employee_1.created_at)
        self.assertEqual(self.employee_2.created_at, self.created_at)

    def test_updated_at(self):
        """Test if updated give correct values"""
        self.assertIsNone(self.employee_1.updated_at)
        self.assertEqual(self.employee_2.updated_at, self.updated_at)

    def test_updated_at_setter(self):
        """Test if updated_at setter set values correect"""
        new_updated_at_1 = datetime.datetime.now() + datetime.timedelta(days=1)
        new_updated_at_2 = datetime.datetime.now() + datetime.timedelta(days=2)
        self.employee_1.updated_at = new_updated_at_1
        self.employee_2.updated_at = new_updated_at_2
        self.assertEqual(self.employee_1.updated_at, new_updated_at_1)
        self.assertEqual(self.employee_2.updated_at, new_updated_at_2)

    def test_add_leadership_bonus_valid_inputs(self):
        """Test that add_leadership bonus calculate correct bonus. bonus = pay * 0.1"""
        self.assertEqual(self.employee_1.add_leadership_bonus(0), 0)
        self.assertEqual(self.employee_1.add_leadership_bonus(1), 0)
        self.assertEqual(self.employee_1.add_leadership_bonus(400), 40.00)

    def test_add_leadership_bonus_invalid_inputs(self):
        """Test that invalid inputs produced correct Exception"""
        with self.assertRaises(TypeError):
            self.employee_1.add_leadership_bonus("abc")

        with self.assertRaises(ValueError):
            self.employee_1.add_leadership_bonus(-1)

    def test_calculate_pay(self):
        """Test pay is calculated correctly"""
        # part time employee and not a leader
        self.assertEqual(self.employee_2.calculate_pay(), 1000.00)
        # a leader and full time employee
        self.assertEqual(self.employee_3.calculate_pay(), 2200.00)

    def test_pay(self):
        """Test if pay gives correct calculated pay as values total hours"""
        # total work hours not given
        self.assertIsNone(self.employee_1.pay)
        # part time employee and not a leader
        self.assertEqual(self.employee_2.pay, 1000.00)
        # a leader and full time employee
        self.assertEqual(self.employee_3.pay, 2200.00)

    def test_set_work_time_hours_valid_inputs(self):
        """Test correct valid inputs are set correctly"""
        # valid boundary values
        self.employee_1.set_work_time_hours(0)
        self.assertEqual(self.employee_1._total_work_hours, 0)
        self.employee_1.set_work_time_hours(1)
        self.assertEqual(self.employee_1._total_work_hours, 1)
        self.employee_1.set_work_time_hours(20)
        self.assertEqual(self.employee_1._total_work_hours, 20)
        self.employee_1.set_work_time_hours(39)
        self.assertEqual(self.employee_1._total_work_hours, 39)
        self.employee_1.set_work_time_hours(40)
        self.assertEqual(self.employee_1._total_work_hours, 40)

    def test_set_work_time_hours_invalid_inputs(self):
        """Test if invalid inputs raise appropriate exceptions"""
        # invalid boundary values
        with self.assertRaises(TypeError):
            self.employee_1.set_work_time_hours("abc")

        with self.assertRaises(domain_validators.EmployeeWorkTimeOutOfRange):
            self.employee_1.set_work_time_hours(-1)
        with self.assertRaises(domain_validators.EmployeeWorkTimeOutOfRange):
            self.employee_1.set_work_time_hours(41)

    def test_is_a_leader(self):
        """Test that is a leader give correct values"""
        self.assertFalse(self.employee_1.is_a_leader)
        self.assertFalse(self.employee_2.is_a_leader)
        self.assertTrue(self.employee_3.is_a_leader)

    def test_set_is_a_leader(self):
        """Test that is_a_leader is set correctly"""
        self.employee_1.is_a_leader = True
        self.assertTrue(self.employee_1.is_a_leader)
        self.employee_1.is_a_leader = False
        self.assertFalse(self.employee_1.is_a_leader)

    def test_is_part_time(self):
        """Test if is_part_time give correct values"""
        self.assertFalse(self.employee_1.is_part_time())
        self.assertTrue(self.employee_2.is_part_time())
        self.assertFalse(self.employee_3.is_part_time())


if __name__ == '__main__':
    unittest.main()
