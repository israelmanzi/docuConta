from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework_simplejwt.tokens import RefreshToken
from .models import User
from .serializers import UserSerializer
from django.contrib.auth.hashers import make_password, check_password


@api_view(['POST'])
def register(request) -> Response:
    serializer = UserSerializer(data=request.data)

    password = make_password(request.data.get('password'))

    serializer.initial_data['password'] = password

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def login(request) -> Response:
    email = request.data.get('email')
    password = request.data.get('password')

    user = User.objects.filter(email=email).first()

    if check_password(password, user.password) is False or user is None:
        return Response({'error': 'Invalid data'})
    else:
        refresh = RefreshToken.for_user(user)

        user.refresh_token = str(refresh)
        user.save()

        return Response({
            'access': str(refresh.access_token),
            'refresh': str(refresh)
        })


@api_view(['POST'])
def refresh_token(request):
    refresh_token = request.data.get('refresh_token')

    try:
        refresh = RefreshToken(refresh_token)
        access_token = refresh.access_token

        return Response({'access_token': str(access_token)}, status=status.HTTP_200_OK)

    except Exception as e:
        return Response({'detail': 'Invalid refresh token'}, status=status.HTTP_401_UNAUTHORIZED)
