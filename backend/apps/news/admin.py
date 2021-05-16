from .models import News, QuestionAnswer
from django.contrib import admin


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    """
    Новость в админке
    """

    list_display = (
        "title",
        "date_updated",
        "date_created",
        "is_published",
        "is_published_landing",
    )
    list_filter = (
        "is_published",
        "is_published_landing",
    )


@admin.register(QuestionAnswer)
class QuestionAnswerAdmin(admin.ModelAdmin):
    """
    Вопрос ответ в админке
    """

    list_display = (
        "question",
        "date_updated",
        "date_created",
    )
    list_filter = ("date_created",)
