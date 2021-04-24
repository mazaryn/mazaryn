from django.http import JsonResponse
from django.contrib.auth.models import User
# from drf_multiple_model.views import ObjectMultipleModelAPIView

from profiles.models import Profile, Relationship
from profiles.forms import ProfileModelForm

from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics, mixins

from .serializers import ProfileSerializer

class MyProfileView(APIView):
    def get_object(self, user):
        try:
            return Profile.objects.get(user=self.request.user)
        except Profile.objects.DoesNotExist:
            return Response({"error": "The profile does not exist"}, status=404)
    
    def get(self, request, user=None):
        instance = self.get_object(user)
        serializer = ProfileSerializer(instance)
        return Response(serializer.data)

@api_view(['GET', 'POST'])
def myprofile(request):
    profile = Profile.objects.get(user=request.user)
    update_flag = False

    if request.method == 'GET':
        serializer = ProfileSerializer(profile) 
        return Response(serializer.data)
    
class ReceivedInvitesList(generics.GenericAPIView, mixins.ListModelMixin):
    serializer_class = ProfileSerializer
    def get_queryset(self):
        profile = Profile.objects.get(user=self.request.user)
        queryset = Relationship.objects.invitations_received(profile)
        return queryset

    def get(self, request):
        return self.list(request)


class InvitesProfileList(generics.GenericAPIView, mixins.ListModelMixin):
    serializer_class = ProfileSerializer
    def get_queryset(self):
        sender = self.request.user
        queryset = Profile.objects.get_all_profiles_to_invite(sender)
        return queryset

    def get(self, request):
        return self.list(request)



class ProfileListView(generics.GenericAPIView, mixins.ListModelMixin, mixins.CreateModelMixin):
    serializer_class = ProfileSerializer

    def get_queryset(self):
        myself = self.request.user
        qs = Profile.objects.get_all_profiles(myself)
        return qs

    def get(self, request):
        return self.list(request)

    def post(self, request):
        return self.create(request)


























@api_view(['GET'])
def received_invites_view(request):
    # profile = Profile.objects.get(user=request.user)
    #obj = Relationship.objects.invitations_received(profile)
    obj = Relationship.objects.all()
    serializer = ProfileSerializer(obj, many=True)
    return Response(serializer.data)


def profile_list_view(request):
    myself = request.user
    profiles = Profile.objects.get_all_profiles(myself)
    serializer = ProfileSerializer(profiles, many=True)
    return Response(serializer.data)
