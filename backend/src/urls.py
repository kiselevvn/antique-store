from django.conf import settings
from django.contrib import admin
from django.views.generic import TemplateView
from django.urls import path, re_path, include
from django.conf.urls.i18n import i18n_patterns
from .views import CartView

urlpatterns = [
    path("admin/", admin.site.urls),
    re_path(r"^ckeditor/", include("ckeditor_uploader.urls")),
    path("cart/", CartView.as_view(), name="cart"),
    path("products/", include("apps.products.urls")),
    path("products/api/", include("apps.products.api")),
    path("orders/api/", include("apps.orders.api")),
    path(
        "", TemplateView.as_view(template_name="landing.html"), name="landing"
    ),
]

urlpatterns = i18n_patterns(
    *urlpatterns,
    prefix_default_language=False,
)


if settings.DEBUG:
    import debug_toolbar

    # pylint: disable=ungrouped-imports
    from django.conf.urls.static import static

    urlpatterns = (
        [
            path("__debug__/", include(debug_toolbar.urls)),
        ]
        + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
        + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
        + urlpatterns
    )
