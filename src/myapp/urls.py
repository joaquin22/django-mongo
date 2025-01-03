from django.urls import path, include

from rest_framework.routers import DefaultRouter

from .views import BookAPIView, BookDetailAPIView


router = DefaultRouter()
router.register("books", BookAPIView, basename="books")


urlpatterns = [
    # path("books/", BookAPIView.as_view(), name="books"),
    path("", include(router.urls)),
    path("books/<str:pk>/", BookDetailAPIView.as_view(), name="books-detail"),
]
