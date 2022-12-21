from rest_framework.routers import DefaultRouter
from django.urls import path, include

from applications.feedback.views import CommentApiView

router = DefaultRouter()
router.register('comment', CommentApiView)

urlpatterns = [
    path('', include(router.urls))
]
