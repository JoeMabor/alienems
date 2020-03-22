"""
Test suite for request data models
"""
import unittest
import domain.usecases.data_models.request_data_models as request_data_models
import decimal


class TestCreateEmployeeRequestData(unittest.TestCase):
    """Test cases for CreateEmployeeRequestData"""

    def setUp(self):
        self.request_data = request_data_models.CreateEmployeeRequestData(
            name="Scurrod",
            employee_id="00001",
            employee_type=1,
            hourly_rate=100.00,
            team_id=1,
            work_arrangement=50
        )

    def test_name(self):
        """Tests if name gives correct values"""
        self.assertEqual(self.request_data.name, "Scurrod")

    def test_employee_id(self):
        """Tests if employee_id  gives correct values employee ID"""
        self.assertEqual(self.request_data.employee_id, "00001")

    def test_employee_type(self):
        """Tests if employee_type give correct value"""
        self.assertEqual(self.request_data.employee_type, 1)

    def test_hourly_rate(self):
        """Test if hourly_rate give correct  decimal values"""
        self.assertEqual(self.request_data.hourly_rate, decimal.Decimal(100.00))

    def test_team_id(self):
        """Tests if team_id give correct values"""
        self.assertEqual(self.request_data.team_id,1)

    def test_work_arrangement(self):
        """Test if work arrangement gives correct work arrangement percentage"""
        self.assertEqual(self.request_data.work_arrangement, 50)


class TestUpdateEmployeeRequestData(unittest.TestCase):
    """Test cases for UpdateEmployeeRequestData"""

    def setUp(self):
        self.request_data = request_data_models.UpdateEmployeeRequestData(
            id=1,
            name="Scurrod",
            employee_id="00001",
            hourly_rate=100.00,
        )

    def test_id(self):
        """Tests if id gives correct values"""
        self.assertEqual(self.request_data.id, 1)

    def test_name(self):
        """Tests if name gives correct values"""
        self.assertEqual(self.request_data.name, "Scurrod")

    def test_employee_id(self):
        """Tests if employee_id  gives correct values"""
        self.assertEqual(self.request_data.employee_id, "00001")

    def test_hourly_rate(self):
        """Test if hourly_rate give correct  decimal values"""
        self.assertEqual(self.request_data.hourly_rate, decimal.Decimal(100.00))


class TestCreateTeamRequestData(unittest.TestCase):
    """Test cases for CreateTeamRequestData"""
    def setUp(self):
        self.request_data_1 = request_data_models.CreateTeamRequestData(name="Grays")
        self.request_data_2 = request_data_models.CreateTeamRequestData(
            name="Flatwoods monster",
            description="Tall humanoid with a spade-shaped head.",
            leader_id=1

        )

    def test_name(self):
        """Test name give correct values"""
        self.assertEqual(self.request_data_1.name, "Grays")
        self.assertEqual(self.request_data_2.name, "Flatwoods monster")

    def test_description(self):
        """Test that description give correct values"""
        self.assertIsNone(self.request_data_1.description)
        self.assertEqual(self.request_data_2.description, "Tall humanoid with a spade-shaped head.")

    def test_leader_id(self):
        """Test if leader_id give correct values"""
        self.assertIsNone(self.request_data_1.leader_id)
        self.assertEqual(self.request_data_2.leader_id, 1)


class TestUpdateTeamRequestData(unittest.TestCase):
    """Test cases for CreateTeamRequestData"""
    def setUp(self):
        self.request_data_1 = request_data_models.UpdateTeamRequestData(id=1, name="Grays")
        self.request_data_2 = request_data_models.UpdateTeamRequestData(
            id=2,
            name="Flatwoods monster",
            description="Tall humanoid with a spade-shaped head.",
        )

    def test_id(self):
        """Tests if id gives correct values"""
        self.assertEqual(self.request_data_1.id, 1)
        self.assertEqual(self.request_data_2.id, 2)

    def test_name(self):
        """Test name give correct values"""
        self.assertEqual(self.request_data_1.name, "Grays")
        self.assertEqual(self.request_data_2.name, "Flatwoods monster")

    def test_description(self):
        """Test that description give correct values"""
        self.assertIsNone(self.request_data_1.description)
        self.assertEqual(self.request_data_2.description, "Tall humanoid with a spade-shaped head.")


class TestCreateWorkArrangementData(unittest.TestCase):
    """Test cases for CreateWorkArrangementData"""
    def setUp(self):
        self.request_data = request_data_models.CreateWorkArrangementData(
            percent=50,
            remarks="50% of 40 hours",
            employee_id=1,
            team_id=1
        )

    def test_remarks(self):
        """Tests if remarks gives correct values"""
        self.assertEqual(self.request_data.remarks, "50% of 40 hours")

    def test_employee_id(self):
        """Tests if employee_id  gives correct values for employee id(primary key)"""
        self.assertEqual(self.request_data.employee_id, 1)

    def test_team_id(self):
        """Tests if team_id give correct values"""
        self.assertEqual(self.request_data.team_id, 1)

    def test_percent(self):
        """Test if work percent gives correct work arrangement percentage"""
        self.assertEqual(self.request_data.percent, 50)


class TestUpdateWorkArrangementData(unittest.TestCase):
    """Test cases for UpdateWorkArrangementData"""
    def setUp(self):
        self.request_data = request_data_models.UpdateWorkArrangementData(
            id=1,
            percent=50,
            remarks="50% of 40 hours",
            employee_id=1,
            team_id=1
        )

    def test_id(self):
        """Tests if id gives correct values"""
        self.assertEqual(self.request_data.id, 1)

    def test_remarks(self):
        """Tests if remarks gives correct values"""
        self.assertEqual(self.request_data.remarks, "50% of 40 hours")

    def test_employee_id(self):
        """Tests if employee_id  gives correct values for employee id(primary key)"""
        self.assertEqual(self.request_data.employee_id, 1)

    def test_team_id(self):
        """Tests if team_id give correct values"""
        self.assertEqual(self.request_data.team_id, 1)

    def test_percent(self):
        """Test if work percent gives correct work arrangement percentage"""
        self.assertEqual(self.request_data.percent, 50)


class TestCreateTeamLeaderOrEmployeeRequestData(unittest.TestCase):
    """Test cases for Create team leader/employee request data"""
    def setUp(self):
        self.request_data = request_data_models.CreateTeamLeaderOrEmployeeRequestData(
            team_id=1,
            employee_id=2
        )

    def test_team_id(self):
        """Tests if team_id give correct values"""
        self.assertEqual(self.request_data.team_id, 1)

    def test_employee_id(self):
        """Tests if employee_id  gives correct values for employee id(primary key)"""
        self.assertEqual(self.request_data.employee_id, 2)


class TestUpdateTeamLeaderOrEmployeeRequestData(unittest.TestCase):
    """Test cases for Create team leader/employee request data"""
    def setUp(self):
        self.request_data = request_data_models.UpdateTeamLeaderRequestData(
            id=1,
            team_id=1,
            employee_id=2
        )

    def test_id(self):
        """Tests if id gives correct values"""
        self.assertEqual(self.request_data.id, 1)

    def test_team_id(self):
        """Tests if team_id give correct values"""
        self.assertEqual(self.request_data.team_id, 1)

    def test_employee_id(self):
        """Tests if employee_id  gives correct values for employee id(primary key)"""
        self.assertEqual(self.request_data.employee_id, 2)


if __name__ == '__main__':
    unittest.main()
