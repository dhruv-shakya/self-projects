from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('update_post/', views.update_post, name='update_post'),
    path('addlike/', views.addlike, name='addlike'),
    path('addcomment/', views.addcomment, name='addcomment'),
    path('deletepost/<post_id>', views.deletepost, name='deletepost'),
]
