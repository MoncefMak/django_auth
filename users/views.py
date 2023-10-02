from rest_framework import generics, status
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


class RegisterView(BaseCreateUserView):
    serializer_class = CustomerSerializer

    def post(self, request):
        return self.create_user(self.serializer_class, request)


class CreateStuffUserView(BaseCreateUserView):
    permission_classes = [IsAuthenticated & SuperAdminPermission]
    serializer_class = StuffSerializer

    def post(self, request):
        return self.create_user(self.serializer_class, request)


class SuperAdminUserView(BaseCreateUserView):
    permission_classes = [IsAuthenticated & SuperAdminPermission]
    serializer_class = SuperAdminSerializer

    def post(self, request):
        return self.create_user(self.serializer_class, request)
