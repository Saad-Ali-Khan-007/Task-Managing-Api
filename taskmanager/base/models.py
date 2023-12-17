from django.db import models

# Create your models here.
class Task(models.Model):
    name = models.CharField(max_length = 50)
    about = models.TextField(max_length = 250,null=True,blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    completed = models.BooleanField(default=False,null=True,blank=True)