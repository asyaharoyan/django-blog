from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Post, Comment


@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):
    """
    Lists fields for display admin, fileds for search,
    field filters, field to populate and text editor
    """

    list_display = ('title', 'slug', 'status', 'created_on')
    search_fields = ['title', 'content']
    list_filter = ('status', 'created_on', 'author',)
    prepopulated_fields = {'slug': ('title',)}
    summernote_fileds = ('content',)


# Register your models here.
admin.site.register(Comment)
