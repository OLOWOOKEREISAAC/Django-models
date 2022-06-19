import datetime
from django.db import models
from django.contrib.auth import get_user_model

class Post(models.Model):
    Title = models.CharField(max_length=200, null=True)
    Text = models.TextField(null=True)
    # # Author = models.ForeignKey(get_user_model(), on_delete=)
    # Created_date = models.DateTimeField(default=datetime)
    # Published_date = models.DateTimeField(default=datetime)