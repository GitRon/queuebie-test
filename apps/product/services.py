from django.db.models import QuerySet, Sum

from apps.product.models import Product


class ProductPricingService:
    def process(self, *, products: QuerySet[Product]) -> int:
        return products.aggregate(total=Sum("price"))["total"]
