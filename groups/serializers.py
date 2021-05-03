from django.db.models import fields
from rest_framework import serializers
from .models import Group


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ['id', 'group_name', 'members',
                  'posts', 'created_by', 'created', 'updated']
        depth = 1
