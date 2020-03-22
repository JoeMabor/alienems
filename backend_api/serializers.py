"""
Serializer module is responsible for converting data to and from Entities and API requests. It also validate api request
data. It would be be useful in define separate request and response data models and not use Entities here. However, we
just use entities and some data models some requests and responses.
"""

from rest_framework import serializers
import domain.usecases.data_models.request_data_models as request_data_models
from domain.entities.employee import EmployeeEntity
from domain.entities.team import TeamEntity
from domain.entities.team_employee import TeamEmployeeEntity
from domain.entities.team_leader import TeamLeaderEntity
from domain.entities.work_arrangment import WorkArrangementEntity
from domain.entities.work_time import WorkTimeEntity


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
        return EmployeeEntity(**validated_data)

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
        return request_data_models.UpdateEmployeeMRequestData(**validated_data)

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
        return request_data_models.CreateEmployeeRequestData(**validated_data)

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
    leader_id = serializers.IntegerField(allow_null=True, required=False)

    def create(self, validated_data):
        """
        Create and return complete instance of team Entity based on validated data
        :param validated_data:
        :return:
        """
        return request_data_models.CreateTeamRequestData(**validated_data)

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


class UpdateTeamSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField(max_length=50)
    description = serializers.CharField()

    def create(self, validated_data):
        """
        Create and return complete instance of team Entity based on validated data
        :param validated_data:
        :return:
        """
        return request_data_models.UpdateTeamRequestData(**validated_data)

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
    id = serializers.IntegerField()
    created_at = serializers.DateTimeField()
    updated_at = serializers.DateTimeField()
    leader = PresentEmployeeDataSerializer(serializers.Serializer)
    team = PresentTeamSerializer(serializers.Serializer)

    def create(self, validated_data):
        """
        Create and return complete instance of team Entity based on validated data
        :param validated_data:
        :return:
        """
        return TeamLeaderEntity(**validated_data)

    def update(self, instance, validated_data):
        """
        Validate team entity at serializer boundary level
        :param instance:
        :param validated_data:
        :return:
        """
        instance.id = validated_data.get("id", instance.id)
        instance.created_at = validated_data.get("created_at", instance.created_at)
        instance.updated_at = validated_data.get("updated_at", instance.updated_at)
        instance.leader = validated_data.get("leader", instance.leader)
        instance.team = validated_data.get("team", instance.team)
        return instance


class TeamLeaderOrEmployeeRequestDataSerializer(serializers.Serializer):
    team_id = serializers.IntegerField()
    employee_id = serializers.IntegerField()

    def create(self, validated_data):
        """
        Create and return complete instance of team Entity based on validated data
        :param validated_data:
        :return:
        """
        return request_data_models.TeamLeaderOrEmployeeRequestData(**validated_data)

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


class UpdateTeamLeaderRequestDataSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    team_id = serializers.IntegerField()
    employee_id = serializers.IntegerField()

    def create(self, validated_data):
        """
        Create and return complete instance of team Entity based on validated data
        :param validated_data:
        :return:
        """
        return request_data_models.UpdateTeamLeaderRequestData(**validated_data)

    def update(self, instance, validated_data):
        """
        Validate team entity at serializer boundary level
        :param instance:
        :param validated_data:
        :return:
        """
        instance.id = validated_data.get("id", instance.id)
        instance.team_id = validated_data.get("team_id", instance.team_id)
        instance.employee_id = validated_data.get("employee_id", instance.employee_id)
        return instance


class PresentTeamEmployeeDataSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    created_at = serializers.DateTimeField()
    updated_at = serializers.DateTimeField()
    team = PresentTeamSerializer(serializers.Serializer)
    employee = PresentEmployeeDataSerializer(serializers.Serializer)

    def create(self, validated_data):
        """
        Create and return complete instance of team Entity based on validated data
        :param validated_data:
        :return:
        """
        return TeamEmployeeEntity(**validated_data)

    def update(self, instance, validated_data):
        """
        Validate team entity at serializer boundary level
        :param instance:
        :param validated_data:
        :return:
        """
        instance.id = validated_data.get("id", instance.id)
        instance.team = validated_data.get("team", instance.team)
        instance.employee = validated_data.get("employee", instance.employee)
        instance.created_at = validated_data.get("created_at", instance.created_at)
        instance.updated_at = validated_data.get("updated_at", instance.updated_at)
        return instance


class PresentWorkArrangementsDataSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    percent = serializers.IntegerField()
    remarks = serializers.CharField(allow_null=True, allow_blank=True)
    employee = PresentEmployeeDataSerializer(serializers.Serializer)
    team = PresentTeamSerializer(serializers.Serializer)

    def create(self, validated_data):
        """
        Create and return complete instance of team Entity based on validated data
        :param validated_data:
        :return:
        """
        return WorkArrangementEntity(**validated_data)

    def update(self, instance, validated_data):
        """
        Validate team entity at serializer boundary level
        :param instance:
        :param validated_data:
        :return:
        """
        instance.id = validated_data.get("id", instance.id)
        instance.percent = validated_data.get("percent", instance.percent)
        instance.remarks = validated_data.get("remarks", instance.remarks)
        instance.employee = validated_data.get("employee", instance.employees)
        instance.team = validated_data.get("team", instance.team)


class CreateWorkArrangementSerializer(serializers.Serializer):
    percent = serializers.IntegerField()
    employee_id = serializers.IntegerField()
    remarks = serializers.CharField(allow_null=True, required=False)
    team_id = serializers.IntegerField()

    def create(self, validated_data):
        """
        Create and return complete instance of team Entity based on validated data
        :param validated_data:
        :return:
        """
        return request_data_models.CreateWorkArrangementData(**validated_data)

    def update(self, instance, validated_data):
        """
        Validate team entity at serializer boundary level
        :param instance:
        :param validated_data:
        :return:
        """

        instance.percent = validated_data.get("percent", instance.percent)
        instance.employee_id = validated_data.get("employee_id", instance.employee_id)
        instance.remarks = validated_data.get("remarks", instance.remarks)
        instance.team_id = validated_data.get("team_id", instance.team_id)
        return instance


class UpdateWorkArrangementSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    percent = serializers.IntegerField()
    employee_id = serializers.IntegerField()
    remarks = serializers.CharField(allow_null=True, required=False)
    team_id = serializers.IntegerField()

    def create(self, validated_data):
        """
        Create and return complete instance of team Entity based on validated data
        :param validated_data:
        :return:
        """
        return request_data_models.UpdateWorkArrangementData(**validated_data)

    def update(self, instance, validated_data):
        """
        Validate team entity at serializer boundary level
        :param instance:
        :param validated_data:
        :return:
        """

        instance.id = validated_data.get("id", instance.id)
        instance.percent = validated_data.get("percent", instance.percent)
        instance.employee_id = validated_data.get("employee_id", instance.employee_id)
        instance.remarks = validated_data.get("remarks", instance.remarks)
        instance.team_id = validated_data.get("team_id", instance.team_id)
        return instance


class PresentWorkTimeDataSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    hours = serializers.IntegerField()
    # employee = PresentEmployeeDataSerializer(serializers.Serializer)
    work_arrangement = PresentWorkArrangementsDataSerializer(serializers.Serializer)

    def create(self, validated_data):
        """
        Create and return complete instance of team Entity based on validated data
        :param validated_data:
        :return:
        """
        return WorkTimeEntity(**validated_data)

    def update(self, instance, validated_data):
        """
        Validate team entity at serializer boundary level
        :param instance:
        :param validated_data:
        :return:
        """
        instance.id = validated_data.get("id", instance.id)
        instance.hours = validated_data.get("hours", instance.hours)
        instance.work_arrangement = validated_data.get("work_arrangement", instance.work_arrangement)
        # instance.employee = validated_data.get("employee", instance.employees)
