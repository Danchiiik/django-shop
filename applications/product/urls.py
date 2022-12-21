from rest_framework.routers import DefaultRouter
from django.urls import path, include

from applications.product.views import CategoryApiView, ProductApiView

router = DefaultRouter()
router.register('category', CategoryApiView)
router.register('', ProductApiView)



urlpatterns = [
    path('', include(router.urls))
]
