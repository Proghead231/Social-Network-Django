from django.contrib import admin
from .models import Post, Comment

admin.site.register(Post)

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('body', 'post', 'date_posted')
    list_filter = ['date_posted']

    def approve_comments(self, request, queryset):
        queryset.update(active=True)
