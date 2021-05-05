from groups.serializers import GroupSerializer
from .models import Group

from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action


class GroupViewSet(viewsets.ModelViewSet):
    serializer_class = GroupSerializer
    queryset = Group.objects.all()
