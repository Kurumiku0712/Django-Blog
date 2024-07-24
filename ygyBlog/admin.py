from django.contrib import admin
from .models import BlogCategory, Blog, BlogComment


# Register your models here.
class BlogCategoryAdmin(admin.ModelAdmin):
    list_display = ['name']


class BlogAdmin(admin.ModelAdmin):
    list_display = ['title', 'content', 'post_date', 'category', 'author']


class BlogCommentAdmin(admin.ModelAdmin):
    list_display = ['content', 'post_date', 'author', 'blog']


admin.site.register(BlogCategory, BlogCategoryAdmin)
admin.site.register(Blog, BlogAdmin)
admin.site.register(BlogComment, BlogCommentAdmin)
