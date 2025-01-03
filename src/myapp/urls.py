from django.urls import path
from .views import BookAPIView, BookDetailAPIView

urlpatterns = [
    path("books/", BookAPIView.as_view(), name="books"),
    path("books/<str:pk>/", BookDetailAPIView.as_view(), name="books-detail"),
]
