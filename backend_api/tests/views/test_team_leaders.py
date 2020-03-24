from rest_framework.test import APITestCase
from rest_framework import status


class TestTeamLeadersUseCase(APITestCase):
    """Test cases for manage team leaders"""
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

        self.team_leader = {
            "employee_id": 1,
            "team_id": 1

        }
        self.client.post("/team-leaders/", self.team_leader)

    def test_retrieve_team_leaders(self):
        """Retrieve all teams leaders in the repository"""
        # get all team leaders
        response = self.client.get("/team-leaders/")
        # assert two teams are returned
        # test if response list length is 1
        self.assertEqual(len(response.data), 1)
        self.client.post("/team-leaders/", {"employee_id": 1, "team_id": 2})
        # get all team leaders
        response = self.client.get("/team-leaders/")
        self.assertEqual(len(response.data), 2)

    def test_retrieve_team_leader(self):
        """Retrieve team leader of a given primary key"""
        response = self.client.get("/team-leaders/1/")
        self.assertEqual(response.data["id"], 1)
        self.assertEqual(response.data["leader"]["name"], "Brol")

    def test_retrieve_not_available_team_leader(self):
        team_response = self.client.get("/team-leaders/3/")
        self.assertEqual(team_response.status_code, status.HTTP_404_NOT_FOUND)

    def test_assign_team_leader_employee(self):
        """test adding team leader to a team without a team leader"""
        response = self.client.post("/team-leaders/", {"employee_id": 1, "team_id": 2})
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_assign_team_leader_invalid_requests(self):
        # assign team leader with employee that doesnt exist
        response = self.client.post("/team-leaders/", {"employee_id": 3, "team_id": 2})
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

        # assign team leader with  team that doesn't exist
        response = self.client.post("/team-leaders/", {"employee_id": 2, "team_id": 4})
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

        # assign team leader to a team that already have a leader
        response = self.client.post("/team-leaders/", {"employee_id": 2, "team_id": 1})
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_change_team_leader(self):
        # change team 1 leader from employee 1 to employee two
        updated_team_leader = {
            "id": 1,
            "team_id": 1,
            "employee_id": 2
        }
        response = self.client.put("/team-leaders/1/", updated_team_leader)
        self.assertEqual(response.data["leader"]["id"], 2)

    def test_change_team_leader_in_valid_requests(self):
        # Change team leader with team leader that doesnt exist
        updated_team_leader = {
            "id": 3,
            "team_id": 1,
            "employee_id": 2
        }
        response = self.client.put("/team-leaders/1/", updated_team_leader)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

        # Change team leader with employee that doesnt exist
        updated_team_leader = {
            "id": 1,
            "team_id": 1,
            "employee_id": 4
        }
        response = self.client.put("/team-leaders/1/", updated_team_leader)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

        # Change team leader with  team that doesn't exist
        updated_team_leader = {
            "id": 1,
            "team_id": 3,
            "employee_id": 2
        }
        response = self.client.put("/team-leaders/1/", updated_team_leader)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
