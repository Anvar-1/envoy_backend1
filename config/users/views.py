from logging import exception

from rest_framework.decorators import api_view
from rest_framework.views import APIView
from .models import User, Image
from rest_framework.response import Response
from .serializers import UserSerializer
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.exceptions import InvalidToken, TokenError
from django.contrib.auth import authenticate
from rest_framework.decorators import authentication_classes, permission_classes
from rest_framework.authentication import TokenAuthentication, SessionAuthentication
from rest_framework.permissions import IsAuthenticated
from .serializers import UserUpdateSerializer
from rest_framework import generics
from .serializers import ImageSerializer
from .models import UserProfile
from .serializers import UserProfileSerializer
from rest_framework.parsers import MultiPartParser, FormParser
from .serializers import UserRegistrationSerializer, UserLoginSerializer


@api_view(["POST"])
def signup(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()

        username = User.objects.get(username=request.data['username'])
        token = Token.objects.get(user=username)

        serializer = UserSerializer(username)

        data = {
            "username": serializer.data,
            "token": token.key
        }

        return Response(data, status=status.HTTP_201_CREATED)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["POST"])
def login(request):
    data = request.data
    authenticate_user = authenticate(username=data['username'], password=data['password'])

    if authenticate_user is not None:
        user = User.objects.get(username=data['username'])
        serializer = UserSerializer(user)

        response_data = {
            'username': serializer.data,
        }

        token, created_token = Token.objects.get_or_create(user=user)

        if token:
            response_data['token'] = token.key
        elif created_token:
            response_data['token'] = created_token.key

        return Response(response_data)
    return Response({"detail": "not found"}, status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET"])
@authentication_classes([SessionAuthentication, TokenAuthentication])
@permission_classes([IsAuthenticated])
def TestView(request):
    return Response({"message": "Test view page"})

@api_view(["GET"])
@authentication_classes([SessionAuthentication, TokenAuthentication])
@permission_classes([IsAuthenticated])
def logout(request):
    request.user.auth_token.delete()
    request.session.flush()

    return Response({"message": "logout was successful"})

@api_view(['PATCH'])
def update_user(request, pk):
    try:
        user = User.objects.get(pk=pk)
    except User.DoesNotExist:
        return Response({'detail': "Invalid username or password" }, status=status.HTTP_404_NOT_FOUND)

    serializer = UserUpdateSerializer(user, data=request.data, partial=True)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UserUpdateView(generics.UpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserUpdateSerializer

class UserProfileView(generics.RetrieveUpdateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = UserProfileSerializer

    def get_object(self):
        return self.request.user.profile

class UserRegisterView(generics.CreateAPIView):
    serializer_class = UserRegistrationSerializer

class UserLoginView(APIView):
    def post(self, request):
        serializer = UserLoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = User.objects.get(username=serializer.validated_data['username'])
        token, created = Token.objects.get_or_create(user=user)

        response_data = {
            'token': token.key,
        }
        return Response(response_data)


@api_view(['GET'])
def check_token(request):
    auth_header = request.headers.get('Authorization')

    if auth_header:
        parts = auth_header.split()

        if len(parts) == 2 and parts[0] == 'Bearer':
            token = parts[1]
            try:
                jwt_auth = JWTAuthentication()
                validated_token = jwt_auth.get_validated_token(token)
                user = jwt_auth.get_user(validated_token)
                return Response({'user_id': user.id, 'username': user.username})
            except Exception as e:
                return Response({'error': str(e)}, status=401)
        else:
            return Response({'error': 'Invalid token format'}, status=400)
    return Response({'error': 'Token required'}, status=400)

class ImageUploadView(APIView):
    parser_classes = (MultiPartParser, FormParser)

    def post(self, request, *args, **kwargs):
        image_serializer = ImageSerializer(data=request.data)
        if image_serializer.is_valid(raise_exception=True):
            image_serializer.save()
            return Response(image_serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(image_serializer.errors, status=status.HTTP_400_BAD_REQUEST)







