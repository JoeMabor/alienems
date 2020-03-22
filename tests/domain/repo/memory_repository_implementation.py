"""
Implementation of repositories using dict  for use cases unit tests.
"""
from domain.entities.employee import EmployeeEntity
from domain.entities.team import TeamEntity
from domain.entities.team_employee import TeamEmployeeEntity
from domain.entities.team_leader import TeamLeaderEntity
from domain.entities.work_arrangment import WorkArrangementEntity
from domain.entities.work_time import WorkTimeEntity
from domain.usecases.repositories.team_repository import TeamRepoPort
from domain.usecases.repositories.employee_repository import EmployeeRepoPort
from domain.usecases.repositories.team_employees_repository import TeamEmployeeRepoPort
from domain.usecases.repositories.team_leader_repository import TeamLeaderRepoPort
from domain.usecases.repositories.work_arrangement_repository import WorkArrangementRepoPort
from domain.usecases.repositories.work_time_repository import WorkTimeRepoPort


class MemoryDB:
    """Memory database. Store Entities in dictionaries using ids"""
    def __init__(self,
                 teams={},
                 employees={},
                 team_leaders={},
                 team_employees={},
                 work_arrangements={},
                 work_time={}
                 ):
        self.teams = teams
        self.employees = employees
        self.team_leaders = team_leaders
        self.team_employees = team_employees
        self.work_arrangements = work_arrangements
        self.work_times = work_time


class TeamRepository(TeamRepoPort):
    def __init__(self, db: MemoryDB):
        self.db = db

    def retrieve_all(self):
        team_entities = []
        for team in self.db.teams.values():
            team_entities.append(team)
        return team_entities

    def retrieve_by_id(self, team_pk):
        try:
            team = self.db.teams[team_pk]
            return team
        except KeyError:
            return None

    def save(self, team_entity: TeamEntity):
        new_id = len(self.db.teams) + 1
        team_entity.id = new_id
        self.db.teams[new_id] = team_entity
        return team_entity

    def delete(self, team_pk: int):
        team = self.db.teams[team_pk]
        self.db.teams.pop(team_pk)
        return team

    def team_exists(self, team_pk: int):
        try:
            team = self.db.teams[team_pk]
            return team
        except KeyError:
            return None

    def has_a_leader(self, team_pk: int):
        if self.db.teams[team_pk].leader:
            return True
        else:
            return False


class EmployeeRepository(EmployeeRepoPort):
    def __init__(self, db: MemoryDB):
        self.db = db

    def retrieve_all(self):
        employees_entities = []
        for employee in self.db.employees.values():
            employees_entities.append(employee)
        return employees_entities

    def retrieve_by_id(self, employee_pk):
        try:
            employee = self.db.employees[employee_pk]
            return employee
        except KeyError:
            return None

    def save(self, employee_entity: EmployeeEntity):
        new_id = len(self.db.employees) + 1
        employee_entity.id = new_id
        self.db.employees[new_id] = employee_entity
        return employee_entity

    def delete(self, employee_pk: int):
        team = self.db.employees[employee_pk]
        self.db.teams.pop(employee_pk)
        return team

    def employee_exists(self, employee_pk):
        try:
            employee = self.db.employees[employee_pk]
            return employee
        except KeyError:
            return None

    def is_employee_id_unique(self, employee_id):
        for employee in self.db.employees.values():
            if employee.employee_id == employee_id:
                return False
            else:
                return True


class TeamLeaderRepository(TeamLeaderRepoPort):
    def __init__(self, db: MemoryDB):
        self.db = db

    def retrieve_all_team_leaders(self):
        tl_entities = []
        for tl_entity in self.db.team_leaders.values():
            tl_entities.append(tl_entity)
        return tl_entities

    def retrieve_team_leader(self, tl_pk: int):
        try:
            team_leader = self.db.team_leaders[tl_pk]
            return team_leader
        except KeyError:
            return None

    def save_team_leader(self, tl_entity: TeamLeaderEntity):
        new_id = len(self.db.team_leaders) + 1
        tl_entity.id = new_id
        self.db.team_leaders[new_id] = tl_entity
        return tl_entity


