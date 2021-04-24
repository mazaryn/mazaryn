from django.contrib import admin
from .models import Profile , Relationship

# Register your models here.

@admin.register(Profile)
class ProfileModel(admin.ModelAdmin):
    list_filter = ('slug','created','first_name')
    # list_display = ('first_name','slug','created')

@admin.register(Relationship)
class RelationshipModel(admin.ModelAdmin):
    list_filter = ('status','created')
    list_display = ('sender','receiver','status')