from rest_framework import serializers


class BookSerializer(serializers.Serializer):
    _id = serializers.CharField(read_only=True)
    title = serializers.CharField()
    author = serializers.CharField()
    published_date = serializers.DateTimeField()
    genre = serializers.CharField()
    price = serializers.FloatField()
    year = serializers.IntegerField(read_only=True)

    def create(self, validated_data):
        from .models import Book

        year = validated_data["published_date"].year
        print(year)
        book = Book(**validated_data, year=year)
        book.save()
        return book

    def update(self, instance, validated_data):
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()
        return instance
