from django.shortcuts import render

from django.views.generic import TemplateView

class ClassListView(TemplateView):
    template_name = 'classes/classes_list.html'

class ClassDetailView(TemplateView):
    template_name = 'classes/class_detail.html'
