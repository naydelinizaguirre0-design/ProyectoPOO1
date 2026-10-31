
from rest_framework import status, viewsets
from .serializers import ProductsSerializer 
from .models import Products

class ProductsViewSet(viewsets.ModelViewSet):
    model = Products 
    serializer_class = ProductsSerializer

    def get_queryset(self):
        return Products.objects.all()


