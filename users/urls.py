from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import RegisterView, CreateStuffUserView, SuperAdminUserView

urlpatterns = [
    path('api/register/', RegisterView.as_view(), name='register'),
    path('api/stuff/create/', CreateStuffUserView.as_view(), name='create-stuff'),
    path('api/superadmin/create/', SuperAdminUserView.as_view(), name='create-superadmin'),
    path('api/login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/login/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]

