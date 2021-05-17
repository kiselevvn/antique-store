from django.views.generic import TemplateView


class CartView(TemplateView):
    template_name = "apps/products/local-storage-cart.html"
