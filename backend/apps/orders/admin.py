from .models import Order, OrderPosition
from django.contrib import admin


class OrderPositionInline(admin.TabularInline):
    model = OrderPosition


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    """
    Заказ
    """

    list_display = (
        "name",
        "date_created",
    )

    # list_filter = ("is_published",)
    inlines = (OrderPositionInline,)
