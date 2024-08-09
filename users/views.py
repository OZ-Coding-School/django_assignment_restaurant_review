from rest_framework.views import APIView
from users.serializers import UserDetailSerializer, UserLoginSerializer
from rest_framework import status
from rest_framework.generics import RetrieveUpdateDestroyAPIView, CreateAPIView, get_object_or_404
from rest_framework.response import Response
from django.contrib.auth import login, get_user_model
from rest_framework.permissions import AllowAny

User = get_user_model()


class UserSignupView(CreateAPIView):
    serializer_class = UserDetailSerializer
    permission_classes = [AllowAny]


class UserLoginView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = UserLoginSerializer(data=request.data)
        if serializer.is_valid():
            login(request, serializer.validated_data.get('user'))
            return Response({'message': 'login successful.'}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserDetailView(RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserDetailSerializer

    def get_object(self):
        # 현재 로그인한 사용자만 자신의 정보를 조회, 수정, 삭제할 수 있도록 설정
        return get_object_or_404(User, id=self.request.user.id)
