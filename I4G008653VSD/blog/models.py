from django.db import models
from django.contrib.auth import get_user_model


class Post(models.Model):
    Title = models.CharField(max_length=200)
    Text = models.TextField()
    Author = models.ForeignKey(
        get_user_model(), on_delete=models.CASCADE, default=1)
    Created_date = models.DateTimeField()
    Published_date = models.DateTimeField()
