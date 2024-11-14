from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify
from django.contrib.auth import get_user_model
from tinymce.models import HTMLField
# Create your models here.

class Post(models.Model):
    # Model for new thread posting

    title = models.CharField(max_length=400)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    slug = models.SlugField(max_length=400, unique=True, blank=True)
    created_time = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
            super(Post, self).save(*args,**kwargs)


class ThreadCreator(models.Model):
    # Model for forum users
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    username = models.CharField(max_length=40, blank=True)
    slug = models.SlugField(max_length=400, unique=True, blank=True)
    userdescription = HTMLField()

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
            super(Post, self).save(*args,**kwargs)
