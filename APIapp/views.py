from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny
from django.shortcuts import get_object_or_404
from django.db import DatabaseError
from .models import ServerInfo
from .serializers import ServerInfoSerializer

class ServerInfoAPIView(APIView):
    permission_classes = [AllowAny]

    def get(self, request, pk=None):
        try:
            if pk:
                serverinfo = get_object_or_404(ServerInfo, pk=pk)
                serializer = ServerInfoSerializer(serverinfo)
                return Response(serializer.data, status=status.HTTP_200_OK)
            else:
                queryset = ServerInfo.objects.all()
                serializer = ServerInfoSerializer(queryset, many=True)
                return Response(serializer.data, status=status.HTTP_200_OK)
        except ServerInfo.DoesNotExist:
            return Response({'error': 'Server record not found'}, status=status.HTTP_404_NOT_FOUND)
        except DatabaseError as e:
            return Response({'error': 'Database error occurred', 'details': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)



    def post(self, request):
        serializer = ServerInfoSerializer(data=request.data)
        try:
            if serializer.is_valid():
                serializer.save()
                return Response({'success': 'Server record added successfully','data': serializer.data }, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except DatabaseError as e:
            return Response({'error': 'Database error occurred','details': str(e) }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def put(self, request, pk=None):
        try:
            serverinfo = get_object_or_404(ServerInfo, pk=pk)
            serializer = ServerInfoSerializer(serverinfo, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({'sucess': 'Server record update succesfully','data':serializer.data,}, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except ServerInfo.DoesNotExist:
            return Response({'error': 'Server record not found'}, status=status.HTTP_404_NOT_FOUND)
        except DatabaseError as e:
            return Response({'error': 'Database error occurred', 'details': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def delete(self, request, pk=None):
        try:
            serverinfo = get_object_or_404(ServerInfo, pk=pk)
            serverinfo.delete() 
            return Response({'sucess': 'Server record delete succesfully'},status=status.HTTP_204_NO_CONTENT)
        except ServerInfo.DoesNotExist:
            return Response({'error': 'Server record not found'}, status=status.HTTP_404_NOT_FOUND)
        except DatabaseError as e:
            return Response({'error': 'Database error occurred', 'details': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)



