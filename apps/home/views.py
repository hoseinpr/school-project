from django.shortcuts import render

from django.views.generic import TemplateView
from apps.content.models import Slider
from apps.content.models import Banner
from apps.news.models import News

class IndexView(TemplateView):
    template_name = 'home/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['sliders'] = Slider.objects.all().order_by('order')
        
    
        
        # دریافت همه بنرها از دیتابیس
        banners = Banner.objects.all()  # یا می‌توانید فیلتر هم کنید اگر نیاز دارید
        context['banners'] = banners

        latest_news = News.objects.all().order_by('-publish_date')[:3]  # جدیدترین 3 خبر
        context['latest_news'] = latest_news

        return context

class AboutView(TemplateView):
    template_name = 'home/about.html'
