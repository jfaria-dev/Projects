from _panel.models import Service, GeneralService
from _api.serializers import ServiceSerializer, GeneralServiceSerializer

from rest_framework.response import Response
from rest_framework.decorators import api_view

@api_view(['POST'])
def logout(request):
    if request.user.is_authenticated:
        request.user.auth_token.delete()
    return Response(status=200)