from django.urls import path
from UserAccounts.views import RegisterView, LoginView, EditProfile
from VehicleInfo.views import VehiclesAddView
from ChargingStations.views import StationsAddView
from PaymentIntegration.views import RazorpayOrderAPIView, TransactionAPIView

urlpatterns = [
    path('register/', RegisterView.as_view()),
    path('login/', LoginView.as_view()),
    path('edit/', EditProfile.as_view()),
    path('addVehicle/', VehiclesAddView.as_view()),
    path('addStations/', StationsAddView.as_view()),
    path('createOrder/', RazorpayOrderAPIView.as_view()),
    path('completeOrder/', TransactionAPIView.as_view()),



]