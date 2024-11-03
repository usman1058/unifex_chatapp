from django.urls import path
from django.conf.urls.static import static
from .views import *



urlpatterns=[
            path('',landing_page, name='landing-page'),
            path('chat/chat-create/',post_create,name="post-create"),
            path('category/<tag>',landing_page,name="category"),
            path('chat/chat-flicker/',post_create_wc,name="post-create_wc"),
            path('chat/chat-delete/<pk>/',post_delete,name="post-delete"),
            path('comment-delete/<pk>/',comment_delete,name="comment-delete"),
            path('reply-delete/<pk>/',reply_delete,name="reply-delete"),
            path('chat/chat-edit/<pk>/',post_edit,name="post-edit"),
            path('chat/chat-page/<pk>/',post_page,name="post-page"),
            path('chat-page/<pk>/likes/',like_post,name="like-post"),
            path('chat-page/<pk>/likes_comment/',like_comment,name="like-comment"),
            path('chat-page/<pk>/likes_reply/',like_reply,name="like-reply"),
             ]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)