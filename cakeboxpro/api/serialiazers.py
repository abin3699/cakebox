from rest_framework import serializers
from cakebxapp.models import User,Cakes

class Userserializer(serializers.ModelSerializer):

    id=serializers.CharField(read_only=True)
    password=serializers.CharField(write_only=True)

    class Meta:
        model=User
        fields=["id","username","email","password","phone","address"]

    def create(self,validated_data):
        return User.objects.create_user(**validated_data)
    

class Cakeserializer(serializers.ModelSerializer):

    class Meta:
        model=Cakes
        fields="__all__"