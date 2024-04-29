from django.contrib import admin
from .models import Author, Book, User, BlogUser, Blog, Comment


class ChoiceInline(admin.StackedInline):
    model = Comment
    extra = 0


class BlogAdmin(admin.ModelAdmin):
    fields = ['article_name', 'article_body', 'blog_user', 'date_of_publicity']
    list_display = ('article_name', 'blog_user', 'date_of_publicity')
    list_filter = ['date_of_publicity']
    search_fields = ['article_name']
    inlines = [ChoiceInline]


class BlogUserAdmin(admin.ModelAdmin):
    search_fields = ['blog_user_name', 'email']


admin.site.register(BlogUser, BlogUserAdmin)
admin.site.register(Blog, BlogAdmin)
