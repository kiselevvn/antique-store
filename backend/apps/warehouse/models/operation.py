from django.db import models
from django.utils.translation import gettext as _
from apps.services.models import (
    DateCreatedMixin,
    DateUpdatedMixin,
)


class Operation(DateUpdatedMixin, DateCreatedMixin, models.Model):
    """
    Операция движения
    товара на складе
    """

    comment = models.TextField(
        verbose_name=_("Описание"), blank=True, null=True
    )

    class Meta:
        verbose_name = _("Операция")
        verbose_name_plural = _("Операции")
        ordering = ["-date_created"]

    # def __str__(self):
    #     return f"{self.name} - {self.email} на сумму {self.price}"
