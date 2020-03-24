from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from .views import HomeView
from .views import ManageTeamView
from .views import ManageEmployeesView
from .views import TeamLeaderView
from .views import TeamEmployeeView
from .views import WorkTimeView
from .views import WorkArrangementsView

employee_router = routers.SimpleRouter()
employee_router.register(r'employees', ManageEmployeesView, basename="employee")
team_router = routers.SimpleRouter()
team_router.register(r'teams', ManageTeamView, basename="team")
team_leaders_router = routers.SimpleRouter()
team_leaders_router.register(r'team-leaders', TeamLeaderView, basename="team-leader")
work_time_router = routers.SimpleRouter()
work_time_router.register(r'work-times', WorkTimeView, basename="work-time")

work_arrangement_router = routers.SimpleRouter()
work_arrangement_router.register(r'work-arrangements', WorkArrangementsView, basename="work-arrangement")

team_employees_router = routers.SimpleRouter()
team_employees_router.register(r'team-employees', TeamEmployeeView, basename="team-employee")


urlpatterns = [
    path("", HomeView.as_view(), name="home"),
    path("", include((employee_router.urls, "employees"), namespace="employees")),
    path("", include((team_router.urls, "teams"), namespace="teams")),
    path("", include((team_leaders_router.urls, "team_leaders"),namespace="team_leaders")),
    path("", include((team_employees_router.urls, "team_employees"), namespace="team_employees")),
    path("", include((work_time_router.urls, "work_time"), namespace="work_time")),
    path("", include((work_arrangement_router.urls, "work_arrangement"), namespace="work_arrangement"))

]
