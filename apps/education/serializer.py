from rest_framework import serializers
from .models import Faculty, Director, Direction


class FacultyListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Faculty
        fields = ("id", "title", "degree", )


class DirectorModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Director
        fields = ('full_name', 'bio', 'phone_number', 'picture',)


class DirectionModelSerializer(serializers.ModelSerializer):
    language = serializers.SerializerMethodField()
    education_type = serializers.SerializerMethodField()

    class Meta:
        model = Direction
        fields = ('title', 'education_type', 'language', 'body')

    def get_language(self, obj):
        return obj.get_language_display()

    def get_education_type(self, obj):
        return obj.get_education_type_display()


class FacultyDetailSerializer(serializers.ModelSerializer):
    direction = DirectionModelSerializer(many=True)
    director = DirectorModelSerializer()
    degree = serializers.SerializerMethodField()

    class Meta:
        model = Faculty
        fields = ('title', 'body', 'degree', 'direction', 'director')

    def get_degree(self, obj):
        return obj.get_degree_display()
