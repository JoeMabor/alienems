import unittest
from domain.entities.employee import EmployeeEntity
from domain.entities.team import TeamEntity
from domain.entities.team_leader import TeamLeaderEntity
from domain.entities.work_arrangment import WorkArrangementEntity
from domain.entities.work_time import WorkTimeEntity
from domain.entities.team_employee import TeamEmployeeEntity
import domain.entities.validators as domain_validators
import datetime


class TestTeamEntity(unittest.TestCase):
    """tests cases for TeamEntity"""
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
        """tests id gives correct values"""
        self.assertIsNone(self.team_1.id)
        self.assertEqual(self.team_2.id, 1)

    def test_name(self):
        """tests name given correct values"""
        self.assertEqual(self.team_1.name, "Greys")
        self.assertEqual(self.team_2.name, "Flatwoods monster")

    def test_name_setter(self):
        """tests name setter setts correct values"""
        self.team_1.name = "Reptilians"
        self.assertEqual(self.team_1.name, "Reptilians")
        self.team_2.name = "Nordic"
        self.assertEqual(self.team_2.name, "Nordic")

    def test_description(self):
        """tests that description gives correct values"""
        self.assertEqual(self.team_1.description,
                         "Grey-skinned humanoids, usually 3–4 feet tall, hairless, with large heads.")
        self.assertEqual(self.team_2.description, "Tall humanoid with a spade-shaped head.")

    def test_description_setter(self):
        """tests that description setter setter correct values"""
        self.team_1.description = "Tall, scaly humanoids."
        self.assertEqual(self.team_1.description, "Tall, scaly humanoids.")
        self.team_2.description = "Humanoids with stereotypical Nordic features."
        self.assertEqual(self.team_2.description,  "Humanoids with stereotypical Nordic features.")

    def test_leader(self):
        """tests that leader gives correct values and is of correct class"""
        self.assertIsNone(self.team_1.leader)
        self.assertIsInstance(self.team_2.leader, EmployeeEntity)
        self.assertEqual(self.team_2.leader, self.leader)

    def test_set_leader(self):
        """tests that leader gives correct values and is of correct class"""
        self.team_1.leader = self.leader
        self.assertIsInstance(self.team_1.leader, EmployeeEntity)
        self.assertEqual(self.team_1.leader, self.leader)

    def test_has_a_leader(self):
        """tests if team has a leader give correct boolean values"""
        self.assertFalse(self.team_1.has_a_leader)
        self.assertTrue(self.team_2.has_a_leader)

    def test_created_at(self):
        """tests if created_at give correct values"""
        self.assertIsNone(self.team_1.created_at)
        self.assertEqual(self.team_2.created_at, self.created_at)

    def test_updated_at(self):
        """tests if updated give correct values"""
        self.assertIsNone(self.team_1.updated_at)
        self.assertEqual(self.team_2.updated_at, self.updated_at)

    def test_updated_at_setter(self):
        """tests if updated_at setter set values correct"""
        new_updated_at_1 = datetime.datetime.now() + datetime.timedelta(days=1)
        new_updated_at_2 = datetime.datetime.now() + datetime.timedelta(days=2)
        self.team_1.updated_at = new_updated_at_1
        self.assertEqual(self.team_1.updated_at, new_updated_at_1)
        self.team_1.updated_at = new_updated_at_2
        self.assertEqual(self.team_1.updated_at, new_updated_at_2)


