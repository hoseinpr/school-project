from django.contrib import admin
from .models import Slider, Banner, Article

@admin.register(Slider)
class SliderAdmin(admin.ModelAdmin):
    list_display = ('id', 'image', 'caption', 'order', 'created_at')
    search_fields = ('caption',)
    list_filter = ('created_at',)

@admin.register(Banner)
class BannerAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'image', 'link', 'created_at')
    search_fields = ('title', 'link')
    list_filter = ('created_at',)

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'created_at', 'updated_at')
    search_fields = ('title', 'content', 'author__username')
    list_filter = ('created_at', 'updated_at', 'author')