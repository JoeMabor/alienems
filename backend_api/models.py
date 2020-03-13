
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
    employee_id = models.CharField(max_length=5)
    # assume an employee can be paid until 1000.xx(max length=7) per hour in the Alien company
    hourly_rate = models.DecimalField(max_digits=7, decimal_places=2)
    # default employee type is full time
    employee_type = models.PositiveIntegerField(choices=EmployeeTYPES, default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def is_full_time(self):
        """
        Check if an employee is full time or part time employee. Return if employee is a full time employee and false
        otherwise
        :return:
        """
        # return self.employee_type ==1
        if self.employee_type:
            return True
        else:
            return False

    def __str__(self):
        return self.name


class Team(models.Model):
    """
    A model that maps to  teams table in the database. Team may not have a leader if it doesn't have team employees,
    """
    name = models.CharField(max_length=50)
    description = models.TextField(null=True, blank=True)
    # set to null if an employee who is the team leader is deleted before it can be assigned another leader
    leader = models.ForeignKey(Employee, on_delete=models.SET_NULL, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        # if leader is null leader is not shown in string represention of Team mode
        leader = "No group leader"
        if self.leader:
            leader = self.leader
        return F"{self.name} -> {leader}"


class TeamEmployee(models.Model):
    """
    A model that maps teams employees table containing each team members.
    """
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    added_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return F"{self.employee} -> {self.team}"


class WorkTime(models.Model):
    """
    A model that maps to work time table that has employees work time.
    Maximum hours is 40 hours. Part time worker can have multiple work time. All full time employee have 40 hours
    """
    hours = models.PositiveIntegerField()
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)

    def __str__(self):
        return F"{self.employee} -> {self.hours}"


class WorkArrangement(models.Model):
    """
    A model that maps to employee work arrangements table. Part time employees can have multiple work arrangements (job)
    but only if their total work time is equal or less than 40. Max percentage is 100%. Work arrangement is used
    for calculating employee work time(on creation/update) and report purposes.
    """
    percentage = models.PositiveIntegerField()
    description = models.TextField(null=True, blank=True)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)

    def __str__(self):
        return F"{self.employee} -> {self.percentage}"


