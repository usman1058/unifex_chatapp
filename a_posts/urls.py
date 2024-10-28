from django.urls import path
from .views import *



urlpatterns=[path('',landing_page, name='landing-page'),
             path('chat/chat-create/',post_create,name="post-create"),
             path('chat/chat-delete/<pk>/',post_delete,name="post-delete"),]