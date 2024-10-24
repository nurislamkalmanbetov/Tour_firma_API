from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework import status
from drf_yasg.utils import swagger_auto_schema

from .serializers import ToursSerializer 

class TourCreateView(APIView):
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(
        request_body=ToursSerializer,
        responses={201: 'Tour created successfully', 403: 'Forbidden'}
    )
    def post(self, request):
        serializer = ToursSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Tour created successfully"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class TourListView(ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = ToursSerializer

    def get_queryset(self):
        return self.request.user.tours.all()
    

