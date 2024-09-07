from django.shortcuts import render
from rest_framework  import generics
from apps.common.serializer import RegionListSerializer, DistrictsSerializer, SocialSerializer
from apps.common.models import Regions, Districts, Socials
from rest_framework.views import APIView
from rest_framework.response import Response


class RegionListApiView(generics.ListAPIView):
    serializer_class = RegionListSerializer
    queryset = Regions.objects.all()


class DistrictsByRegionApiView(generics.ListAPIView):
    serializer_class = DistrictsSerializer
    queryset = Districts.objects.all()

    def get_queryset(self):
        region_id = self.request.parser_context['kwargs'].get('pk', None)
        qs = super().get_queryset()
        return qs.filter(region_id=region_id)


class SocialApiView(generics.ListAPIView):
    serializer_class = SocialSerializer
    queryset = Socials.objects.all()


class GenderChoicesApiView(APIView):
    def get(self, request, *args, **kwargs):
        data = [
            {
                "key": "male",
                "value": "Male"
            },
            {
                "key": "female",
                "value": "Female"
            }
        ]
        return Response(data=data, status=200)