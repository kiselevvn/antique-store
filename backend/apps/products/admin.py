from .models import Product, Tag, Category, Picture
from django.contrib import admin


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    """
    Категория
    """

    list_display = ("name",)
    list_filter = ("is_published",)


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    """
    Тег
    """

    list_display = ("name",)


class PictureInline(admin.TabularInline):
    model = Picture


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    """
    Товар
    """

    list_display = (
        "name",
        "date_created",
        "is_published",
    )
    readonly_fields = ["count"]
    list_filter = (
        "is_published",
        "category",
    )
    inlines = (PictureInline,)
