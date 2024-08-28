from django.urls import path
from .views import post_list,post_detail,create_post,update_post,delete_post,profile

app_name='posts'

urlpatterns = [
    path('',post_list,name='post_list'),
    path('create_post',create_post,name='create_post'),
    path('user',profile,name='profile'),
    path('<slug:slug>',post_detail,name='post_detail'),
    path('<slug:slug>/update',update_post ,name='update_post'),
    path('delete/<slug:slug>',delete_post ,name='delete_post'),
]
