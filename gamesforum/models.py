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




class Category(models.Model):
    #Model for different categories of forum
    name = models.CharField(max_length=120)
    description = models.Textfield
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Thread(models.Model):
    # Thread moodel for this project forum
    title = models.Charfield(max_length=255)
    userdescription = HTMLField()
    category = models.ForeignKey(Category, related_name='threads', on_delete=models.CASCADE)
    user = models.ForeignKey(User, related_name='threads', on_delete=models.CASCADE)
    slug = models.SlugField( blank=True, unique=True, null=True, max_length=400)
    created_time = models.DateTimeField(auto_now_add=True)
    updated_time = models.DateTimeField(auto_now= True)


