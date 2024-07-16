from django.urls import path

from API.views.filters import FilterListView
from API.views.tasks import TaskListView, TaskDetailView

urlpatterns = [
    path('filters/', FilterListView.as_view()),
    path('tasks/', TaskListView.as_view()),
    path('tasks/<int:task_id>/', TaskDetailView.as_view()),
]
