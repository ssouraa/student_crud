from .models import student
from rest_framework import serializers

class studentSerializer(serializers.ModelSerializer):
    class Meta:
        model = student
        fields=['sid','sname','marks']
    