class TeamEmployeeRepository(TeamEmployeeRepoPort):
    def __init__(self, db: MemoryDB):
        self.db = db

    def retrieve_all_teams_employees(self):
        te_entities = []
        for te_entity in self.db.team_employees.values():
            te_entities.append(te_entity)
        return te_entities

    def retrieve_team_employees(self, te_pk: int):
        try:
            team_employee = self.db.team_employees[te_pk]
            return team_employee
        except KeyError:
            return None

    def save_team_employee(self, te_entity: TeamEmployeeEntity):
        new_id = len(self.db.team_employees) + 1
        te_entity.id = new_id
        self.db.team_employees[new_id] = te_entity
        return te_entity

    def delete_team_employee(self, te_pk):
        team_employee = self.db.team_employees[te_pk]
        self.db.team_employees.pop(te_pk)
        return team_employee

    def is_a_member(self, team_pk: int, employee_pk: int):
        for team_employee in self.db.team_employees.values():
            if team_employee.team.id == team_pk and team_employee.employee.id == employee_pk:
                return True
            else:
                return False

    def team_employee_exists(self, te_pk):
        try:
            team_employee = self.db.team_employees[te_pk]
            return team_employee
        except KeyError:
            return None

    def employee_has_more_teams(self, employee_pk):
        count = 0
        for team_employee in self.db.team_employees.values():
            if team_employee.employee.id == employee_pk:
                count += 1
            if count >= 2:
                return True
        return False


class WorkArrangement(WorkArrangementRepoPort):
    def __init__(self, db: MemoryDB):
        self.db = db

    def retrieve_all(self):
        wa_entities = []
        for wa_entity in self.db.work_arrangements.values():
            wa_entities.append(wa_entity)
        return wa_entities

    def retrieve_by_pk(self, wa_pk: int):
        try:
            wa_entity = self.db.work_arrangements[wa_pk]
            return wa_entity
        except KeyError:
            return None

    def save(self, wa_entity: WorkArrangementEntity):
        new_id = len(self.db.work_arrangements) + 1
        wa_entity.id = new_id
        self.db.team_employees[new_id] = wa_entity
        return wa_entity

    def delete(self, wa_pk: int):
        wa_entity = self.db.work_arrangements[wa_pk]
        self.db.team_employees.pop(wa_pk)
        return wa_entity

    def get_employee_work_arrangements_percent(self, employee_pk: int):
        total_percent = 0
        for work_arrangement in self.db.work_arrangements.values():
            if work_arrangement.employee.id == employee_pk:
                total_percent += work_arrangement.percent
        return total_percent

    def has_work_arrangement_with_team(self, employee_pk: int, team_pk: int):
        for work_arrangement in self.db.work_arrangements.values():
            if work_arrangement.team.id == team_pk and work_arrangement.employee.id == employee_pk:
                return True
            else:
                return False

    def work_arrangement_exists(self, wa_pk: int):
        try:
            wa_entity = self.db.work_arrangements[wa_pk]
            return wa_entity
        except KeyError:
            return None


class WorkTimeRepository(WorkTimeRepoPort):
    def __init__(self, db: MemoryDB):
        self.db = db

    def retrieve_all_work_times(self):
        wt_entities = []
        for wt_entity in self.db.work_times.values():
            wt_entities.append(wt_entity)
        return wt_entities

    def retrieve_work_time(self, wt_pk: int):
        try:
            wt_entity = self.db.work_times[wt_pk]
            return wt_entity
        except KeyError:
            return None

    def save_work_time(self, wt_entity: WorkTimeEntity):
        new_id = len(self.db.work_arrangements) + 1
        wt_entity.id = new_id
        self.db.team_employees[new_id] = wt_entity
        return wt_entity

    def retrieve_by_work_arrangement_pk(self, work_arrangement_pk):
        for work_time in self.db.work_times.values():
            if work_time.work_arrangement.id == work_arrangement_pk:
                return work_time
        return None



