from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from .views import ManageTeamView
from .views import ManageEmployeesView
from .views import TeamLeaderView
from .views import TeamEmployeeView

employee_router = routers.SimpleRouter()
employee_router.register(r'employees', ManageEmployeesView, basename="employees")
team_router = routers.SimpleRouter()
team_router.register(r'teams', ManageTeamView, basename="teams")
team_leaders_router = routers.SimpleRouter()
team_leaders_router.register(r'team-leaders', TeamLeaderView, basename="team-leaders")

team_employees_router = routers.SimpleRouter()
team_employees_router.register(r'team-employees', TeamEmployeeView, basename="team-employees")


urlpatterns = [
    path("", include(employee_router.urls)),
    path("", include(team_router.urls)),
    path("", include(team_leaders_router.urls)),
    path("", include(team_employees_router.urls))

]
