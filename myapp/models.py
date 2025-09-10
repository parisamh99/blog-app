from django.db import models

# Create your models here.
from django.db import models
class Contact(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(null=True)
    subject = models.CharField(max_length=255)
    message = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
# Create your models here.
    class Meta:
        ordering = ['-created']

    def __str__(self):
        return self.name  
