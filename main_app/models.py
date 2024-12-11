from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

class Story(models.Model):
    title = models.CharField(max_length= 100)
    chapters = models.IntegerField()
    synopsis = models.TextField(max_length = 500)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse("story_detail", kwargs={"story_id": self.id})
    
