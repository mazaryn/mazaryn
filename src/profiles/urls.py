from django.urls import path
from .models import Profile
from .views import (my_profile_view, received_invites_view,invite_profiles_list_view,profile_list_view, send_invitation, 
                    remove_from_friends, accept_invitation, reject_invitation, ProfileListView,ProfileDetailView)

app_name = 'profiles'

urlpatterns = [
    
    path('', ProfileListView.as_view(), name = 'all-profiles-view'),
    path('myprofile/', my_profile_view,name='my-profile-view'),
    path('myprofile/my-invites/', received_invites_view, name = 'my-invites-view'),
    path('myprofile/to-invite/', invite_profiles_list_view, name = 'to-invite-view'),
    path('myprofile/send-invite/', send_invitation, name='send-invite-view'),
    path('myprofile/remove-friend/', remove_from_friends, name='remove-friend-view'),
    path('myprofile/my-invites/accept/', accept_invitation, name = 'accept-invite-view'),
    path('myprofile/my-invites/reject/', reject_invitation, name = 'reject-invite-view'),
    path('<slug>/', ProfileDetailView.as_view(), name = 'profile-detail-view'),

]