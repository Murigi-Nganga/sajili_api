from rest_framework import serializers
from api.models import Book

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['id', 'title', 'description']
        read_only_fields = ['id']      #? incase you want to use the serializer as a mutator