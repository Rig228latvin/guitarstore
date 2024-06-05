# shop/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserViewSet, OrderViewSet, GuitarViewSet, GuitarCategoryViewSet, ShoppingCartViewSet

router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'orders', OrderViewSet)
router.register(r'guitars', GuitarViewSet)
router.register(r'categories', GuitarCategoryViewSet)
router.register(r'carts', ShoppingCartViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
