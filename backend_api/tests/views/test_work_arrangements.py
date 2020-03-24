from rest_framework.test import APITestCase
from rest_framework import status


class TestWorkArrangementUseCase(APITestCase):
    """Test cases for manage work arrangement view"""
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
            "employee_type": 2,
            "team_id": 1,
            "work_arrangement": 80
        }
        # part time employee employee

        # add one employee
        self.client.post("/employees/", self.employee_1)
        self.client.post("/employees/", self.employee_2)

    def test_retrieve_work_arrangements(self):
        """Retrieve all works arrangements in the repository"""
        # get all work arrangements
        response = self.client.get("/work-arrangements/")
        # assert two works are returned
        # test if response list length is 1
        self.assertEqual(len(response.data), 2)  # already added 2 employees work arrangements

    def test_retrieve_work_arrangement(self):
        """Retrieve work arrangement of a given primary key"""
        response = self.client.get("/work-arrangements/1/")
        self.assertEqual(response.data["id"], 1)
        self.assertEqual(response.data["employee"]["name"], "Brol")

    def test_retrieve_not_available_work_arrangement(self):
        work_response = self.client.get("/work-arrangements/3/")
        self.assertEqual(work_response.status_code, status.HTTP_404_NOT_FOUND)

    def test_add_work_arrangement_arrangement(self):
        """test adding work arrangement to part time employee"""
        work_arrangement = {
            "employee_id": 2,
            "team_id": 2,
            "percent": 15,
            "remarks": "Extra work for Scox"
        }
        response = self.client.post("/work-arrangements/", work_arrangement)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['employee']["pay"], '2090.00')  # assert employee pay is updated

    def test_add_work_arrangement_invalid_requests(self):
        # assign work arrangement with employee that doesnt exist
        work_arrangement = {
            "employee_id": 3,
            "team_id": 2,
            "percent": 15,
            "remarks": "Extra work for Scox"
        }
        response = self.client.post("/work-arrangements/", work_arrangement)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

        # assign work arrangement with  team that doesn't exist
        work_arrangement = {
            "employee_id": 2,
            "team_id": 3,
            "percent": 15,
            "remarks": "Extra work for Scox"
        }
        response = self.client.post("/work-arrangements/", work_arrangement)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

        # assign work arrangement to an employee in a team whose employee already have work arrangement already
        work_arrangement = {
            "employee_id": 2,
            "team_id": 1,
            "percent": 15,
            "remarks": "Extra work for Scox"
        }
        response = self.client.post("/work-arrangements/", work_arrangement)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_update_work_arrangement(self):
        """Check if work arrangement can be updated correctly """
        # add work arrangement
        work_arrangement = {
            "employee_id": 2,
            "team_id": 2,
            "percent": 15,
            "remarks": "Extra work for Scox"
        }
        response = self.client.post("/work-arrangements/", work_arrangement)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['percent'], 15)
        id = response.data["id"]
        # update work arrangement
        work_arrangement = {
            "id": id,
            "employee_id": 2,
            "team_id": 2,
            "percent": 20,
            "remarks": "Extra work for Scox"
        }
        response = self.client.put(F"/work-arrangements/{id}/", work_arrangement)  # update new added work arrangement
        print(response)
        self.assertEqual(response.data["percent"], 20)

    def test_update_work_arrangement_invalid_requests(self):
        # update work arrangement not in the database
        work_arrangement = {
            "id": 4,
            "employee_id": 2,
            "team_id": 2,
            "percent": 20,
            "remarks": "Extra work for Scox"
        }
        response = self.client.put(F"/work-arrangements/4/", work_arrangement)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data, "Work arrangement does not exist in repository")

    def test_remove_work_arrangement(self):
        # first add arrangement to another work
        work_arrangement = {
            "employee_id": 2,
            "team_id": 2,
            "percent": 15,
            "remarks": "Extra work for Scox"
        }
        response = self.client.post("/work-arrangements/", work_arrangement)
        # remove work arrangement
        id = response.data['id']
        print(id)
        response_1 = self.client.delete(F"/work-arrangements/{id}/")
        self.assertEqual(response_1.status_code, status.HTTP_204_NO_CONTENT)
        response = self.client.get(F"/work-arrangements/{id}/")
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_remove_work_arrangement_invalid(self):
        # remove work arrangement that doesnt exist
        response = self.client.delete("/work-arrangements/4/")
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data, "Work arrangement does not exist")
