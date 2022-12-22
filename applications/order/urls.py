from django.urls import path, include
from rest_framework.routers import DefaultRouter

from applications.order.views import OrderApiView, OrderConfirmApiView 

router = DefaultRouter()
router.register('', OrderApiView)

urlpatterns = [
    path("confirm/<uuid:code>/", OrderConfirmApiView.as_view()),
    path('', include(router.urls))
]
