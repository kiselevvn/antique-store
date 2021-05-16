from django.db import models
from django.utils.translation import gettext as _
from apps.services.models import (
    DateCreatedMixin,
    DateUpdatedMixin,
)


class Order(DateUpdatedMixin, DateCreatedMixin, models.Model):
    """
    Заказ
    """

    name = models.CharField(verbose_name=_("Имя"), max_length=255)
    email = models.EmailField(
        verbose_name=_("Электронная почта"), max_length=255
    )
    phone = models.CharField(verbose_name=_("Телефон"), max_length=25)
    address = models.CharField(
        verbose_name=_("Адрес доставки"), max_length=500, blank=True, null=True
    )
    comment = models.TextField(
        verbose_name=_("Описание"), blank=True, null=True
    )

    @property
    def price(self):
        """
        Сумма заказа
        """
        price = 0
        # TODO: Сервис подсчета суммы заказа
        return price

    class Meta:
        verbose_name = _("Заказ")
        verbose_name_plural = _("Заказы")
        ordering = ["-date_created"]

    def __str__(self):
        return f"{self.name} - {self.email} на сумму {self.price}"
