from django import template

from ..models import QuestionAnswer

register = template.Library()


@register.inclusion_tag("templatetags/question-answer.html")
def question_answer() -> dict:
    objects = QuestionAnswer.objects.filter(is_published_landing=True)
    return {
        "objects": objects,
    }
