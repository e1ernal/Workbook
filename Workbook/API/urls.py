from django.urls import path

from API.views.filters import FilterListView
from API.views.tasks import TaskListView

urlpatterns = [
    path('filters/', FilterListView.as_view()),
    path('tasks/', TaskListView.as_view()),
]
