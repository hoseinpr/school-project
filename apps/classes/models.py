# classes/models.py
from django.db import models

class Class(models.Model):
    title = models.CharField(max_length=255)  # عنوان کلاس
    description = models.TextField()           # توضیحات کلاس
    image = models.ImageField(upload_to='classes/')  # عکس مرتبط با کلاس

    created_at = models.DateTimeField(auto_now_add=True)  # تاریخ ایجاد
    updated_at = models.DateTimeField(auto_now=True)      # تاریخ آخرین بروزرسانی

    def __str__(self):
        return self.title
