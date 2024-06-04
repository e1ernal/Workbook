from django.urls import path

from API.views.filters import FilterListView
from API.views.healf_check import HealthCheckView
from API.views.tasks import TaskListView

urlpatterns = [
    path('check/', HealthCheckView.as_view()),
    path('filters/', FilterListView.as_view()),
    path('tasks/', TaskListView.as_view()),
]
