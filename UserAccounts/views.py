from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import RegisterSerializer, LoginSerializer,EditSerializer
from rest_framework import status
from .models import CustomUser
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication


# Create your views here.
class RegisterView(APIView):

    def post(self,request):
        try:
            data=request.data
            serializer=RegisterSerializer(data=data)
            if not serializer.is_valid():
                return Response({
                    'data':serializer.errors,
                    'message':'something went wrong'
                }, status=status.HTTP_400_BAD_REQUEST)
            serializer.save()
            return Response({
                    'data':{},
                    'message':'Account created'
                }, status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response({
                    'data':serializer.errors,
                    'message':'something went wrong'
                }, status=status.HTTP_400_BAD_REQUEST)


class LoginView(APIView):
    def post(self,request):
        try:
            data=request.data
            serializer=LoginSerializer(data=data)
            if not serializer.is_valid():
                return Response({
                    'data':serializer.errors,
                    'message':'something went wrong'
                }, status=status.HTTP_400_BAD_REQUEST)
            response=serializer.get_jwt_token(serializer.data)
            return Response(response, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({
                    'data':serializer.errors,
                    'message':'something went wrong'
                }, status=status.HTTP_400_BAD_REQUEST)

            
class EditProfile(APIView):
    # permission_classes=[IsAuthenticated]
    # authentication_classes=[JWTAuthentication]
    def get(self, request):
        try:
            user_details = CustomUser.objects.get(id=request.user.id)
            serializer=EditSerializer(user_details)
            return Response({
                    'data':serializer.data,
                    'message':'User details fetched successfully'
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
            current_user = CustomUser.objects.get(id=request.user.id)
            print(current_user)
            if not current_user:
                return Response({
                    'data':{},
                    'message':'Not a valid user id'
                }, status=status.HTTP_400_BAD_REQUEST)

            if request.user != current_user:
                return Response({
                    'data':{},
                    'message':'You are not authorized'
                }, status=status.HTTP_400_BAD_REQUEST)
            
            serializer = EditSerializer(current_user, data=data, partial=True)


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


