from django.urls import path

from .views import *


urlpatterns = [
    path('profile/', UserProfileViewSet.as_view()),
    path('confirm_email/<str:token>/', ConfirmEmailView.as_view(), name='confirm_email'),
]