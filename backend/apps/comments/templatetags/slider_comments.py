from django import template

from ..models import Comment

register = template.Library()


@register.inclusion_tag("templatetags/comments-landing.html")
def slider_comments() -> dict:
    objects = Comment.objects.filter(is_published_landing=True)

    return {
        "objects": objects,
    }
