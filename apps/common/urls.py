from apps.common.views import (
    RegionListApiView,
    DistrictsByRegionApiView,
    SocialApiView,
    GenderChoicesApiView
)
from django.urls import path

urlpatterns = [
    path('regions/', RegionListApiView.as_view()),
    path('<int:pk>/districts/', DistrictsByRegionApiView.as_view()),
    path('social/', SocialApiView.as_view()),
    path('genders/', GenderChoicesApiView.as_view()),
]

