from rest_framework import serializers
from .models import Twitter,User

class UserOrganisationSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=["name","email","password","is_manager"]

class TwitterSerializer(serializers.ModelSerializer):
    class Meta:
        model=Twitter
        fields=["tweet"]

class ViewTwitterSerializer(serializers.ModelSerializer):
    class Meta:
        model=Twitter
        fields="__all__"