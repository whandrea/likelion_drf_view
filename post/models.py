from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Tag(models.Model):
    id = models.AutoField(primary_key=True)
    name= models.CharField(max_length=50)

def image_upload_path(instance, filename):
    return f'{instance.pk}/{filename}'

class Post(models.Model):
    id=models.AutoField(primary_key=True)
    name= models.CharField(max_length=50)
    content = models.TextField(max_length=200)
    created_at= models.DateField(auto_now_add=True)
    updated_at= models.DateField(auto_now=True)
    tag= models.ManyToManyField(Tag,blank=True)
    image = models.ImageField(upload_to=image_upload_path,blank=True, null=True)
    likes = models.PositiveIntegerField(default=0)
    likes_user = models.ManyToManyField(User, related_name='like_post', blank=True)


class Comment(models.Model):
    id = models.AutoField(primary_key=True)
    post = models.ForeignKey(Post, blank=False, null=False, on_delete=models.CASCADE, related_name='comments')
    writer= models.ForeignKey(User, on_delete=models.CASCADE)
    content=models.TextField(max_length=200)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
