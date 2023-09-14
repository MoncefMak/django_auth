# views.py
from rest_framework import generics
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .models import User
from .permissions import SuperAdminPermission
from .serializers import CustomerSerializer, StuffSerializer, SuperAdminSerializer


class BaseCreateUserView(generics.CreateAPIView):
    def create_user(self, serializer_class, request):
        serializer = serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


#
class RegisterView(BaseCreateUserView):
    def post(self, request):
        return self.create_user(CustomerSerializer, request)


class CreateStuffUserView(BaseCreateUserView):
    permission_classes = [IsAuthenticated and SuperAdminPermission]
    required_role = User.Role.SUPERADMIN

    def post(self, request):
        return self.create_user(StuffSerializer, request)


class SuperAdminUserView(BaseCreateUserView):
    permission_classes = [IsAuthenticated and SuperAdminPermission]

    def post(self, request):
        return self.create_user(SuperAdminSerializer, request)

