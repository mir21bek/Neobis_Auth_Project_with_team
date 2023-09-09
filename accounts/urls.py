from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from .views import *


urlpatterns = [
    path('profile/', UserProfileViewSet.as_view()),
    path('confirm_email/<str:token>/', ConfirmEmailView.as_view(), name='confirm_email'),
<<<<<<< HEAD
    path('', TokenObtainPairView.as_view()),
    path('api/refresh/',TokenRefreshView.as_view()),
=======
>>>>>>> 8b0d891e9d584c70be0572167e6e5128ed5d8fc5
]