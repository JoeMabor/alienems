"""
This module contains classes that receive API call requests for various uses and call respective services through
respective controllers of the use cases
"""

import domain.entities.validators as domain_exceptions
from django.core.exceptions import ObjectDoesNotExist
from rest_framework import viewsets
from django.views.generic import TemplateView
from django.http import Http404
from rest_framework.response import Response
from rest_framework import status
from .app_config import CONTROLLERS
import backend_api.serializers as data_serializers


class HomeView(TemplateView):
    """Home view that shows available main routes the API allow"""
    template_name = "index.html"


class ManageTeamView(viewsets.ViewSet):
    """Receive direct api calls and call respective ManageTeamController services"""
    # manage team controller
    controller = CONTROLLERS.manage_teams_controller()

    def get_team_object(self, team_pk=None):
        try:
            return self.controller.retrieve_team(team_pk=team_pk)
        except domain_exceptions.ObjectEntityDoesNotExist:
            raise Http404

    def list(self, request):
        """Retrieve list of all available team objects"""
        teams = self.controller.retrieve_all_teams()
        serializer = data_serializers.PresentTeamSerializer(teams, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        """Retrieve a given team object"""
        team = self.get_team_object(pk)
        serializer = data_serializers.PresentTeamSerializer(team)
        return Response(serializer.data)

    def create(self, request):
        """Create a new team object"""
        serializer = data_serializers.CreateTeamSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            request_data = serializer.save()
            try:
                new_team_entity = self.controller.create_team(request_data=request_data)
                serializer = data_serializers.PresentTeamSerializer(new_team_entity)
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            except domain_exceptions.TeamHasALeader as e:
                return Response(e.message, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk):
        """Update existing team object"""
        print("Update a team")
        serializer = data_serializers.UpdateTeamSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            request_data = serializer.save()
            new_team_entity = self.controller.update_team(request_data=request_data)

            serializer = data_serializers.PresentTeamSerializer(new_team_entity)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        """Delete a given team object"""
        try:
            deleted_team = self.controller.delete_team(pk)
            return Response(status=status.HTTP_204_NO_CONTENT)
        except ObjectDoesNotExist:
            return Response(ObjectDoesNotExist, status=status.HTTP_400_BAD_REQUEST)


class ManageEmployeesView(viewsets.ViewSet):
    """Receive direct api calls and call respective controller services"""
    # manage employee controller
    controller = CONTROLLERS.manage_employee_controller()

    def get_employee_object(self, pk):
        try:
            return self.controller.retrieve_employee(pk)
        except domain_exceptions.ObjectEntityDoesNotExist:
            raise Http404

    def list(self, request):
        """Retrieve list of all available employees in the repository"""
        employee = self.controller.retrieve_all_employees()
        serializer = data_serializers.PresentEmployeeDataSerializer(employee, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        """Retrieve an employee of the give primary key (pk)"""
        employee = self.get_employee_object(pk)
        print(F"Employee: {employee}")
        serializer = data_serializers.PresentEmployeeDataSerializer(employee)
        return Response(serializer.data)

    def create(self, request):
        """Create new employee object"""
        serializer = data_serializers.CreateEmployeeSerializer(data=request.data)

        if serializer.is_valid(raise_exception=True):
            request_data = serializer.save()
            print(F"Request employee Data: {serializer.data}")

            try:
                new_employee = self.controller.create_employee(request_data=request_data)
                serializer = data_serializers.PresentEmployeeDataSerializer(new_employee)
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            except (domain_exceptions.EmployeeIDIsNotUnique,
                    domain_exceptions.WorkArrangementPercentageOutOfRange,
                    domain_exceptions.TeamDoesNotExist,
                    domain_exceptions.TeamHasALeader,
                    domain_exceptions.WorkArrangementPercentageNull
                    ) as e:
                return Response(e.message, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk):
        """Update existing employee object"""
        serializer = data_serializers.UpdateEmployeeRequestSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            request_data = serializer.save()
            try:
                new_employee_entity = self.controller.update_employee(request_data=request_data)
                serializer = data_serializers.PresentEmployeeDataSerializer(new_employee_entity)
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            except (domain_exceptions.EmployeeIDIsNotUnique,
                    domain_exceptions.WorkArrangementPercentageOutOfRange,
                    domain_exceptions.TeamHasALeader,
                    domain_exceptions.ObjectEntityDoesNotExist
                    ) as e:
                return Response(e.message, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        """Delete a given employee object in the repository"""
        try:
            deleted_team = self.controller.delete_employee(pk)
            return Response(status=status.HTTP_204_NO_CONTENT)
        except domain_exceptions.ObjectEntityDoesNotExist as e:
            return Response(e.message, status=status.HTTP_404_NOT_FOUND)


class TeamLeaderView(viewsets.ViewSet):
    """Direct API calls for manageTeamLeader use case to respective controller services"""
    # manage team leader controller
    controller = CONTROLLERS.team_leaders_controller()

    def get_team_leader_object(self, pk):
        try:
            return self.controller.retrieve_team_leader(pk)
        except domain_exceptions.ObjectEntityDoesNotExist:
            raise Http404

    def list(self, request):
        """Retrieve list of all available team leaders"""
        team_leaders = self.controller.retrieve_all_teams_leaders()
        serializer = data_serializers.TeamLeaderPresenterSerializer(team_leaders, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        """Retrieve a given team leader"""
        team_leader = self.get_team_leader_object(pk)
        serializer = data_serializers.TeamLeaderPresenterSerializer(team_leader)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def create(self, request):
        """Adding a new leader to a team"""
        serializer = data_serializers.TeamLeaderOrEmployeeRequestDataSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            request_data = serializer.save()
            try:
                new_team_entity = self.controller.assign_team_leader(request_data=request_data)
                serializer = data_serializers.TeamLeaderPresenterSerializer(new_team_entity)
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            except (
                    domain_exceptions.TeamDoesNotExist,
                    domain_exceptions.TeamHasALeader,
                    domain_exceptions.EmployeeDoesNotExist
                    )as e:
                return Response(e.message, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk):
        """Change a leader of a team"""
        print("Update a team")
        serializer = data_serializers.UpdateTeamLeaderRequestDataSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            request_data = serializer.save()
            try:
                new_team_entity = self.controller.change_team_leader(request_data=request_data)
                serializer = data_serializers.TeamLeaderPresenterSerializer(new_team_entity)
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            except (
                    domain_exceptions.TeamDoesNotExist,
                    domain_exceptions.ObjectEntityDoesNotExist,
                    domain_exceptions.UpdateOfTeamLeaderOfWrongTeam,
                    domain_exceptions.EmployeeDoesNotExist
            )as e:
                return Response(e.message, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class TeamEmployeeView(viewsets.ViewSet):
    """Direct API calls for team employee use case to respective controller services"""
    # manage Team employee controller
    controller = CONTROLLERS.team_employees_controller()

    def get_team_employee_object(self, pk):
        try:
            return self.controller.retrieve_team_employee(pk)
        except ObjectDoesNotExist:
            raise Http404

    def list(self, request):
        """Retrieve list of all available team employee objects"""
        teams = self.controller.retrieve_all_teams_employees()
        serializer = data_serializers.PresentTeamEmployeeDataSerializer(teams, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        """Retrieve a given team employee"""
        try:
            team_employee = self.get_team_employee_object(pk)
            serializer = data_serializers.PresentTeamEmployeeDataSerializer(team_employee)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        except (
                domain_exceptions.TeamDoesNotExist
        )as e:
            return Response(e.message, status=status.HTTP_400_BAD_REQUEST)

    def create(self, request):
        """Add an employee to a team"""
        serializer = data_serializers.TeamLeaderOrEmployeeRequestDataSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            request_data = serializer.save()
            try:
                respond_data = self.controller.add_team_employee(request_data=request_data)
                serializer = data_serializers.PresentTeamEmployeeDataSerializer(respond_data)
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            except (
                    domain_exceptions.TeamDoesNotExist,
                    domain_exceptions.EmployeeDoesNotExist,
                    domain_exceptions.EmployeeIsATeamMember
                    )as e:
                return Response(e.message, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        """Remove an employee from a team"""
        try:
            deleted_team_employee = self.controller.remove_team_employee(pk)
            return Response(status=status.HTTP_204_NO_CONTENT)
        except (domain_exceptions.ObjectEntityDoesNotExist,
                domain_exceptions.EmployeeHasOneTeam
                ) as e:
            return Response(e.message, status=status.HTTP_400_BAD_REQUEST)


class WorkTimeView(viewsets.ViewSet):
    """Direct API calls for employee work times to respective controller services. Work time are are added
    automatically when a new employee or work arrangement is added and can only be viewed here
    """
    # manage work time controller
    controller = CONTROLLERS.work_time_controller()

    def get_team_employee_object(self, pk):
        try:
            return self.controller.retrieve_work_time(pk)
        except ObjectDoesNotExist:
            raise Http404

    def list(self, request):
        """Retrieve list of all available work times"""
        teams = self.controller.retrieve_all_work_times()
        serializer = data_serializers.PresentWorkTimeDataSerializer(teams, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        """Retrieve a given work time"""
        try:
            team_employee = self.get_team_employee_object(pk)
            serializer = data_serializers.PresentWorkTimeDataSerializer(team_employee)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        except (
                domain_exceptions.TeamDoesNotExist
        )as e:
            return Response(e.message, status=status.HTTP_400_BAD_REQUEST)


class WorkArrangementsView(viewsets.ViewSet):
    """Direct API calls for work arrangement use case to respective controller services. Mainly used for adding
    multiple work arrangements for part time employees.
    """
    # manage work arrangement controller
    controller = CONTROLLERS.work_arrangements_controller()

    def get_work_arrangement_object(self, pk):
        try:
            return self.controller.view_work_arrangement(pk)
        except domain_exceptions.ObjectEntityDoesNotExist:
            raise Http404

    def list(self, request):
        """Retrieve list of all available work arrangements"""
        teams = self.controller.view_all_work_arrangements()
        serializer = data_serializers.PresentWorkArrangementsDataSerializer(teams, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        """Retrieve a given work arrangement"""
        try:
            team_employee = self.get_work_arrangement_object(pk)
            serializer = data_serializers.PresentWorkArrangementsDataSerializer(team_employee)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        except (
                domain_exceptions.TeamDoesNotExist
        )as e:
            return Response(e.message, status=status.HTTP_400_BAD_REQUEST)

    def create(self, request):
        """Add new work arrangement for a part time employee"""
        serializer = data_serializers.CreateWorkArrangementSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            request_data = serializer.save()
            try:
                work_arrangement = self.controller.add_work_arrangement(request_data=request_data)
                serializer = data_serializers.PresentWorkArrangementsDataSerializer(work_arrangement)
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            except (
                    domain_exceptions.ObjectEntityDoesNotExist,
                    domain_exceptions.TeamDoesNotExist,
                    domain_exceptions.MultipleWorksForFullTimeEmployee,
                    domain_exceptions.MultipleWorkArrangementInOneTeam,
                    domain_exceptions.Max40HoursExceeded
                    )as e:
                return Response(e.message, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk):
        """Update existing work arrangement"""
        serializer = data_serializers.UpdateWorkArrangementSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            request_data = serializer.save()
            try:
                new_team_entity = self.controller.update_work_arrangement(request_data=request_data)
                serializer = data_serializers.PresentWorkArrangementsDataSerializer(new_team_entity)
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            except (
                    domain_exceptions.ObjectEntityDoesNotExist,
                    domain_exceptions.MultipleWorkArrangementInOneTeam,
                    domain_exceptions.EmployeeDoesNotExist,
                    domain_exceptions.Max40HoursExceeded
            )as e:
                return Response(e.message, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        """Delete work arrangement"""
        try:
            deleted_team_employee = self.controller.remove_work_arrangement(pk)
            return Response(status=status.HTTP_204_NO_CONTENT)
        except (domain_exceptions.ObjectEntityDoesNotExist,
                domain_exceptions.EmployeeHasOneTeam
                ) as e:
            return Response(e.message, status=status.HTTP_400_BAD_REQUEST)








