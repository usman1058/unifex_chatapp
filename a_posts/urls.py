from django.urls import path
from .views import *



urlpatterns=[
            path('',landing_page, name='landing-page'),
            path('chat/chat-create/',post_create,name="post-create"),
            path('chat/chat-create-flicker/',post_create_wc,name="post-create_wc"),
            path('chat/chat-delete/<pk>/',post_delete,name="post-delete"),
            path('chat/chat-edit/<pk>/',post_edit,name="post-edit"),
            path('chat/chat-page/<pk>/',post_page,name="post-page"),
             ]