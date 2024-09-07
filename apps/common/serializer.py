from rest_framework import serializers
from apps.common.models import Regions, Districts, Socials


class RegionListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Regions
        fields = ('id', 'title')


class DistrictsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Districts
        fields = ('id', 'title')


class SocialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Socials
        fields = ('id', 'title')

