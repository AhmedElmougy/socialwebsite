from django.conf.urls import url
from django.urls import path
from posts import views

app_name = 'post'

urlpatterns = [
    path('new/<int:pk>/<slug:group>',views.PostCreateView.as_view(),name='new_post'),
    path('<int:pk>/',views.PostDetailView.as_view(),name='post_details'),
    path('post_edit/<int:pk>/',views.PostUpdateView.as_view(),name='edit_post'),
    path('post_delete/<int:pk>/',views.PostDeleteView.as_view(),name='delete_post'),
    path('new_comment/<int:post>/',views.CommentCreateView.as_view(),name='new_comment'),
    path('comment_edit/<int:pk>/',views.CommentUpdateView.as_view(),name='edit_comment'),
    path('comment_delete/<int:pk>/',views.CommentDeleteView.as_view(),name='delete_comment'),
]
