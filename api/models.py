from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Todo(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    task=models.CharField(max_length=100)
    created_date=models.DateTimeField(auto_now_add=True)
    is_active=models.BooleanField(default=True)