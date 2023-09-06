from django.contrib.auth import login
from django.contrib.auth import get_user_model

from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken

from .serializers import CustomUserSerializer

User = get_user_model()


class UserProfileViewSet(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = CustomUserSerializer
    permission_classes = []


class ConfirmEmailView(generics.GenericAPIView):
    @staticmethod
    def get(request, token):
        try:
            user = User.objects.get(token_auth=token)
            user.is_active = True
            user.save()

            login(request, user)
            refresh = RefreshToken.for_user(user)
            return Response({
                'refresh': str(refresh),
                'access': str(refresh.access_token),
            }, status=status.HTTP_200_OK)
        except User.DoesNotExist:
            return Response({'detail': 'Invalid token'}, status=status.HTTP_400_BAD_REQUEST)


