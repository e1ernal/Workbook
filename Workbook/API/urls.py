from django.urls import path

from API.views.healf_check import HealthCheckView

urlpatterns = [
    path('check/', HealthCheckView.as_view()),
]