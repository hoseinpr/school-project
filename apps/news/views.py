from django.shortcuts import render

from django.views.generic import TemplateView

class NewsListView(TemplateView):
    template_name = 'news/news_list.html'

class NewsDetailView(TemplateView):
    template_name = 'news/news_detail.html'
