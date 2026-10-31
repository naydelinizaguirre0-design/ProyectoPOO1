from django.urls import path, include
from rest_framework import routers 

from .views import (
    ProductsViewSet,
  
)

router = routers.DefaultRouter()
router.register(r"products", ProductsViewSet, "products")  

urlpatterns = [
    path("", include(router.urls)),
]