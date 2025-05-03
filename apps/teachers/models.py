# teachers/models.py
from django.db import models

class Teacher(models.Model):
    name = models.CharField(max_length=255)
    position = models.CharField(max_length=255)  # سمت یا عنوان شغلی
    photo = models.ImageField(upload_to='teachers/')  # آپلود عکس معلم‌ها

    created_at = models.DateTimeField(auto_now_add=True)  # زمان ساخته شدن
    updated_at = models.DateTimeField(auto_now=True)      # زمان آخرین ویرایش

    def __str__(self):
        return self.name
