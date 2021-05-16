from .models import Comment
from django.contrib import admin


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    """
    Новость в админке
    """

    list_display = (
        "name",
        "date_created",
        "is_published_landing",
    )
    list_filter = ("is_published_landing",)
