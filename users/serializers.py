from rest_framework import serializers

from users.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "email", "username", "password", "role"]

    def create(self, validated_data):
        user = User.objects.create(
            email=validated_data['email'],
            username=validated_data['username'],
            role=validated_data['role']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user


class CustomerSerializer(UserSerializer):
    class Meta:
        model = User
        fields = ["id", "email", "username", "password", "role"]

    def create(self, validated_data):
        validated_data['role'] = User.Role.CUSTOMER
        return super().create(validated_data)


class StuffSerializer(UserSerializer):
    class Meta:
        model = User
        fields = ["id", "email", "username", "password", "role"]

    def create(self, validated_data):
        validated_data['role'] = User.Role.STUFF
        return super().create(validated_data)


class SuperAdminSerializer(UserSerializer):
    class Meta:
        model = User
        fields = ["id", "email", "username", "password", "role"]

    def create(self, validated_data):
        validated_data['role'] = User.Role.SUPERADMIN
        return super().create(validated_data)
