from rest_framework.test import APITestCase
from rest_framework import status


class TestTeamEmployeesUseCase(APITestCase):
    """Test cases for manage team"""
    def setUp(self):
        self.team_1 = {
            "name": "Grays",
            "description": "Grey-skinned humanoids, usually 3–4 feet tall, hairless."
        }
        self.team_2 = {
            "name": "Reptilians",
            "description": "Tall, scaly humanoids. Popularized by David Icke."
        }
        # add team
        self.client.post("/teams/", self.team_1)
        self.client.post("/teams/", self.team_2)

        self.employee_1 = {
            "name": "Brol",
            "employee_id": "00001",
            "hourly_rate": "100.00",
            "employee_type": 1,
            "team_id": 1
        }
        self.employee_2 = {
            "name": "Scox",
            "employee_id": "00002",
            "hourly_rate": "50.00",
            "employee_type": 1,
            "team_id": 1
        }
        # part time employee employee

        # add one employee
        self.client.post("/employees/", self.employee_1)
        self.client.post("/employees/", self.employee_2)

    def test_retrieve_team_employees(self):
        """Retrieve all teams employees in the repository"""
        # get all team employees
        response = self.client.get("/team-employees/")
        # assert two teams are returned
        # test if response list length is 1
        self.assertEqual(len(response.data),2)
        self.client.post("/team-employees/", {"employee_id": 1, "team_id": 2})
        # get all team employee
        response = self.client.get("/team-employees/")
        self.assertEqual(len(response.data), 3)

    def test_retrieve_team_employee(self):
        """Retrieve team employee of a given primary key"""
        response = self.client.get("/team-employees/1/")
        self.assertEqual(response.data["id"], 1)
        self.assertEqual(response.data["employee"]["name"], "Brol")

    def test_retrieve_not_available_team_employee(self):
        team_response = self.client.get("/team-employees/3/")
        self.assertEqual(team_response.status_code, status.HTTP_404_NOT_FOUND)

    def test_add_team_employee_employee(self):
        """test adding team employee to a team without a team employee"""
        response = self.client.post("/team-employees/", {"employee_id": 1, "team_id": 2})
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_add_team_employee_invalid_requests(self):
        # assign team employee with employee that doesnt exist
        response = self.client.post("/team-employees/", {"employee_id": 3, "team_id": 2})
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

        # assign team employee with  team that doesn't exist
        response = self.client.post("/team-employees/", {"employee_id": 2, "team_id": 4})
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

        # assign team employee to a team that already a member
        response = self.client.post("/team-employees/", {"employee_id": 1, "team_id": 1})
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_remove_team_employee(self):
        # first add employee to another team
        response = self.client.post("/team-employees/", {"employee_id": 1, "team_id": 2})
        # remove team employee
        response_1 = self.client.delete("/team-employees/1/")
        self.assertEqual(response_1.status_code, status.HTTP_204_NO_CONTENT)
        # try to get team with id 1 and assert response
        team_response = self.client.get("/team-employees/1/")
        self.assertEqual(team_response.status_code, status.HTTP_404_NOT_FOUND)

    def test_remove_team_employee_invalid(self):
        # remove team employee of an employee that is a member of one team only
        response = self.client.delete("/team-employees/1/")
        # try to get team with id 1 and assert response
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data, "Can not remove team employee when employee is a member of one team only")
        # remove team employee that doesnt exist
        response = self.client.delete("/team-employees/4/")
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data, "Team Employee doesnt exists")
