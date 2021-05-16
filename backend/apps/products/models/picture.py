from django.db import models
from django.utils.translation import gettext as _
from apps.services.models import DateCreatedMixin, DateUpdatedMixin, OrderMixin


class Picture(OrderMixin, DateCreatedMixin, DateUpdatedMixin, models.Model):
    """
    Изображение товара
    """

    product = models.ForeignKey(
        "products.Product",
        verbose_name=_("Товар"),
        on_delete=models.CASCADE,
        related_name="pictures",
    )
    image = models.ImageField(
        _("Изображение"),
    )
    is_card_size = models.BooleanField(
        verbose_name=_("Изображение карточки товара"),
        default=False,
        blank=True,
        null=True,
    )
    is_published = models.BooleanField(
        verbose_name=_("Изображение опубликовано"),
        default=False,
        blank=True,
        null=True,
    )

    class Meta:
        verbose_name = _("Изображение товара")
        verbose_name_plural = _("Изображения товаров")

    def __str__(self):
        return self.product.name
