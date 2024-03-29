from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Mobile
from .serializers import MobileSerializer
from django.shortcuts import get_object_or_404

class MobileAPI(APIView):
    def get(self, request, pk=None):
        if pk != None:
            mobile = get_object_or_404(Mobile, pk=pk)
            serializer = MobileSerializer(mobile)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            queryset = Mobile.objects.all()
            serializer = MobileSerializer(queryset, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)


    def post(self, request):
        serializer = MobileSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def put(self, request, pk=None):
        mobile = get_object_or_404(Mobile, pk=pk)
        serializer = MobileSerializer(mobile, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def patch(self, request, pk=None):
        mobile = get_object_or_404(Mobile, pk=pk)
        serializer = MobileSerializer(mobile, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk=None):
        mobile = get_object_or_404(Mobile, pk=pk)
        mobile.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
