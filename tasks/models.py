from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=300, blank=True, null=True)
    description = models.CharField(max_length=5000, blank=True, null=True)
    create_date_time = models.DateTimeField(auto_now_add=True)
    update_date_time = models.DateTimeField(auto_now=True)
    completed = models.BooleanField(default=False, null=True)
    image = models.ImageField(upload_to="", blank = True, null = True)

    def __str__(self):
        return self.title
    
    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url
    @property
    def getTitle(self):
        try:
            title = self.title
        except:
            title = ''
        return title
    @property
    def getDescription(self):
        try:
            description = self.description
        except:
            description = ''
        return description   