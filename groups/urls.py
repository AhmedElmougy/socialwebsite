from django.urls import path
from groups import views 

app_name = 'groups'

urlpatterns = [
    path('new/',views.GroupCreateView.as_view(),name='create_group'),
    path('edit/<int:pk>/<slug:slug>/',views.GroupUpdateView.as_view(),name='edit_group'),
    path('delete/<int:pk>/<slug:slug>/',views.GroupDeleteView.as_view(),name='delete_group'),
    path('<int:pk>/<slug:slug>/',views.GroupDetailView.as_view(),name='group_details'),
    path('',views.GroupListView.as_view(),name='group_list'),
    path('join/<int:pk>/<slug:slug>/',views.JoinGoup.as_view(),name='join_group'),
    path('leave/<int:pk>/<slug:slug>/',views.LeaveGoup.as_view(),name='leave_group'),
]
