from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from account.serailizers import UserRegistratorSerializer,UserLoginSerializer,UserProfileSerializer
from django.contrib.auth import authenticate
from account.renderers import UserRenderer
from rest_framework_simplejwt.tokens import RefreshToken ,AccessToken
from rest_framework.permissions import IsAuthenticated

#generate token manually
def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)
    access = AccessToken.for_user(user)
    return {
        'refresh': str(refresh),
        'access': str(access),
    }


# @api_view(['POST'])
class UserRegistrationView(APIView):
    renderer_classes = [UserRenderer]
    def post(self,request):
        serializer = UserRegistratorSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            user= serializer.save()
            return Response({'messaage':"register successfully registered"},
            status = status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_404_NOT_FOUND)
        
        
class UserLoginView(APIView):
    renderer_classes = [UserRenderer]
    def post(self,request):
        serializer = UserLoginSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            email = serializer.data.get('email')
            password = serializer.data.get('password')
            user = authenticate(email=email, password=password)
            if user is not None:
                token = get_tokens_for_user(user)
                return Response({'token':token, 'messaage':"Login successfully "},status=status.HTTP_200_OK)
            else:
                return Response({'messaage':"Invalid Credentials"},status=status.HTTP_404_NOT_FOUND)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

class UserProfileView(APIView):
    renderer_classes = [UserRenderer]
    permission_classes = [IsAuthenticated]
    def get(self,request,format=None):
        user = request.user
        serializer = UserProfileSerializer(user)
        return Response( serializer.data,status=status.HTTP_200_OK)


        
         