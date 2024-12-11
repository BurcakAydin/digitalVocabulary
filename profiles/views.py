from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions
from profiles.serializers import RegisterSerializer, UserSerializer, ProfileSerializer
from rest_framework.generics import ListAPIView
from profiles.models import Profile, FollowRelation
from rest_framework import status
from django.shortcuts import get_object_or_404

class RegisterView(APIView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        user_serializer = UserSerializer(user)
        return Response(user_serializer.data)

class ProfileSearchView(ListAPIView):
    serializer_class = ProfileSerializer
    
    def get_queryset(self):
        
        username = self.request.query_params.get('username', '')

        if username:
            return Profile.objects.filter(user__username__icontains=username)
        return Profile.objects.none()
    

class FollowProfileView(APIView):
    def post(self, request, username):
        profile_to_follow = get_object_or_404(Profile, user__username=username)

        if request.user.profile == profile_to_follow:
            return Response({"error" : "You can not follow yourself."}, status=status.HTTP_400_BAD_REQUEST)
        
        FollowRelation.objects.get_or_create(follower=request.user.profile, following=profile_to_follow)
        return Response({"success": "User followed successfully."})
    
class UnfollowProfileView(APIView):
    def post(self, request, username):
        profile_to_unfollow = get_object_or_404(Profile, user__username=username)

        follow_relation = FollowRelation.objects.filter(follower=request.user.profile, following=profile_to_unfollow)
        if follow_relation.exists():
            follow_relation.delete()
            return Response({"success": "User unfollowed successfully."})
        else: 
            return Response({"error" : "You are not following this user."}, status=status.HTTP_400_BAD_REQUEST)
        

class FollowListView(ListAPIView):
    serializer_class = ProfileSerializer

    def get_queryset(self):
        
        user_profile = self.request.user.profile
        return user_profile.followers.all()
