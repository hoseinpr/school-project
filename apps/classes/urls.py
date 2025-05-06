from django.urls import path
from . import views

urlpatterns = [
    path('', views.ClassListView.as_view(), name='classes_list'),  # لیست کلاس‌ها
    path('<int:pk>/', views.ClassDetailView.as_view(), name='class_detail'),  # جزئیات کلاس
]
