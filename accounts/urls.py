from django.urls import path
from accounts.views import UserRegistrationView
from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView, TokenBlacklistView

urlpatterns = [
    path('users/', UserRegistrationView.as_view(), name='register'),
    path('token/', TokenObtainPairView.as_view(), name='token_create'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path("token/logout/", TokenBlacklistView.as_view(), name='token_logout'),
]