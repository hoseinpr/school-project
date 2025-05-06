from django.db import models

# Create your models here.
# content/models.py
from django.db import models

class Slider(models.Model):
    image = models.ImageField(upload_to='sliders/')
    caption = models.CharField(max_length=255, blank=True, null=True)
    order = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Slider {self.id}"

class Banner(models.Model):
    image = models.ImageField(upload_to='banners/')
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    link = models.URLField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class Article(models.Model):
    title = models.CharField(max_length=255)
    summary = models.TextField(blank=True, null=True)
    content = models.TextField()
    image = models.ImageField(upload_to='articles/', blank=True, null=True)
    author = models.ForeignKey('users.User', on_delete=models.SET_NULL, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
