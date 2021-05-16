from django import template

from ..models import News

register = template.Library()


@register.inclusion_tag("templatetags/news-landing.html")
def news_cards() -> dict:
    objects = News.objects.filter(is_published=True, is_published_landing=True)

    return {
        "objects": objects,
    }
