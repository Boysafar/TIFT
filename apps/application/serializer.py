from rest_framework import serializers
from .models import Application
from rest_framework.exceptions import ValidationError
from apps.common.serializer import DistrictsSerializer
from apps.education.serializer import DirectionModelSerializer


class ApplicationCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Application
        fields = ('first_name', 'last_name',
                  'passport', 'pinfl',
                  'gender', 'direction',
                  'district', 'birth_date',
        )

    def create(self, validated_data):
        user = self.context['request'].user
        validated_data['user'] = user
        if Application.objects.filter(passport=validated_data['passport']).exists():
            raise ValidationError({
                "passport": "Application already created with this passport data"
            })
        return super().create(validated_data)


class ApplicationDetailSerializer(serializers.ModelSerializer):
    direction = DirectionModelSerializer()
    district = DistrictsSerializer()

    status = serializers.SerializerMethodField()
    gender = serializers.SerializerMethodField()

    class Meta:
        model = Application
        fields = ('first_name', 'last_name',
                  'passport', 'pinfl',
                  'gender', 'direction',
                  'district', 'birth_date',
                  'status', 'accepted',
                  'created_at',
        )

    def get_status(self, obj):
        return obj.get_status_display()

    def get_gender(self, obj):
        return obj.get_gender_display()
