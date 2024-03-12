from _panel.models import Service, GeneralService
from _web.models import User
from _auth.models import UserAuth

from _api.serializers import ServiceSerializer, GeneralServiceSerializer, UserAuthSerializer

from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.authentication import TokenAuthentication, SessionAuthentication
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404

@api_view(['POST'])
def login(request):
    user_auth = get_object_or_404(UserAuth, email=request.data.get('email'))
    if not user_auth.check_password(request.data.get('password')):
        return Response({'error': 'Invalid password'}, status=400)
    token, created = Token.objects.get_or_create(user=user_auth)
    return Response({'token': token.key, 'auth_user': UserAuthSerializer(user_auth).data}, status=200)
    
    
@api_view(['POST'])
def signup(request):
    data = {
        'email': request.data.get('email'),
        'password': request.data.get('password'),
        'name': request.data.get('name'),
        'phone': request.data.get('phone'),
        'is_client': True
    }  

    for k, v in data.items():
        if v == None:
            return Response({'error': f'Parameter {k.upper()} is required.'}, status=status.HTTP_400_BAD_REQUEST)        

    if request.method == 'POST':
        serializer = UserAuthSerializer(data=data)
        if serializer.is_valid():
            try:
                user_auth = serializer.save()
                user_auth.set_password(data['password'])
                user_auth.save()   
                         
                user = User(user_auth=user_auth, name=data['name'], phone=data['phone'])
                user.save()
                
                token = Token.objects.create(user=user_auth)
                return Response({'token': token.key, 'user': serializer.data}, status=status.HTTP_201_CREATED)
            except Exception as e:
                print('Erro ao inserir usuário:', e)           
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    return Response(status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
@authentication_classes([SessionAuthentication, TokenAuthentication])
@permission_classes([IsAuthenticated])
def logout(request):
    if request.method == 'POST':
        request.user.auth_token.delete()
    return Response({'message': 'You are logged out!'}, status=200)

@api_view(['GET'])
@authentication_classes([SessionAuthentication, TokenAuthentication])
@permission_classes([IsAuthenticated])
def test_auth(request):
    return Response({'message': 'Authenticated'}, status=200)