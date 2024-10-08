from rest_framework import serializers
from .models import Tours

class ToursSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tours
        fields = ('id', 'title', 'description', 'price', 'user', 'created_at')