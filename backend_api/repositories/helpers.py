from domain.entities.team import TeamEntity
from domain.entities.employee import EmployeeEntity
from domain.entities.work_time import WorkTimeEntity
from domain.entities.team_leader import TeamLeaderEntity
from domain.entities.team_employee import TeamEmployeeEntity
from domain.entities.work_arrangment import WorkArrangementEntity
from backend_api.models import Team
from backend_api.models import Employee
from backend_api.models import WorkTime
from ..models import WorkArrangement
from ..models import TeamEmployee


class DataConverter:

    @staticmethod
    def to_team_entity(team_obj: Team):

        team_entity = TeamEntity(id=team_obj.id,
                                 name=team_obj.name,
                                 description=team_obj.description,
                                 created_at=team_obj.created_at,
                                 updated_at=team_obj.updated_at
                                 )
        if team_obj.leader:
            # team has a leader
            team_entity.leader = DataConverter.to_employee_entity(team_obj.leader)
        return team_entity

    @staticmethod
    def from_team_entity(team_entity: TeamEntity):
        print("Converting to django model team instanct")
        team_model = Team(
            id=team_entity.id,
            name=team_entity.name,
            description=team_entity.description,
            leader=team_entity.leader)
        if team_entity.has_a_leader():
            # check if a team has a leader
            team_model.leader = DataConverter.from_employee_entity(team_entity.leader)
        return team_model

    @staticmethod
    def to_employee_entity(employee_obj: Employee):
        """
        Convert Employee django ORM model to Employee entity.
        :param employee_obj: Employee model
        :param total_hours: total hours of employeee work time
        :return:
        """
        total_hours = WorkTime.objects.get_employee_work_time(employee_obj.id)
        employee_entity = EmployeeEntity(
            id=employee_obj.id,
            name=employee_obj.name,
            employee_id=employee_obj.employee_id,
            employee_type=employee_obj.employee_type,
            hourly_rate=employee_obj.hourly_rate,
            created_at=employee_obj.created_at,
            updated_at=employee_obj.updated_at,
            is_a_leader=employee_obj.is_a_leader,
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
            percent=wa_model.percent,
            employee=DataConverter.to_employee_entity(wa_model.employee)

        )

    @staticmethod
    def to_work_time_entity(wt_model: WorkTime):
        return WorkTimeEntity(
            id=wt_model.id,
            hours=wt_model.hours,
            employee=DataConverter.to_employee_entity(wt_model.employee)
        )

    @staticmethod
    def to_team_leader_entity(leader: Employee, teams):
        tl_entities = []
        for team in teams:
            tl_entities.append(DataConverter.to_team_entity(team))
        return TeamLeaderEntity(
            leader=DataConverter.to_employee_entity(leader),
            teams=tl_entities
        )

    @staticmethod
    def to_team_employee_entity(te_model: TeamEmployee):
        return TeamEmployeeEntity(
            id=te_model.id,
            team=DataConverter.to_team_entity(te_model.team),
            employee=DataConverter.to_employee_entity(te_model.employee)
        )