class TestEmployeeEntity(unittest.TestCase):
    """tests cases for EmployeeEntity"""

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
        """tests id gives correct values"""
        self.assertIsNone(self.employee_1.id)
        self.assertEqual(self.employee_2.id, 1)

    def test_name(self):
        """tests if name gives correct values"""
        self.assertEqual(self.employee_1.name, "Scurrod")
        self.assertEqual(self.employee_2.name, "Brol")

    def test_name_setter(self):
        """tests name setter setts correct values"""
        self.employee_1.name = "Draikrox"
        self.assertEqual(self.employee_1.name, "Draikrox")
        self.employee_2.name = "Strorkreins"
        self.assertEqual(self.employee_2.name, "Strorkreins")

    def test_employee_id(self):
        """tests if employee id give correct values"""
        self.assertEqual(self.employee_1.employee_id, "00001")
        self.assertEqual(self.employee_2.employee_id, "00002")

    def test_employee_id_setter(self):
        """tests if employee id give correct values"""
        self.employee_1.employee_id = "00003"
        self.assertEqual(self.employee_1.employee_id, "00003")
        self.employee_2.employee_id = "00004"
        self.assertEqual(self.employee_2.employee_id, "00004")

    def test_employee_id_setter_invalid_inputs(self):
        """tests correct exceptions is raised when invalid inputs are  passed"""
        with self.assertRaises(domain_validators.EmployeeIDLengthNot5):
            self.employee_2.employee_id = "0004"  # length less than 5
        with self.assertRaises(domain_validators.EmployeeIDLengthNot5):
            self.employee_2.employee_id = "000040"  # length more than 5

    def test_hourly_rate(self):
        """tests if hourly rate gives correct values"""
        self.assertEqual(self.employee_1.hourly_rate, 100.00)
        self.assertEqual(self.employee_2.hourly_rate, 50.00)

    def test_hourly_rate_setter(self):
        """tests if hourly rate setter setts correct values"""
        self.employee_1.hourly_rate = 45.00
        self.assertEqual(self.employee_1.hourly_rate, 45.00)
        self.employee_2.hourly_rate = 60.50
        self.assertEqual(self.employee_2.hourly_rate, 60.50)

    def test_hourly_rate_setter_invalid_inputs(self):
        """tests if hourly rate setter raise appropriate exceptions"""
        with self.assertRaises(ValueError):
            self.employee_1.hourly_rate = "abc"

        with self.assertRaises(ValueError):
            self.employee_1.hourly_rate = -1

    def test_employee_type(self):
        """tests if employee type gives correct values"""
        self.assertEqual(self.employee_1.employee_type, 1)
        self.assertEqual(self.employee_2.employee_type, 2)

    def test_employee_type_setter(self):
        """tests if employee type setter setter correct values"""
        self.employee_1.employee_type = 1
        self.assertEqual(self.employee_1.employee_type, 1)
        self.employee_1.employee_type = 2
        self.assertEqual(self.employee_1.employee_type, 2)

    def test_employee_type_setter_invalid_inputs(self):
        """tests if employee type setter setter correct values"""
        # employee can only be full time (1) or Part time (2)
        with self.assertRaises(ValueError):
            self.employee_1.employee_type = "abc"

        with self.assertRaises(ValueError):
            self.employee_1.employee_type = 0

        with self.assertRaises(ValueError):
            self.employee_1.employee_type = 3

    def test_created_at(self):
        """tests if created_at give correct values"""
        self.assertIsNone(self.employee_1.created_at)
        self.assertEqual(self.employee_2.created_at, self.created_at)

    def test_updated_at(self):
        """tests if updated give correct values"""
        self.assertIsNone(self.employee_1.updated_at)
        self.assertEqual(self.employee_2.updated_at, self.updated_at)

    def test_updated_at_setter(self):
        """tests if updated_at setter set values correect"""
        new_updated_at_1 = datetime.datetime.now() + datetime.timedelta(days=1)
        new_updated_at_2 = datetime.datetime.now() + datetime.timedelta(days=2)
        self.employee_1.updated_at = new_updated_at_1
        self.employee_2.updated_at = new_updated_at_2
        self.assertEqual(self.employee_1.updated_at, new_updated_at_1)
        self.assertEqual(self.employee_2.updated_at, new_updated_at_2)

    def test_add_leadership_bonus_valid_inputs(self):
        """tests that add_leadership bonus calculate correct bonus. bonus = pay * 0.1"""
        self.assertEqual(self.employee_1.add_leadership_bonus(0), 0)
        self.assertEqual(self.employee_1.add_leadership_bonus(1), 0)
        self.assertEqual(self.employee_1.add_leadership_bonus(400), 40.00)

    def test_add_leadership_bonus_invalid_inputs(self):
        """tests that invalid inputs produced correct Exception"""
        with self.assertRaises(TypeError):
            self.employee_1.add_leadership_bonus("abc")

        with self.assertRaises(ValueError):
            self.employee_1.add_leadership_bonus(-1)

    def test_calculate_pay(self):
        """tests pay is calculated correctly"""
        # part time employee and not a leader
        self.assertEqual(self.employee_2.calculate_pay(), 4000.00)
        # a leader and full time employee
        self.assertEqual(self.employee_3.calculate_pay(), 8800.00)

    def test_pay(self):
        """tests if pay gives correct calculated pay as values total hours"""
        # total work hours not given
        self.assertIsNone(self.employee_1.pay)
        # part time employee and not a leader
        self.assertEqual(self.employee_2.pay, 4000.00)
        # a leader and full time employee
        self.assertEqual(self.employee_3.pay, 8800.00)

    def test_set_work_time_hours_valid_inputs(self):
        """tests correct valid inputs are set correctly"""
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
        """tests if invalid inputs raise appropriate exceptions"""
        # invalid boundary values
        with self.assertRaises(TypeError):
            self.employee_1.set_work_time_hours("abc")

        with self.assertRaises(domain_validators.EmployeeWorkTimeOutOfRange):
            self.employee_1.set_work_time_hours(-1)
        with self.assertRaises(domain_validators.EmployeeWorkTimeOutOfRange):
            self.employee_1.set_work_time_hours(41)

    def test_is_a_leader(self):
        """tests that is a leader give correct values"""
        self.assertFalse(self.employee_1.is_a_leader)
        self.assertFalse(self.employee_2.is_a_leader)
        self.assertTrue(self.employee_3.is_a_leader)

    def test_set_is_a_leader(self):
        """tests that is_a_leader is set correctly"""
        self.employee_1.is_a_leader = True
        self.assertTrue(self.employee_1.is_a_leader)
        self.employee_1.is_a_leader = False
        self.assertFalse(self.employee_1.is_a_leader)

    def test_is_part_time(self):
        """tests if is_part_time give correct values"""
        self.assertFalse(self.employee_1.is_part_time())
        self.assertTrue(self.employee_2.is_part_time())
        self.assertFalse(self.employee_3.is_part_time())


