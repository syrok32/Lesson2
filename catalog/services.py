from catalog.models import Product, Category


class ProductServices:
    @staticmethod
    def get_products(category_id=None):
        products = Product.objects.all()

        # Фильтрация по категории
        if category_id:
            products = products.filter(category_id=category_id)
        return category_id




