from rest_framework import serializers
from .models import Favorites

class FavoritesSerializer(serializers.ModelSerializer):
    # user = serializers.StringRelatedField(many=False)
    # blog = serializers.StringRelatedField(many=False)
    class Meta:
        model = Favorites
        fields = ['user', 'blog']
        read_only_fields = ['user', 'blog']
