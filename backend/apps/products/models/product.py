from django.db import models
from django.utils.translation import gettext as _
from apps.services.models import (
    DateCreatedMixin,
    DateUpdatedMixin,
)


class ReadyForSale(models.Manager):
    """
    Готовые к продаже Товары
    """

    def get_queryset(self):
        return (
            super()
            .get_queryset()
            .filter(price__isnull=False, is_published=True)
        )


class Product(DateUpdatedMixin, DateCreatedMixin, models.Model):
    """
    Товар
    """

    name = models.CharField(verbose_name=_("Наименование"), max_length=500)
    price = models.DecimalField(
        verbose_name=_("Цена"),
        max_digits=10,
        decimal_places=2,
    )
    short_description = models.TextField(
        verbose_name=_("Краткое описание"), blank=True, null=True
    )
    description = models.TextField(
        verbose_name=_("Описание"), blank=True, null=True
    )
    tags = models.ManyToManyField(
        "products.Tag",
        verbose_name=_("Теги"),
        blank=True,
        null=True,
    )
    category = models.ForeignKey(
        "products.Category",
        verbose_name=_("Категория"),
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name="products",
    )
    is_published = models.BooleanField(
        verbose_name=_("Товар опубликован"), default=False
    )
    count = models.IntegerField(_("Количство товара"), default=0)

    def pictures_card(self):
        return self.pictures.first(is_card_size=True, is_published=True)[:1]

    ready_for_sale = ReadyForSale()
    objects = models.Manager()

    class Meta:
        verbose_name = _("Товар")
        verbose_name_plural = _("Товары")

    def __str__(self):
        return self.name
