from django.db import models
from datetime import datetime

# Create your models here.


class HomePageContent(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    created_at = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return self.title
