from django.urls import path
from .views import GroupListView, PostUpdateView, PostDeleteView

app_name = 'groups'

urlpatterns = [
    path('', GroupListView.as_view(), name='all-groups-view'),
    path('<pk>/delete/', PostDeleteView.as_view(), name='group-post-delete'),
    path('<pk>/update/', PostUpdateView.as_view(), name='group-post-update')
]