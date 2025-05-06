from django.urls import path
from . import views

urlpatterns = [
    path('', views.TeacherListView.as_view(), name='teachers_list'),  # لیست معلمان
    path('<int:pk>/', views.TeacherDetailView.as_view(), name='teacher_detail'),  # جزئیات معلم
]
