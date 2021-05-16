from django.db import models
from django.utils.translation import gettext as _
from apps.services.models import (
    DateCreatedMixin,
    DateUpdatedMixin,
)


class Comment(
    DateCreatedMixin,
    models.Model,
):
    """
    Модель Отзыва
    """

    name = models.CharField(
        verbose_name=_("Имя"),
        max_length=255,
    )
    text = models.TextField(
        verbose_name=_("Отзыв"),
    )
    is_published_landing = models.BooleanField(
        verbose_name=_("Отзыв опубликован"), default=False
    )

    class Meta:
        verbose_name = _("Отзыв")
        verbose_name_plural = _("Отзывы")
        ordering = ["-date_created"]

    def __str__(self):
        return f"{self.name} " + f"(дата создания: {self.date_created}) "
