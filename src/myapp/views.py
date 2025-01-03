from bson.objectid import ObjectId

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import Book
from .serializers import BookSerializer


class BookAPIView(APIView):

    def get(self, request):
        books = Book.find()
        serializer = BookSerializer(books, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = BookSerializer(data=request.data)
        if serializer.is_valid():
            book = serializer.save()
            return Response({"id": str(book._id)}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class BookDetailAPIView(APIView):
    def get_object(self, pk):
        book = Book.find_one({"_id": ObjectId(pk)})
        if not book:
            return None
        return book

    def get(self, request, pk):
        book = self.get_object(pk)
        if not book:
            return Response(
                {"error": "Book not found"}, status=status.HTTP_404_NOT_FOUND
            )
        serializer = BookSerializer(book)
        return Response(serializer.data)

    def put(self, request, pk):
        book = self.get_object(pk)
        if not book:
            return Response(
                {"error": "Book not found"}, status=status.HTTP_404_NOT_FOUND
            )
        serializer = BookSerializer(book, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk):
        book = self.get_object(pk)
        if not book:
            return Response(
                {"error": "Book not found"}, status=status.HTTP_404_NOT_FOUND
            )
        serializer = BookSerializer(book, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        book = self.get_object(pk)
        if not book:
            return Response(
                {"error": "Book not found"}, status=status.HTTP_404_NOT_FOUND
            )
        book.delete()
        return Response(
            {"message": "Book deleted successfully"}, status=status.HTTP_204_NO_CONTENT
        )
