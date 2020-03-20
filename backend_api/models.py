
"""
backend_api django ORM models that map directly to database.
"""


from django.db import models


class Employee(models.Model):
    """
    A model that map to  employees table im the database. It is related to employee type by foreighn key
    employee_type and referenced by WorkTime, TeamLeader, TeamEmployee models.
    """
    EmployeeTYPES = (
        (1, "Full time"),
        (2, "Part time")
    )
    name = models.CharField(max_length=50)
    employee_id = models.CharField(max_length=5, unique=True)
    # assume an employee can be paid until 1000.xx(max length=7) per hour in the Alien company
    hourly_rate = models.DecimalField(max_digits=7, decimal_places=2)
    is_a_leader = models.BooleanField(default=False)
    # default employee type is full time
    employee_type = models.PositiveIntegerField(choices=EmployeeTYPES, default=1)
    created_at = models.DateTimeField(auto_now=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True)

    def __str__(self):
        return self.name


class Team(models.Model):
    """
    A model that maps to  teams table in the database. Team may not have a leader if it doesn't have team employees,
    """
    name = models.CharField(max_length=50)
    description = models.TextField(null=True, blank=True)
    # set to null if an employee who is the team leader is deleted before it can be assigned another leader
    leader = models.ForeignKey(Employee, related_name="leader", on_delete=models.SET_NULL, null=True, blank=True)
    created_at = models.DateTimeField(auto_now=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True)

    def __str__(self):
        # if leader is null leader is not shown in string represention of Team mode
        leader = "No group leader"
        if self.leader:
            leader = self.leader
        return F"{self.name} -> {leader}"


class TeamLeader(models.Model):
    """
    A model that maps teams employees table containing each team members.
    """
    leader = models.ForeignKey(Employee, related_name="teamLeader", on_delete=models.CASCADE)
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True)

    def __str__(self):
        return F"{self.leader} -> {self.team}"


class TeamEmployee(models.Model):
    """
    A model that maps teams employees table containing each team members.
    """
    employee = models.ForeignKey(Employee, related_name="teamEmployee", on_delete=models.CASCADE)
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True)

    def __str__(self):
        return F"{self.employee} -> {self.team}"


class WorkTimeManager(models.Manager):

    def get_employee_work_time(self, employee_pk):
        work_time_obj = WorkTime.objects.filter(employee_id=employee_pk)
        total_hours = 0
        for wt_model in work_time_obj:
            total_hours += wt_model.hours
        return total_hours


class WorkTime(models.Model):
    """
    A model that maps to work time table that has employees work time.
    Maximum hours is 40 hours. Part time worker can have multiple work time. All full time employee have 40 hours
    """
    hours = models.PositiveIntegerField()
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    objects = WorkTimeManager()

    def __str__(self):
        return F"{self.employee} -> {self.hours}"


class WorkArrangement(models.Model):
    """
    A model that maps to employee work arrangements table. Part time employees can have multiple work arrangements (job)
    but only if their total work time is equal or less than 40. Max percentage is 100%. Work arrangement is used
    for calculating employee work time(on creation/update) and report purposes.
    """
    percent = models.PositiveIntegerField()
    remarks = models.TextField(null=True, blank=True)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)

    def __str__(self):
        return F"{self.employee} -> {self.percent}"


