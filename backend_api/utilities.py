from domain.entities.team import TeamEntity
from domain.entities.employee import EmployeeEntity
from domain.entities.work_time import WorkTimeEntity
from domain.entities.team_leader import TeamLeaderEntity
from domain.entities.team_employee import TeamEmployeeEntity
from domain.entities.work_arrangment import WorkArrangementEntity
from backend_api.models import Team
from backend_api.models import Employee
from backend_api.models import WorkTime
from backend_api.models import WorkArrangement
from backend_api.models import TeamEmployee
from backend_api.models import TeamLeader


# helper methods
def get_team_leader(team_pk):

    try:
        print(team_pk)
        team_leader = TeamLeader.objects.get(team_id=team_pk)

        return team_leader.leader
    except TeamLeader.DoesNotExist:
        return None


def employee_is_a_leader(employee_pk):
    """
    Check if an employee is a leader of any team
    :param employee_pk:
    :return:
    """
    teams = TeamLeader.objects.filter(leader_id=employee_pk)
    # if an employee is a leader of one or more teams than return True otherwise False
    if len(teams) >= 1:
        return True
    else:
        return False


# data converters
class DataConverters:

    @staticmethod
    def to_team_entity(team_obj: Team):
        leader = get_team_leader(team_pk=team_obj.id)
        if leader:
            leader_entity = DataConverters.to_employee_entity(leader)
        else:
            leader_entity = None
        team_entity = TeamEntity(id=team_obj.id,
                                 name=team_obj.name,
                                 description=team_obj.description,
                                 created_at=team_obj.created_at,
                                 updated_at=team_obj.updated_at,
                                 leader=leader_entity
                                 )

        return team_entity

    @staticmethod
    def from_team_entity(team_entity: TeamEntity):
        team_model = Team(
            id=team_entity.id,
            name=team_entity.name,
            description=team_entity.description,
            created_at=team_entity.created_at,
            updated_at=team_entity.updated_at
        )
        if team_entity.has_a_leader:
            # check if a team has a leader
            team_model.leader = DataConverters.from_employee_entity(team_entity.leader)
        return team_model

    @staticmethod
    def to_employee_entity(employee_obj: Employee):
        """
        Convert Employee django ORM model to Employee entity.
        :param employee_obj: Employee model
        :param total_hours: total hours of employeee work time
        :return:
        """
        is_a_team_leader = employee_is_a_leader(employee_pk=employee_obj.id)
        print(F"Is a team leader: {is_a_team_leader}")
        total_hours = WorkTime.objects.get_employee_work_time(employee_obj.id)
        employee_entity = EmployeeEntity(
            id=employee_obj.id,
            name=employee_obj.name,
            employee_id=employee_obj.employee_id,
            employee_type=employee_obj.employee_type,
            hourly_rate=employee_obj.hourly_rate,
            created_at=employee_obj.created_at,
            updated_at=employee_obj.updated_at,
            is_a_leader=is_a_team_leader,
            total_work_hours=total_hours

        )
        return employee_entity

    @staticmethod
    def from_employee_entity(employee_entity: EmployeeEntity):
        return Employee(
            id=employee_entity.id,
            name=employee_entity.name,
            employee_id=employee_entity.employee_id,
            hourly_rate=employee_entity.hourly_rate,
            employee_type=employee_entity.employee_type,
            created_at=employee_entity.created_at,
            updated_at=employee_entity.updated_at
        )

    @staticmethod
    def to_work_arrangement_entity(wa_model: WorkArrangement):
        return WorkArrangementEntity(
            id=wa_model.id,
            percent=wa_model.percent,
            employee=DataConverters.to_employee_entity(wa_model.employee),
            team=DataConverters.to_team_entity(wa_model.team)

        )

    @staticmethod
    def to_work_time_entity(wt_model: WorkTime):
        return WorkTimeEntity(
            id=wt_model.id,
            hours=wt_model.hours,
            employee=DataConverters.to_employee_entity(wt_model.employee),
            work_arrangement=DataConverters.to_work_arrangement_entity(wt_model.work_arrangement)
        )

    @staticmethod
    def to_team_leader_entity(team_leader: TeamLeader):
        return TeamLeaderEntity(
            id=team_leader.id,
            leader=DataConverters.to_employee_entity(team_leader.leader),
            team=DataConverters.to_team_entity(team_leader.team),
            created_at=team_leader.created_at,
            updated_at=team_leader.updated_at
        )

    @staticmethod
    def to_team_employee_entity(te_model: TeamEmployee):
        return TeamEmployeeEntity(
            id=te_model.id,
            team=DataConverters.to_team_entity(te_model.team),
            employee=DataConverters.to_employee_entity(te_model.employee),
            created_at=te_model.created_at,
            updated_at=te_model.updated_at
        )


