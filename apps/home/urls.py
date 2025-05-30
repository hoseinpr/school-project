from django.urls import path
from . import views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),   # صفحه اصلی
    path('about/', views.AboutView.as_view(), name='about'),  # صفحه درباره ما
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
