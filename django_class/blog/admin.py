from django.contrib import admin
from .models import Post, Profile


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ("title", "content", "price")
    list_filter = ("is_published",)
    search_fields = ("title", "content")


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    pass