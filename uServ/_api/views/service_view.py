from _panel.models import Service
from ..serializers.services_serializer import ServiceSerializer

from rest_framework import generics

class ServiceListAPIView(generics.ListAPIView):
    queryset = Service.objects.filter(active=True)
    serializer_class = ServiceSerializer
    
service_list_view = ServiceListAPIView.as_view()

class ServiceDetailAPIView(generics.RetrieveAPIView):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer

service_detail_view = ServiceDetailAPIView.as_view()