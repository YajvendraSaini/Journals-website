from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Journal(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField(max_length=200)
    document = models.FileField(upload_to='documents/')  
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.created_at.strftime('%Y-%m-%d %H:%M:%S')}"