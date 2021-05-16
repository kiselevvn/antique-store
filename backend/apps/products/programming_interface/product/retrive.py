from rest_framework.generics import RetrieveAPIView
from rest_framework.serializers import ModelSerializer
from ...models import Product, Picture


class PicturesSerializer(ModelSerializer):
    class Meta:
        model = Picture
        fields = [
            "image",
        ]


class ProductSerializer(ModelSerializer):
    pictures = PicturesSerializer(many=True, read_only=True)

    class Meta:
        model = Product
        fields = ["id", "name", "price", "pictures", "count"]


class ProductRetriveAPIView(RetrieveAPIView):
    serializer_class = ProductSerializer
    queryset = Product.ready_for_sale.all()
