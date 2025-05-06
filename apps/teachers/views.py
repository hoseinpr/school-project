from django.shortcuts import render

from django.views.generic import TemplateView

class TeacherListView(TemplateView):
    template_name = 'teachers/teachers_list.html'

class TeacherDetailView(TemplateView):
    template_name = 'teachers/teacher_detail.html'
