"""
Serializer module is responsible for converting data to and from Entities and API requests. It also validate api request
data. It would be be useful in define separate request and response data models and not use Entities here. However, we
just use entities and some data models some requests and responses.
"""

from rest_framework import serializers
from domain.usecases.data_models.manage_employees_data_models import EmployeePresenterData
from domain.usecases.data_models.manage_employees_data_models import CreateEmployeeRequestData
from domain.usecases.data_models.manage_employees_data_models import UpdateEmployeeMRequestData
import domain.usecases.data_models.manage_team_data_models as team_data
from domain.entities.team import TeamEntity


class PresentEmployeeDataSerializer(serializers.Serializer):
    id = serializers.IntegerField(required=False, allow_null=True)
    name = serializers.CharField(max_length=50)
    employee_id = serializers.CharField(max_length=5)
    # assume an employee can be paid until 1000.xx(max length=7) per hour in the Alien company
    hourly_rate = serializers.DecimalField(max_digits=7, decimal_places=2)
    # default employee type is full time
    employee_type = serializers.IntegerField()
    created_at = serializers.DateTimeField()
    updated_at = serializers.DateTimeField()
    is_a_leader = serializers.BooleanField()
    pay = serializers.DecimalField(max_digits=13, decimal_places=2, allow_null=True)

    def __str__(self):
        return self.name

    def create(self, validated_data):
        """
        Create and return complete instance of Employee Entity based on validated data
        :param validated_data:
        :return:
        """
        return EmployeePresenterData(**validated_data)

    def update(self, instance, validated_data):
        """
        Validate employee entity at serializer boundary level
        :param instance:
        :param validated_data:
        :return:
        """
        instance.id = validated_data.get("id", instance.id)
        instance.name = validated_data.get("name", instance.name)
        instance.employee_id = validated_data.get("employee_id", instance.employee_id)
        instance.hourly_rate = validated_data.get("hourly_rate", instance.hourly_rate)
        instance.employee_type = validated_data.get("employee_type", instance.employee_type)
        instance.created_at = validated_data.get("created_at", instance.created_at)
        instance.updated_at = validated_data.get("updated_at", instance.updated_at)
        instance.is_a_leader = validated_data.get("is_a_leader", instance.is_a_leader)
        instance.pay = validated_data.get("pay", instance.pay)
        return instance


class UpdateEmployeeRequestSerializer(serializers.Serializer):
    """
    Serializer for update employee request
    """
    id = serializers.IntegerField(required=False, allow_null=True)
    name = serializers.CharField(max_length=50)
    employee_id = serializers.CharField(max_length=5)
    # assume an employee can be paid until 1000.xx(max length=7) per hour in the Alien company
    hourly_rate = serializers.DecimalField(max_digits=7, decimal_places=2)

    def create(self, validated_data):
        """
        Create and return complete instance of Employee Entity based on validated data
        :param validated_data:
        :return:
        """
        return UpdateEmployeeMRequestData(**validated_data)

    def update(self, instance, validated_data):
        """
        Validate employee entity at serializer boundary level
        :param instance:
        :param validated_data:
        :return:
        """
        instance.id = validated_data.get("id", instance.id)
        instance.name = validated_data.get("name", instance.name)
        instance.employee_id = validated_data.get("employee_id", instance.employee_id)
        instance.hourly_rate = validated_data.get("hourly_rate", instance.hourly_rate)
        return instance


class CreateWorkArrangement(serializers.Serializer):
    percentage = serializers.IntegerField()
    description = serializers.CharField(allow_null=True, allow_blank=True)

    def create(self, validated_data):
        pass

    def update(self, instance, validated_data):
        pass


class CreateEmployeeSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=50)
    employee_id = serializers.CharField(max_length=5)
    # assume an employee can be paid until 1000.xx(max length=7) per hour in the Alien company
    hourly_rate = serializers.DecimalField(max_digits=7, decimal_places=2)
    # default employee type is full time
    employee_type = serializers.IntegerField()
    team_id = serializers.IntegerField()
    work_arrangement = serializers.IntegerField(allow_null=True, required=False)

    def create(self, validated_data):
        """
        Create and return complete instance of Employee Entity based on validated data
        :param validated_data:
        :return:
        """
        return CreateEmployeeRequestData(**validated_data)

    def update(self, instance, validated_data):
        """
        Validate employee entity at serializer boundary level
        :param instance:
        :param validated_data:
        :return:
        """
        instance.name = validated_data.get("name", instance.name)
        instance.employee_id = validated_data.get("employee_id", instance.employee_id)
        instance.hourly_rate = validated_data.get("hourly_rate", instance.hourly_rate)
        instance.employee_type = validated_data.get("employee_type", instance.employee_type)
        instance.team_id = validated_data.get("team_id", instance.team_id)
        instance.work_arrangement = validated_data.get("work_arrangement", instance.work_arrangement)
        return instance


class CreateTeamSerializer(serializers.Serializer):
    id = serializers.IntegerField(required=False, allow_null=True)
    name = serializers.CharField(max_length=50)
    description = serializers.CharField()
    leader_id = serializers.IntegerField(allow_null=True)

    def create(self, validated_data):
        """
        Create and return complete instance of team Entity based on validated data
        :param validated_data:
        :return:
        """
        return team_data.CreateTeamRequestData(**validated_data)

    def update(self, instance, validated_data):
        """
        Validate team entity at serializer boundary level
        :param instance:
        :param validated_data:
        :return:
        """
        if validated_data.get("id", instance.id):
            instance.id = validated_data.get("id", instance.id)

        instance.name = validated_data.get("name", instance.name)
        instance.description = validated_data.get("description", instance.description)
        instance.leader_id = validated_data.get("leader_id", instance.leader_id)

        return instance


class PresentTeamSerializer(serializers.Serializer):
    id = serializers.IntegerField(required=False, allow_null=True)
    name = serializers.CharField(max_length=50)
    description = serializers.CharField()
    created_at = serializers.DateTimeField()
    updated_at = serializers.DateTimeField()

    def create(self, validated_data):
        """
        Create and return complete instance of team Entity based on validated data
        :param validated_data:
        :return:
        """
        return TeamEntity(**validated_data)

    def update(self, instance, validated_data):
        """
        Validate team entity at serializer boundary level
        :param instance:
        :param validated_data:
        :return:
        """
        instance.id = validated_data.get("id", instance.id)
        instance.name = validated_data.get("name", instance.name)
        instance.description = validated_data.get("description", instance.description)
        instance.created_at = validated_data.get("created_at", instance.created_at)
        instance.updated_at = validated_data.get("updated_at", instance.updated_at)

        return instance


class TeamLeaderPresenterSerializer(serializers.Serializer):
    leader = PresentEmployeeDataSerializer(serializers.Serializer)
    teams = PresentTeamSerializer(serializers.Serializer, many=True)

    def create(self, validated_data):
        """
        Create and return complete instance of team Entity based on validated data
        :param validated_data:
        :return:
        """
        return team_data.PresentTeamLeaderRequestData(**validated_data)

    def update(self, instance, validated_data):
        """
        Validate team entity at serializer boundary level
        :param instance:
        :param validated_data:
        :return:
        """
        instance.leader = validated_data.get("leader", instance.leader)
        instance.teams = validated_data.get("teams", instance.team)
        return instance


class TeamLeaderRequestDataSerializer(serializers.Serializer):
    team_id = serializers.IntegerField()
    employee_id = serializers.IntegerField()

    def create(self, validated_data):
        """
        Create and return complete instance of team Entity based on validated data
        :param validated_data:
        :return:
        """
        return team_data.TeamLeaderRequestData(**validated_data)

    def update(self, instance, validated_data):
        """
        Validate team entity at serializer boundary level
        :param instance:
        :param validated_data:
        :return:
        """
        instance.team_id = validated_data.get("team_id", instance.team_id)
        instance.employee_id = validated_data.get("employee_id", instance.employee_id)
        return instance





