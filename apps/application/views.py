from typing import Any
from rest_framework.generics import ListAPIView, CreateAPIView
from .serializer import ApplicationCreateSerializer, ApplicationDetailSerializer
from .models import Application
from rest_framework.permissions import IsAuthenticated
from django.views.generic import TemplateView


class ApplicationCreateAPIView(CreateAPIView):
    serializer_class = ApplicationCreateSerializer
    queryset = Application.objects.all()
    permission_classes = (IsAuthenticated, )


class ApplicationDetailAPIView(ListAPIView):
    queryset = Application.objects.all()
    serializer_class = ApplicationDetailSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        qs = super().get_queryset()
        return qs.filter(user=self.request.user)


class StudentApplicationView(TemplateView):
    template_name = "application.html"

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        application_id = self.request.GET.get('application_id')

        if application_id:
            try:
                context['application'] = Application.objects.get(id=application_id)
            except Application.DoesNotExist:
                context['application'] = None

        return context
