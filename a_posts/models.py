import uuid
from django.conf import settings
from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=255)
    artist=models.CharField(max_length=400,null=True)
    auther=models.ForeignKey(User, on_delete=models.SET_NULL,null=True,related_name="posts")
    url=models.URLField(max_length=300,null=True)
    image=models.URLField(max_length=200)
    images = models.ImageField(upload_to='pics/', null=True, blank=True)
    body = models.TextField()
    likes=models.ManyToManyField(User,related_name='likedposts',through='LikedPost')
    tags=models.ManyToManyField("Tag")
    created=models.DateTimeField(auto_now_add=True)
    id=models.CharField(max_length=100,unique=True,default=uuid.uuid4,primary_key=True,editable=False)
    
    def __str__(self):
        return str(self.title)
    class Meta:
        ordering=['-created']
    @property
    def avatar(self):
        if self.image:
            return self.image.url
        return f'{settings.STATIC_URL}post-pic/pics.svg'
    
        
        
         
    @property
    def avatar(self):
        if self.image:
            return self.image.url
        return f'{settings.STATIC_URL}post-pic/pics.svg'
    
    
class Tag(models.Model):
    name = models.CharField(max_length=20)
    slug=models.SlugField(max_length=20,unique=True)
    order=models.IntegerField(null=True)
    
    def __str__(self):
        return str(self.name)
    
    class Meta:
         ordering=['order']
         

class Comment(models.Model):
    auther = models.ForeignKey(User, on_delete=models.SET_NULL,null=True, related_name='comments')
    parent_post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    body = models.CharField(max_length=150)
    likes=models.ManyToManyField(User,related_name='likedcomments',through='LikedComment')
    created=models.DateTimeField(auto_now_add=True)
    id=models.CharField(max_length=100,unique=True,default=uuid.uuid4,primary_key=True,editable=False)
    
    def __str__(self):
        try:
            return f'{self.auther.username} : {self.body[:30]}'
        except:
             return f'No Author : {self.body[:30]}'
    class Meta:
         ordering=['-created']
    
class Reply(models.Model):
    auther = models.ForeignKey(User, on_delete=models.SET_NULL,null=True, related_name='replies')
    parent_comment= models.ForeignKey(Comment, on_delete=models.CASCADE, related_name='replies')
    body = models.CharField(max_length=150)
    likes=models.ManyToManyField(User,related_name='likedreplies',through='Likedreply')
    created=models.DateTimeField(auto_now_add=True)
    id=models.CharField(max_length=100,unique=True,default=uuid.uuid4,primary_key=True,editable=False)
    
    def __str__(self):
        try:
            return f'{self.auther.username} : {self.body[:30]}'
        except:
             return f'No Author : {self.body[:30]}'
         
    class Meta:
         ordering=['-created']
    
class LikedPost(models.Model):
    post=models.ForeignKey(Post,on_delete=models.CASCADE)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    created=models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
            return f'{self.user.username} : {self.post.title}'
    
    
class LikedComment(models.Model):
    comment=models.ForeignKey(Comment,on_delete=models.CASCADE)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    created=models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
            return f'{self.user.username} : {self.comment.body[:30]}'
    
    
class LikedReply(models.Model):
    reply=models.ForeignKey(Reply,on_delete=models.CASCADE)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    created=models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
            return f'{self.user.username} : {self.reply.body[:30]}'
    
    
