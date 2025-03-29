from rest_framework import generics, permissions
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authtoken.models import Token
from django.contrib.auth import get_user_model
from .serializers import UsersRegistrationSerializer, UsersLoginSerializer, AuthTokenSerializer
from django.shortcuts import get_object_or_404
from .serializers import FollowSerializer
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated


User = get_user_model()

#start task 0
class UsersRegistrationView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UsersRegistrationSerializer
    permission_classes = [permissions.AllowAny]

class UserLoginView(generics.GenericAPIView):
    serializer_class = UsersLoginSerializer
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({'token': token.key}, status=status.HTTP_200_OK)

class TokenRetrieveView(generics.RetrieveAPIView):
    serializer_class = AuthTokenSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        return Token.objects.get(user=self.request.user)
#end task 0

#start task 2
class FollowUserView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, user_id):
        user_to_follow = get_object_or_404(User, id=user_id)
        if request.user == user_to_follow:
            return Response({"detail": "You cannot follow yourself."}, status=status.HTTP_400_BAD_REQUEST)
        request.user.profile.following.add(user_to_follow)
        return Response({"detail": f"You are now following {user_to_follow.username}."}, status=status.HTTP_200_OK)

class UnfollowUserView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, user_id):
        user_to_unfollow = get_object_or_404(User, id=user_id)
        request.user.profile.following.remove(user_to_unfollow)
        return Response({"detail": f"You have unfollowed {user_to_unfollow.username}."}, status=status.HTTP_200_OK)
#end task 2