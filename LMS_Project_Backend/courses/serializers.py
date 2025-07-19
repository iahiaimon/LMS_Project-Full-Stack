from rest_framework.serializers import ModelSerializer

from .models import Course


class CourseSerializer(ModelSerializer):
    class Meta:
        model = Course
        fields = [
            "id",
            "title",
            "description",
            "price",
            "duration",
            "teacher_id",
            "category_id",
            "is_active",
            "created_at",
            "updated_at",
        ]