class TestTeamEmployee(unittest.TestCase):
    """tests cases for TeamEmployeeEntity"""
    def setUp(self):
        self.created_at = datetime.datetime.now()
        self.updated_at = datetime.datetime.now()
        self.employee = EmployeeEntity(
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
        self.team = TeamEntity(
            id=1,
            name="Flatwoods monster",
            description="Tall humanoid with a spade-shaped head.",
            created_at=self.created_at,
            updated_at=self.updated_at
        )
        self.team_employee = TeamEmployeeEntity(
            id=1,
            employee=self.employee,
            team=self.team,
            created_at=self.created_at,
            updated_at=self.updated_at
        )

    def test_id(self):
        """tests that id give correct values"""
        self.assertEqual(self.team_employee.id, 1)

    def test_employee(self):
        """tests that employee give correct value and instance"""
        self.assertIsInstance(self.team_employee.employee, EmployeeEntity)
        self.assertEqual(self.team_employee.employee, self.employee)

    def test_team(self):
        """tests that employee give correct value and instance"""
        self.assertEqual(self.team_employee.team, self.team)

    def test_created_at(self):
        """tests if created_at give correct values"""
        self.assertEqual(self.team_employee.created_at, self.created_at)

    def test_updated_at(self):
        """tests if updated give correct values"""
        self.assertEqual(self.team_employee.updated_at, self.updated_at)


class TestTeamLeader(unittest.TestCase):
    """tests cases for Team leader"""
    def setUp(self):
        self.created_at = datetime.datetime.now()
        self.updated_at = datetime.datetime.now()
        self.leader = EmployeeEntity(
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
        self.team = TeamEntity(
            id=1,
            name="Flatwoods monster",
            description="Tall humanoid with a spade-shaped head.",
            created_at=self.created_at,
            updated_at=self.updated_at
        )
        self.team_leader = TeamLeaderEntity(
            id=1,
            leader=self.leader,
            team=self.team,
            created_at=self.created_at,
            updated_at=self.updated_at
        )

    def test_id(self):
        """tests that id give correct values"""
        self.assertEqual(self.team_leader.id, 1)

    def test_employee(self):
        """tests that employee give correct value and instance"""
        self.assertIsInstance(self.team_leader.leader, EmployeeEntity)
        self.assertEqual(self.team_leader.leader, self.leader)

    def test_team(self):
        """tests that employee give correct value and instance"""
        self.assertIsInstance(self.team_leader.team, TeamEntity)
        self.assertEqual(self.team_leader.team, self.team)

    def test_created_at(self):
        """tests if created_at give correct values"""
        self.assertEqual(self.team_leader.created_at, self.created_at)

    def test_updated_at(self):
        """tests if updated give correct values"""
        self.assertEqual(self.team_leader.updated_at, self.updated_at)


class TestWorkArrangement(unittest.TestCase):
    """tests cases for work arrangements"""
    def setUp(self):
        self.created_at = datetime.datetime.now()
        self.updated_at = datetime.datetime.now()
        self.employee = EmployeeEntity(
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
        self.team = TeamEntity(
            id=1,
            name="Flatwoods monster",
            description="Tall humanoid with a spade-shaped head.",
            created_at=self.created_at,
            updated_at=self.updated_at
        )

        self.work_arrangement = WorkArrangementEntity(
            id=1,
            percent=80,
            employee=self.employee,
            team=self.team,
            remarks="Blah bla ..."
        )

    def test_id(self):
        """tests that id give correct values"""
        self.assertEqual(self.work_arrangement.id, 1)

    def test_percent(self):
        """tests that percent give correct values"""
        self.assertEqual(self.work_arrangement.percent, 80)

    def test_validate_percentage(self):
        """tests that validation raise correct Exception"""
        # boundary valid values
        self.assertEqual(self.work_arrangement.validate_percentage(0), 0)
        self.assertEqual(self.work_arrangement.validate_percentage(1), 1)
        self.assertEqual(self.work_arrangement.validate_percentage(50), 50)
        self.assertEqual(self.work_arrangement.validate_percentage(99), 99)
        self.assertEqual(self.work_arrangement.validate_percentage(100), 100)
        # boundary invalid inputs
        with self.assertRaises(domain_validators.WorkArrangementPercentageOutOfRange):
            self.work_arrangement.validate_percentage(-1)

        with self.assertRaises(domain_validators.WorkArrangementPercentageOutOfRange):
            self.work_arrangement.validate_percentage(101)
        # wrong type
        with self.assertRaises(TypeError):
            self.work_arrangement.validate_percentage("abc")

    def test_percent_setter(self):
        """tests that percent setter can setter correct values anc validates inputs"""
        self.work_arrangement.percent = 50
        self.assertEqual(self.work_arrangement.percent, 50)

        with self.assertRaises(domain_validators.WorkArrangementPercentageOutOfRange):
            self.work_arrangement.percent = -1

        with self.assertRaises(domain_validators.WorkArrangementPercentageOutOfRange):
            self.work_arrangement.percent = 101

        with self.assertRaises(TypeError):
            self.work_arrangement.percent = "abc"

    def test_employee(self):
        """tests that employee give correct value"""
        self.assertIsInstance(self.work_arrangement.employee, EmployeeEntity)
        self.assertEqual(self.work_arrangement.employee, self.employee)

    def test_employee_setter(self):
        """tests that employee setter set correct employee"""
        employee = EmployeeEntity(
            id=1,
            name="Scox",
            employee_id="00003",
            hourly_rate=50.00,
            employee_type=2,
            is_a_leader=False,
            created_at=self.created_at,
            updated_at=self.updated_at,
            total_work_hours=20
        )
        self.work_arrangement.employee = employee
        self.assertIsInstance(self.work_arrangement.employee, EmployeeEntity)
        self.assertEqual(self.work_arrangement.employee, employee)

    def test_team(self):
        """tests that team give correct value"""
        self.assertIsInstance(self.work_arrangement.team, TeamEntity)
        self.assertEqual(self.work_arrangement.team, self.team)

    def test_remarks(self):
        """Tests that remarks give correct values"""
        self.assertEqual(self.work_arrangement.remarks, "Blah bla ...")

    def test_calculate_work_time_hours(self):
        """Tests that calculate_work_time_hours work correctly"""
        # hours = percent/100 * 40 (hours)
        # boundary values valid
        self.assertEqual(self.work_arrangement.calculate_work_time_hours(0), 0)
        self.assertEqual(self.work_arrangement.calculate_work_time_hours(1), 0)  # round off
        self.assertEqual(self.work_arrangement.calculate_work_time_hours(50), 20)  # round off
        self.assertEqual(self.work_arrangement.calculate_work_time_hours(99), 39)  # round off
        self.assertEqual(self.work_arrangement.calculate_work_time_hours(100), 40)

    def test_calculate_work_time_hours_invalid_inputs(self):
        """Tests that calculate_work_time_hours work correctly"""
        # hours = percent/100 * 40 (hours)
        # boundary values valid
        with self.assertRaises(domain_validators.WorkArrangementPercentageOutOfRange):
            self.work_arrangement.calculate_work_time_hours(-1)

        with self.assertRaises(domain_validators.WorkArrangementPercentageOutOfRange):
            self.work_arrangement.calculate_work_time_hours(101)

        with self.assertRaises(TypeError):
            self.work_arrangement.calculate_work_time_hours("abc")

    def test_str__(self):
        """Test if str rep is correct"""
        self.assertEqual(str(self.work_arrangement), "80")


class TestWorkTime(unittest.TestCase):
    """Test cases for WorkTimeEntity"""
    def setUp(self):
        self.created_at = datetime.datetime.now()
        self.updated_at = datetime.datetime.now()
        self.employee = EmployeeEntity(
            id=1,
            name="Brol",
            employee_id="00002",
            hourly_rate=50.00,
            employee_type=2,
            is_a_leader=False,
            created_at=self.created_at,
            updated_at=self.updated_at,
            total_work_hours=32
        )
        self.team = TeamEntity(
            id=1,
            name="Flatwoods monster",
            description="Tall humanoid with a spade-shaped head.",
            created_at=self.created_at,
            updated_at=self.updated_at
        )

        self.work_arrangement = WorkArrangementEntity(
            id=1,
            percent=80,
            employee=self.employee,
            team=self.team,
            remarks="Blah bla ..."
        )

        self.work_time = WorkTimeEntity(
            id=1,
            hours=32,
            employee=self.employee,
            work_arrangement=self.work_arrangement
        )

    def test_id(self):
        """Tests that id give correct values"""
        self.assertEqual(self.work_time.id, 1)

    def test_hours(self):
        """Tests that hours give correct values"""
        self.assertEqual(self.work_time.hours, 32)

    def test_validates_hours(self):
        """Tests that validator validates well"""
        # valid boundary inputs
        self.assertEqual(self.work_time.validates_hours(0), 0)
        self.assertEqual(self.work_time.validates_hours(1), 1)
        self.assertEqual(self.work_time.validates_hours(20), 20)
        self.assertEqual(self.work_time.validates_hours(39), 39)
        self.assertEqual(self.work_time.validates_hours(40), 40)
        # Invalid boundary inputs
        with self.assertRaises(domain_validators.EmployeeWorkTimeOutOfRange):
            self.work_time.validates_hours(-1)

        with self.assertRaises(domain_validators.EmployeeWorkTimeOutOfRange):
            self.work_time.validates_hours(41)

        with self.assertRaises(TypeError):
            self.work_time.validates_hours("abc")

    def test_hours_setter(self):
        """Tests that hours setter setts correct values """
        self.work_time.hours = 40
        self.assertEqual(self.work_time.hours, 40)

    def test_employee(self):
        """tests that employee give correct value"""
        self.assertIsInstance(self.work_time.employee, EmployeeEntity)
        self.assertEqual(self.work_time.employee, self.employee)

    def test_employee_setter(self):
        """Tests that employee setter sets correct values"""
        employee = EmployeeEntity(
            id=1,
            name="Scox",
            employee_id="00003",
            hourly_rate=50.00,
            employee_type=2,
            is_a_leader=False,
            created_at=self.created_at,
            updated_at=self.updated_at,
            total_work_hours=20
        )
        self.work_time.employee = employee
        self.assertIsInstance(self.work_time.employee, EmployeeEntity)
        self.assertEqual(self.work_time.employee, employee)

    def test_work_arrangement(self):
        """Tests that work_arrangement gives correct values"""
        self.assertIsInstance(self.work_time.work_arrangement, WorkArrangementEntity)
        self.assertEqual(self.work_time.work_arrangement, self.work_arrangement)


if __name__ == '__main__':
    unittest.main()
