from django.shortcuts import render
from django.shortcuts import render
from rest_framework import generics,status
from .serializers import UserRegistrationSerializer
from users.models import CustomUser
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny,IsAuthenticated
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
# Create your views here.
class CreateUserView(generics.CreateAPIView):
    queryset =CustomUser.objects.all()
    serializer_class = UserRegistrationSerializer


class BlackListToken(APIView):
    permission_classes = [AllowAny]
    authentication_classes = ()

    def post(self, request):
        try:
            refresh_token = request.data["refresh_token"]
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response(status=status.HTTP_205_RESET_CONTENT)
        except Exception as e:
            return Response(status=status.HTTP_400_BAD_REQUEST)
class TestView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self,request):
        return Response(status= status.HTTP_200_OK)