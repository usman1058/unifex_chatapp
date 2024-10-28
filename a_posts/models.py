import uuid
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