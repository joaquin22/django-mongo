from rest_framework import serializers


class BookSerializer(serializers.Serializer):
    _id = serializers.CharField(read_only=True)
    title = serializers.CharField()
    author = serializers.CharField()
    published_date = serializers.DateTimeField()
    genre = serializers.CharField()
    price = serializers.FloatField()

    def create(self, validated_data):
        from .models import Book

        book = Book(**validated_data)
        book.save()
        return book

    def update(self, instance, validated_data):
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()
        return instance
