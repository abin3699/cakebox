from rest_framework import serializers
from cakebxapp.models import User,Cakes,Cake_variant,Cart

class Userserializer(serializers.ModelSerializer):

    id=serializers.CharField(read_only=True)
    password=serializers.CharField(write_only=True)

    class Meta:
        model=User
        fields=["id","username","email","password","phone","address"]

    def create(self,validated_data):
        return User.objects.create_user(**validated_data)

class Cakevariantserializer(serializers.ModelSerializer):
    id=serializers.CharField(read_only=True)

    class Meta:
        model=Cake_variant
        fields="__all__"

class Cakeserializer(serializers.ModelSerializer):

    # Catagory=serializers.StringRelatedField(read_only=True)
    Catagory=serializers.SlugRelatedField(read_only=True,slug_field="types")
    variants=Cakevariantserializer(many=True,read_only=True)

    class Meta:
        model=Cakes
        fields="__all__"


class Cartserializer(serializers.ModelSerializer):

    Cake_variant=serializers.CharField(read_only=True)
    user=serializers.CharField(read_only=True)
    status=serializers.CharField(read_only=True)
    date=serializers.CharField(read_only=True)

    class Meta:
        model=Cart
        fields="__all__"