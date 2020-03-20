from django.contrib import admin
from .models import Employee, Team, TeamEmployee, WorkTime, WorkArrangement, TeamLeader


# Registering models in admin

admin.site.register(Employee)
admin.site.register(Team)
admin.site.register(TeamLeader)
admin.site.register(TeamEmployee)
admin.site.register(WorkTime)
admin.site.register(WorkArrangement)

