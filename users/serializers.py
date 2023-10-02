from rest_framework import serializers

from users.models import User


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "email", "username", "password"]
        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data):
        validated_data['role'] = User.Role.CUSTOMER
        validated_data['is_staff'] = False
        return super().create(validated_data)


class StuffSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "email", "username", "password"]
        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data):
        validated_data['role'] = User.Role.STUFF
        validated_data['is_staff'] = False
        return super().create(validated_data)


class SuperAdminSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "email", "username", "password"]
        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data):
        validated_data['role'] = User.Role.SUPERADMIN
        validated_data['is_staff'] = True
        return super().create(validated_data)
