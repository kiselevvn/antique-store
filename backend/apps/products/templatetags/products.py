from django import template

from ..models import Product, Category

register = template.Library()


@register.inclusion_tag("templatetags/products-section.html")
def all_products_section() -> dict:
    objects = Category.objects.prefetch_related("category")

    return {
        "title": "Все товары",
        "objects": objects,
    }


@register.inclusion_tag("templatetags/products-section.html")
def new_products_section() -> dict:
    objects = Product.objects.all()

    return {
        "title": "Последние поступления",
        "objects": objects,
    }


@register.inclusion_tag("templatetags/category-section.html")
def all_category_section() -> dict:
    objects = Category.objects.all()

    return {
        "objects": objects,
    }
