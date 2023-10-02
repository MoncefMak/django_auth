from rest_framework import serializers
from users.models import User

class BaseUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "email", "username", "password"]
        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data):
        role = self.Meta.role
        is_staff = self.Meta.is_staff
        validated_data['role'] = role
        validated_data['is_staff'] = is_staff
        user = User.objects.create(**validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user

class CustomerSerializer(BaseUserSerializer):
    class Meta:
        role = User.Role.CUSTOMER
        is_staff = False

class StuffSerializer(BaseUserSerializer):
    class Meta:
        role = User.Role.STUFF
        is_staff = False

class SuperAdminSerializer(BaseUserSerializer):
    class Meta:
        fields = ["id", "email", "username", "password", "role"]
        extra_kwargs = {"password": {"write_only": True}}
        role = User.Role.SUPERADMIN
        is_staff = True
