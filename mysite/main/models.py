from django.db import models
from datetime import datetime

# Create your models here.


class Tutorial(models.Model):
    tutorial_title = models.CharField(max_length=200)
    tutorial_content = models.TextField()
    tutorial_published = models.DateTimeField(
        "date published", default=datetime.now)

    # This acts as an override for the default "view" when the object is called in render()
    def __str__(self):
        return self.tutorial_title
