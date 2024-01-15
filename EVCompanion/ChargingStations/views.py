from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import ChargingStationSerializer
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from django.db.models import Q
from django.core.paginator import Paginator

from UserAccounts.models import CustomUser
from ChargingStations.models import ChargingStation

# Create your views here.
class StationsAddView(APIView):
    permission_classes=[IsAuthenticated]
    authentication_classes=[JWTAuthentication]

    def get(self, request):
        try:
            vehicles=ChargingStation.objects.all().order_by('?')
            page_number=request.GET.get('page',1)
            paginator=Paginator(vehicles,2)
            serializer=ChargingStationSerializer(paginator.page(page_number),many=True)

            return Response({
                    'data':serializer.data,
                    'message':'Charging Staion details fetched successfully'
                }, status=status.HTTP_201_CREATED)
        
        except Exception as e:
            print(e)
            return Response({
                    'data':{},
                    'message':'something went wrong'
                }, status=status.HTTP_400_BAD_REQUEST)
        
    def post(self, request):
        try:
            current_user = CustomUser.objects.get(id=request.user.id)
            print(current_user)
            if not current_user.is_superuser:
                return Response({
                    'message': 'You are not authorized to perform this action'
                }, status=status.HTTP_403_FORBIDDEN)
            data=request.data
            data['user']=request.user.id
            print(request.user)
            serializer=ChargingStationSerializer(data=data)
            if not serializer.is_valid():
                return Response({
                    'data':serializer.errors,
                    'message':'something went wrong'
                }, status=status.HTTP_400_BAD_REQUEST)
            
            serializer.save()

            return Response({
                    'data':serializer.data,
                    'message':'Station added successfully'
                }, status=status.HTTP_201_CREATED)
        except Exception as e:
            print(e)
            return Response({
                    'data':{},
                    'message':'something went wrong'
                }, status=status.HTTP_400_BAD_REQUEST)

    def patch(self,request):
        try:
            data=request.data
            station=ChargingStation.objects.filter(uid=data.get('uid'))
            current_user = CustomUser.objects.get(id=request.user.id)
            if not station.exists():
                return Response({
                    'data':{},
                    'message':'Not a valid station id'
                }, status=status.HTTP_400_BAD_REQUEST)

            if not current_user.is_superuser:
                return Response({
                    'data':{},
                    'message':'You are not authorized'
                }, status=status.HTTP_400_BAD_REQUEST)
            
            serializer=ChargingStationSerializer(station[0],data=data,partial=True)

            if not serializer.is_valid():
                return Response({
                    'data':{},
                    'message':'Something went wrong'
                }, status=status.HTTP_400_BAD_REQUEST)
            
            serializer.save()

            return Response({
                    'data':serializer.data,
                    'message':'Successfully updated'
                }, status=status.HTTP_201_CREATED)
        
        except Exception as e:
            print(e)
            return Response({
                    'data':{},
                    'message':'something went wrong'
                }, status=status.HTTP_400_BAD_REQUEST)
    def delete(self,request):
        try:
            data=request.data
            station=ChargingStation.objects.filter(uid=data.get('uid'))
            current_user = CustomUser.objects.get(id=request.user.id)
            if not station.exists():
                return Response({
                    'data':{},
                    'message':'Not a valid station id'
                }, status=status.HTTP_400_BAD_REQUEST)

            if not current_user.is_superuser:
                return Response({
                    'data':{},
                    'message':'You are not authorized'
                }, status=status.HTTP_400_BAD_REQUEST)
            
            station[0].delete()

            return Response({
                    'data':{},
                    'message':'Successfully deleted'
                }, status=status.HTTP_201_CREATED)
        
        except Exception as e:
            print(e)
            return Response({
                    'data':{},
                    'message':'something went wrong'
                }, status=status.HTTP_400_BAD_REQUEST)


    