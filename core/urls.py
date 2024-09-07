
from django.contrib import admin
from django.urls import path, include
from apps.telegram.views import message_handler
from rest_framework.permissions import AllowAny
from apps.application.views import StudentApplicationView
from django.conf import settings
from django.conf.urls.static import static


from drf_yasg.views import get_schema_view
from drf_yasg import openapi


schema_view = get_schema_view(
   openapi.Info(
      title="Snippets API",
      default_version='v1',
      description="Test description",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@snippets.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes = (AllowAny, ),
)


urlpatterns = [
    path('webhook/', message_handler),
    path('admin/', admin.site.urls),
    path('student-application/', StudentApplicationView.as_view(), name='application-generator'),
    path('api/v1/', include('apps.common.urls')),
    path('api/v1/', include('apps.news.urls')),
    path('api/v1/', include('apps.education.urls')),
    path('api/v1/', include('apps.application.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.CONTRACT_URL, document_root=settings.CONTRACT_ROOT)


urlpatterns += [
   path('swagger<format>/', schema_view.without_ui(cache_timeout=0), name='schema-json'),
   path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
   path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]