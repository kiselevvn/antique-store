from .models import Operation, OperationPosition
from django.contrib import admin


class OperationPositionInline(admin.TabularInline):
    model = OperationPosition


@admin.register(Operation)
class OperationAdmin(admin.ModelAdmin):
    """
    Операция на складе
    """

    list_display = ("date_created", "count", "comment")
    # readonly_fields = ["phone", "address"]
    # list_filter = ("is_published",)
    inlines = (OperationPositionInline,)

    def count(self, obj):
        summ = 0
        for p in obj.positions.all():
            summ += p.count
        if summ > 0:
            return f"Увеличилось (на {summ} едениц)"
        else:
            return f"Уменьшилось (на {summ} едениц)"
