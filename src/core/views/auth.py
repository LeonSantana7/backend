from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny, IsAuthenticated
from django.contrib.auth import authenticate, login, logout
from django.middleware.csrf import get_token
from ..serializers.auth import UserSerializer

class CsrfTokenView(APIView):
    permission_classes = [AllowAny]
    def get(self, request):
        token = get_token(request)
        return Response({'csrfToken': token})

class LoginView(APIView):
    permission_classes = [AllowAny]
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            serializer = UserSerializer(user)
            return Response({'success': True, 'user': serializer.data})
        return Response({'success': False, 'detail': 'Credenciais inválidas'}, status=status.HTTP_401_UNAUTHORIZED)

class LogoutView(APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request):
        logout(request)
        return Response({'success': True})

class VerifyView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        serializer = UserSerializer(request.user)
        return Response({'isAuthenticated': True, 'user': serializer.data})
