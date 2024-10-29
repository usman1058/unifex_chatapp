import uuid
from django.conf import settings
from django.db import models

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=255)
    artist=models.CharField(max_length=400,null=True)
    url=models.URLField(max_length=300,null=True)
    image=models.URLField(max_length=200)
    body = models.TextField()
    created=models.DateTimeField(auto_now_add=True)
    id=models.CharField(max_length=300,unique=True,default=uuid.uuid4,primary_key=True,editable=False)
    
    def __str__(self):
        return str(self.title)
    class Meta:
        ordering=['-created']
        
        
        
class Post2(models.Model):
    title = models.CharField(max_length=255)
    artist=models.CharField(max_length=400,null=True)
    url=models.URLField(max_length=300,null=True)
    image = models.ImageField(upload_to='pics/', null=True, blank=True)
    body = models.TextField()
    created=models.DateTimeField(auto_now_add=True)
    id=models.CharField(max_length=300,unique=True,default=uuid.uuid4,primary_key=True,editable=False)
    
    def __str__(self):
        return str(self.title)
    class Meta:
        ordering=['-created']
        
    @property
    def avatar(self):
        if self.image:
            return self.image.url
        return f'{settings.STATIC_URL}post-pic/pics.svg'
