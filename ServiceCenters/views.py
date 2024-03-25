from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import ServiceCenterSerializer
from rest_framework import status
from django.http import Http404
from django.core.paginator import Paginator
from rest_framework.permissions import IsAdminUser
from .models import DeliveryBoy, ServiceCenter, Service
from .serializers import DeliveryBoySerializer, ServiceSerializer

from django.contrib.auth import get_user_model

User = get_user_model()

class CenterAddView(APIView):

    def get(self, request):
        try:
            centers = ServiceCenter.objects.all().order_by('?')
            page_number = request.GET.get('page', 1)
            paginator = Paginator(centers, 2)  # Customize the paginate_by value as needed
            serializer = ServiceCenterSerializer(paginator.page(page_number), many=True)

            return Response({
                'data': serializer.data,
                'message': 'Service Center details fetched successfully'
            }, status=status.HTTP_200_OK)
        
        except Exception as e:
            return Response({
                'data': {},
                'message': 'Something went wrong: ' + str(e)
            }, status=status.HTTP_400_BAD_REQUEST)
        
    def post(self, request):
        try:
            if not request.user.is_superuser:
                return Response({
                    'message': 'You are not authorized to perform this action'
                }, status=status.HTTP_403_FORBIDDEN)

            data = request.data
            serializer = ServiceCenterSerializer(data=data)
            if not serializer.is_valid():
                return Response({
                    'data': serializer.errors,
                    'message': 'Something went wrong'
                }, status=status.HTTP_400_BAD_REQUEST)
            
            serializer.save()
            return Response({
                'data': serializer.data,
                'message': 'Service Center added successfully'
            }, status=status.HTTP_201_CREATED)
        
        except Exception as e:
            return Response({
                'data': {},
                'message': 'Something went wrong: ' + str(e)
            }, status=status.HTTP_400_BAD_REQUEST)


class ServiceList(APIView):
    def get(self, request):
        services = Service.objects.all()
        serializer = ServiceSerializer(services, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ServiceSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ServiceDetail(APIView):
    def get_object(self, pk):
        try:
            return Service.objects.get(pk=pk)
        except Service.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        service = self.get_object(pk)
        serializer = ServiceSerializer(service)
        return Response(serializer.data)

    def put(self, request, pk):
        service = self.get_object(pk)
        serializer = ServiceSerializer(service, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        service = self.get_object(pk)
        service.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class DeliveryAddView(APIView):
    permission_classes = [IsAdminUser]

    def get(self, request):
        delivery_boys = DeliveryBoy.objects.all()
        serializer = DeliveryBoySerializer(delivery_boys, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = DeliveryBoySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class DeliveryView(APIView):
    permission_classes = [IsAdminUser]

    def get_object(self, pk):
        try:
            return DeliveryBoy.objects.get(pk=pk)
        except DeliveryBoy.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        delivery_boy = self.get_object(pk)
        serializer = DeliveryBoySerializer(delivery_boy)
        return Response(serializer.data)

    def put(self, request, pk):
        delivery_boy = self.get_object(pk)
        serializer = DeliveryBoySerializer(delivery_boy, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        delivery_boy = self.get_object(pk)
        delivery_boy.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)