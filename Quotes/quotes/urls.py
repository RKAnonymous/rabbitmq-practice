from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import UserAPIView, QuoteViewset, UserDetailAPIView


router = DefaultRouter()
router.register("quotes", QuoteViewset, basename="quotes")


urlpatterns = [
    path("", include(router.urls)),
    path("users", UserAPIView.as_view(), name="users"),
    path("users/<int:pk>/", UserDetailAPIView.as_view(), name="user-details"),
]
