from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class NotFoundView(APIView):
    def dispatch(self, request, *args, **kwargs):
        print('Dispatch has been called!')
        return Response({'error': 'Not Found'}, status=status.HTTP_404_NOT_FOUND)