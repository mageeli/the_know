from django.db import models
from django.db import models
from tinymce.models import HTMLField

class Post(models.Model):
    title = models.CharField(max_length=252)
    text = HTMLField()