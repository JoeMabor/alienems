
from rest_framework.test import APITestCase
from rest_framework import status


class TestManageTeamView(APITestCase):
    """Test cases for  manage team use case"""
    def setUp(self):
        self.team = {
            "name": "Grays",
            "description": "Grey-skinned humanoids, usually 3–4 feet tall, hairless."
        }

        self.client.post("/teams/", self.team)

    def test_create_team_valid_request(self):
        # team without a leader
        team_1 = {
            "name": "Reptilians",
            "description": "Tall, scaly humanoids. Popularized by David Icke."
        }

        team_response_1 = self.client.post("/teams/", team_1)

        self.assertEqual(team_response_1.status_code, status.HTTP_201_CREATED)
        # adding team with a leader
        employee_data = {
            "name": "Brol",
            "employee_id": "00002",
            "hourly_rate": "100.00",
            "employee_type": 1,
            "team_id": team_response_1.data['id']
            }

        employee_response = self.client.post("/employees/", employee_data)
        team_data_2 = {
            "name": "Flatwoods monster",
            "description": "Tall humanoid with a spade-shaped head",
            "leader_id": employee_response.data["id"]
        }

        response = self.client.post("/teams/", team_data_2)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_team_invalid_request(self):
        # null name
        data_1 = {
            "name": "",
            "description": "Grey-skinned humanoids, usually 3–4 feet tall, hairless."
                }
        response_1 = self.client.post("/teams/", data_1)
        self.assertEqual(response_1.status_code, status.HTTP_400_BAD_REQUEST)
        # add team with employee  not available
        data_2 = {
            "name": "",
            "description": "Grey-skinned humanoids, usually 3–4 feet tall, hairless.",
            "leader_id": 1
        }
        response_1 = self.client.post("/teams/", data_2)
        self.assertEqual(response_1.status_code, status.HTTP_400_BAD_REQUEST)

    def test_team_list(self):
        # get all teams
        teams_response = self.client.get("/teams/")
        # assert two teams are returned
        self.assertEqual(len(teams_response.data), 1)

    def test_team_detail(self):
        # get team 1 details
        team_response = self.client.get("/teams/1/")
        self.assertEqual(team_response.data["id"], 1)
        self.assertEqual(team_response.data["name"], "Grays")

    def test_not_available_team_details(self):
        """Get a team that doesn't exist in database"""
        team_response = self.client.get("/teams/3/")
        self.assertEqual(team_response.status_code, status.HTTP_404_NOT_FOUND)

    def test_update_team(self):

        updated_team = {
            "id": 1,
            "name": "Grays",
            "description": "Description updated"
        }
        team_response = self.client.put("/teams/1/", updated_team)
        self.assertEqual(team_response.data["description"], "Description updated")

    def test_delete_team(self):
        # delete added team in set up
        response_1 = self.client.delete("/teams/1/")
        self.assertEqual(response_1.status_code, status.HTTP_204_NO_CONTENT)
        # try to get team with id 1 and assert response
        team_response = self.client.get("/teams/1/")
        self.assertEqual(team_response.status_code, status.HTTP_404_NOT_FOUND)







