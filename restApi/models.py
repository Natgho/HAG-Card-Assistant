from django.db import models
from django.contrib.auth.models import User
from tinymce.models import HTMLField


# Create your models here.
class Articles(models.Model):
    article_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)
    image1_url = models.URLField(max_length=255)
    image2_url = models.URLField(max_length=255)
    video_link = models.URLField(max_length=255)
    content = HTMLField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    lang = models.CharField(max_length=10)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        db_table = "articles"
