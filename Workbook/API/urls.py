from django.urls import path

from API.views.filters import FilterListView
from API.views.healf_check import HealthCheckView

urlpatterns = [
    path('check/', HealthCheckView.as_view()),
    path('filters/', FilterListView.as_view()),
]
