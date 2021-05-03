from django.http import JsonResponse
from groups.models import Group
from groups.serializers import GroupSerializer

from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics, mixins

from groups.serializers import GroupSerializer
