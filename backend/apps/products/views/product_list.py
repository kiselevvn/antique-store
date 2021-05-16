from django.views.generic import ListView
from ..models import Product, Category


class ProductList(ListView):
    """
    Список товаров
    """

    model = Product
    paginate_by = 9
    template_name = "apps/products/product-list.html"

    def get_queryset(self):
        products = self.model.ready_for_sale.all()
        category = self.request.GET.get("category")
        tag = self.request.GET.get("tag")
        if category is not None:
            products = products.filter(category_id=category)
        if tag is not None:
            products = products.filter(group_tags__tag_id=tag)
        # print(len(products))
        return products

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["categories"] = Category.objects.filter(is_published=True)
        return context
