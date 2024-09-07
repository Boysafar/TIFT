from django.urls import path
from .views import ApplicationCreateAPIView, ApplicationDetailAPIView


urlpatterns = [
    path('application-created/', ApplicationCreateAPIView.as_view()),
    path('application-statuses/', ApplicationDetailAPIView.as_view()),
]