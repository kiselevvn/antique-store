from django.views.generic import DetailView
from ..models import Product


class ProductDetail(DetailView):
    model = Product
    template_name = "apps/products/product-detail.html"
