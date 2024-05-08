from django.urls import path
from rest_framework.routers import DefaultRouter

from apps.users.views import UserAPI, HistoryTransferAPI

router = DefaultRouter()
router.register('users', UserAPI, basename='api_user'),
router.register('historytrans/', HistoryTransferAPI, basename='historytrans')

urlpatterns = router.urls

