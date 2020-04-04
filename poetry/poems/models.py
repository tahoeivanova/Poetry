from django.db import models

# Create your models here.

class Poem(models.Model):
    poem_text = models.TextField(unique=True)
    poem_title = models.CharField(max_length=1000, unique=True)

    def __str__(self):
        return self.poem_title