from rest_framework.test import APITestCase
from rest_framework import status


class TestWorkTimeUseCase(APITestCase):
    """Test cases for manage work times view"""
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

    def test_retrieve_work_times(self):
        """Retrieve all works times in the repository"""
        # get all work times
        response = self.client.get("/work-times/")
        # assert two works are returned
        # test if response list length is 1
        self.assertEqual(len(response.data), 2)  # already added 2 employees work times

    def test_retrieve_work_time(self):
        """Retrieve work time of a given primary key"""
        response = self.client.get("/work-times/1/")
        self.assertEqual(response.data["id"], 1)
        self.assertEqual(response.data["hours"], 40)  # first employee is full time
        response = self.client.get("/work-times/2/")
        self.assertEqual(response.data["id"], 2)
        self.assertEqual(response.data["hours"], 32)  # second employee is part time (80% of 40)

    def test_retrieve_not_available_work_time(self):
        work_response = self.client.get("/work-times/3/")
        self.assertEqual(work_response.status_code, status.HTTP_404_NOT_FOUND)