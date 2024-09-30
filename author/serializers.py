from rest_framework import serializers
from .models import author

class AuthorSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(many=False)
    class Meta:
        model = author
        fields = ['user','bios', 'image','social_media_links']
