from api.models import Book
from api.serializers import BookSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(['GET'])
def book_list(request):
    books = Book.objects.all()
    serializer = BookSerializer(books, many=True)
    return Response(serializer.data, safe=False)