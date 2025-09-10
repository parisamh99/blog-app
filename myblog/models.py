from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField(default='null')
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    published = models.DateTimeField(null=True)
    status = models.BooleanField(default=False)
    counted_view = models.IntegerField(default=0)
    image = models.ImageField(upload_to='myblog/', default='myblog/default.jpg')
    category = models.ManyToManyField(Category,)
    #tag
    
    def __str__(self):
        return self.title