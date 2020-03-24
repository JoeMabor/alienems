
from rest_framework.test import APITestCase
from rest_framework import status


class TestManageEmployeeView(APITestCase):
    """Test cases for manage employee use case view"""
    def setUp(self):
        """When be run on every test case"""
        self.team = {
            "name": "Grays",
            "description": "Grey-skinned humanoids, usually 3–4 feet tall, hairless."
        }
        # add team
        self.client.post("/teams/", self.team)
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
        self.employee_3 = {
            "name": "Thomels",
            "employee_id": "00003",
            "hourly_rate": "50.00",
            "employee_type": 2,
            "team_id": 1,
            "work_arrangement": 85
        }
        # add one employee
        self.client.post("/employees/", self.employee_1)

    def test_create_employee_valid_request(self):
        # add full time employee employee
        response_1 = self.client.post("/employees/", self.employee_2)
        self.assertEqual(response_1.status_code, status.HTTP_201_CREATED)
        # adding part time employee
        response_2 = self.client.post("/employees/", self.employee_3)
        self.assertEqual(response_2.status_code, status.HTTP_201_CREATED)

    def test_create_employee_invalid_request(self):
        # add employee with existing employee ID
        response = self.client.post("/employees/", self.employee_1)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data, "New  employee ID  already exist")
        # add part time employee with null work arrangement
        employee = {
            "name": "Thomels",
            "employee_id": "00003",
            "hourly_rate": "50.00",
            "employee_type": 2,
            "team_id": 1,
            "work_arrangement": ""
        }
        response = self.client.post("/employees/", employee)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        # add employee with work arrangement percent more than 100
        employee = {
            "name": "Thomels",
            "employee_id": "00003",
            "hourly_rate": "50.00",
            "employee_type": 2,
            "team_id": 1,
            "work_arrangement": "110"
        }
        response = self.client.post("/employees/", employee)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data, "Employee work arrangement percentage must be more than 0 and less than 100")

    def test_employee_list(self):
        """Get list of employees"""
        # get all teams
        response = self.client.get("/employees/")
        # assert two teams are returned
        self.assertEqual(len(response.data), 1)
        # add more employee
        self.client.post("/employees/", self.employee_2)
        response = self.client.get("/employees/")
        self.assertEqual(len(response.data), 2)

    def test_employee_detail(self):
        # get team 1 details
        response = self.client.get("/employees/1/")
        self.assertEqual(response.data["id"], 1)
        self.assertEqual(response.data["name"], "Brol")

    def test_not_available_employee_details(self):
        """Get a employee that doesn't exist in database"""
        response = self.client.get("/employees/3/")
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_update_employee_valid_request(self):
        update_employee = {
            "id": 1,
            "name": "Brol Grol",
            "employee_id": "00001",
            "hourly_rate": "100.00",
            "employee_type": 1,
            "team_id": 1
        }
        team_response = self.client.put("/employees/1/", update_employee)
        self.assertEqual(team_response.data["name"], "Brol Grol")

    def test_update_employee_in_valid_requests(self):
        # update employee that is not available in the database
        update_employee = {
            "id": 3,
            "name": "Brol Grol",
            "employee_id": "00001",
            "hourly_rate": "100.00",
            "employee_type": 1,
            "team_id": 1
        }
        team_response = self.client.put("/employees/1/", update_employee)
        self.assertEqual(team_response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_delete_employee(self):
        # delete added team in set up
        response_1 = self.client.delete("/employees/1/")
        self.assertEqual(response_1.status_code, status.HTTP_204_NO_CONTENT)
        # try to get team with id 1 and assert response
        team_response = self.client.get("/employees/1/")
        self.assertEqual(team_response.status_code, status.HTTP_404_NOT_FOUND)







