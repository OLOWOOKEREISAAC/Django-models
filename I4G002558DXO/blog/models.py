import datetime
from django.db import models
from django.contrib.auth import get_user_model

class Post(models.Model):
    Title = models.CharField(max_length=200, null=True)
    Text = models.TextField()
    # # Author = models.ForeignKey(get_user_model(), on_delete=)
    Created_date = models.DateTimeField(auto_now_add=True, blank=True)
    Published_date = models.DateTimeField(auto_now_add=False, blank=True)