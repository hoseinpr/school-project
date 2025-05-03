# news/models.py
from django.db import models
from django_jalali.db import models as jmodels  # برای تاریخ شمسی (jalali)

class News(models.Model):
    title = models.CharField(max_length=255)   # عنوان خبر
    summary = models.TextField()               # خلاصه خبر
    image = models.ImageField(upload_to='news/') # عکس خبر
    publish_date = jmodels.jDateField()         # تاریخ شمسی انتشار خبر

    created_at = models.DateTimeField(auto_now_add=True)  # تاریخ ایجاد (میلادی)
    updated_at = models.DateTimeField(auto_now=True)      # تاریخ بروزرسانی (میلادی)

    def __str__(self):
        return self.title
