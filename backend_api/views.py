
from rest_framework.response import Response
from rest_framework import status
from .serializers import CreateTeamSerializer
from .serializers import PresentTeamSerializer
from .serializers import PresentEmployeeDataSerializer
from .serializers import CreateEmployeeSerializer
from .serializers import UpdateEmployeeRequestSerializer
from.serializers import TeamLeaderPresenterSerializer
from.serializers import TeamLeaderRequestDataSerializer
from rest_framework import viewsets
from django.core.exceptions import ObjectDoesNotExist
from django.http import Http404
import domain.entities.validators as domain_exceptions

from .app_config import CONTROLLERS


class ManageTeamView(viewsets.ViewSet):
    # manage team controller
    controller = CONTROLLERS.manage_teams_controller()

    def get_team_object(self, team_pk=None):
        try:
            return self.controller.retrieve_team(team_pk=team_pk)
        except ObjectDoesNotExist:
            raise Http404

    def list(self, request):
        teams = self.controller.retrieve_all_teams()
        serializer = PresentTeamSerializer(teams, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        team = self.get_team_object(pk)
        serializer = PresentTeamSerializer(team)
        return Response(serializer.data)

    def create(self, request):
        serializer = CreateTeamSerializer(data=request.data)
        if serializer.is_valid(raise_exception=False):
            team_entity = serializer.save()
            try:
                new_team_entity = self.controller.create_team(team_entity=team_entity)
                serializer = PresentTeamSerializer(new_team_entity)
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            except domain_exceptions.TeamHasALeader as e:
                return Response(e.message, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk):
        print("Update a team")
        serializer = CreateTeamSerializer(data=request.data)
        if serializer.is_valid(raise_exception=False):
            team_entity = serializer.save()
            new_team_entity = self.controller.update_team(team_entity=team_entity)
            print(F"new Team entity: {team_entity.name}")
            serializer = PresentTeamSerializer(new_team_entity)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        try:
            deleted_team = self.controller.delete_team(pk)
            return Response(status=status.HTTP_204_NO_CONTENT)
        except ObjectDoesNotExist:
            return Response(ObjectDoesNotExist, status=status.HTTP_400_BAD_REQUEST)


class ManageEmployeesView(viewsets.ViewSet):
    # manage team controller
    controller = CONTROLLERS.manage_employee_controller()

    def get_employee_object(self, pk):
        try:
            return self.controller.retrieve_employee(pk)
        except ObjectDoesNotExist:
            raise Http404

    def list(self, request):
        employee = self.controller.retrieve_all_employees()
        serializer = PresentEmployeeDataSerializer(employee, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        employee = self.get_employee_object(pk)
        print(F"Employee: {employee}")
        serializer = PresentEmployeeDataSerializer(employee)
        return Response(serializer.data)

    def create(self, request):
        serializer = CreateEmployeeSerializer(data=request.data)

        if serializer.is_valid(raise_exception=False):
            request_data = serializer.save()
            print(F"Request employee Data: {serializer.data}")

            try:
                new_employee = self.controller.create_employee(request_data=request_data)
                serializer = PresentEmployeeDataSerializer(new_employee)
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            except (domain_exceptions.WorkArrangementPercentageOutOfRange,
                    domain_exceptions.TeamHasALeader,
                    domain_exceptions.WorkArrangementPercentageNull
                    ) as e:
                return Response(e.message, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk):
        print("Update a employee")
        serializer = UpdateEmployeeRequestSerializer(data=request.data)
        if serializer.is_valid(raise_exception=False):
            request_data = serializer.save()

            new_employee_entity = self.controller.update_employee(request_data=request_data)
            serializer = PresentEmployeeDataSerializer(new_employee_entity)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        try:
            deleted_team = self.controller.delete_employee(pk)
            return Response(status=status.HTTP_204_NO_CONTENT)
        except ObjectDoesNotExist:
            return Response(ObjectDoesNotExist, status=status.HTTP_400_BAD_REQUEST)


class TeamLeaderView(viewsets.ViewSet):
    # manage team controller
    controller = CONTROLLERS.team_leaders_controller()

    def list(self, request):
        teams = self.controller.retrieve_all_teams_leaders()
        serializer = PresentEmployeeDataSerializer(teams, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        try:
            new_team_entity = self.controller.retrieve_team_leader(leader_pk=pk)
            serializer = TeamLeaderPresenterSerializer(new_team_entity)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        except (
                domain_exceptions.EmployeeDoesNotExist,
                domain_exceptions.EmployeeIsNotALeader
        )as e:
            return Response(e.message, status=status.HTTP_400_BAD_REQUEST)

    def create(self, request):
        serializer = TeamLeaderRequestDataSerializer(data=request.data)
        if serializer.is_valid(raise_exception=False):
            request_data = serializer.save()
            try:
                new_team_entity = self.controller.assign_team_leader(request_data=request_data)
                serializer = TeamLeaderPresenterSerializer(new_team_entity)
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
        print("Update a team")
        serializer = TeamLeaderRequestDataSerializer(data=request.data)
        if serializer.is_valid(raise_exception=False):
            request_data = serializer.save()
            try:
                new_team_entity = self.controller.change_team_leader(request_data=request_data)
                serializer = TeamLeaderPresenterSerializer(new_team_entity)
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            except (
                    domain_exceptions.TeamDoesNotExist,
                    domain_exceptions.EmployeeDoesNotExist
            )as e:
                return Response(e.message, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)






