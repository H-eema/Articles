from rest_framework import generics, permissions
from django.contrib.auth import get_user_model

from .serializers import UserArticleSerializer, UserSerializer
from .permissions import IsAdminOrUserSelf


class UserDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = get_user_model().objects.all()
    permission_classes = [IsAdminOrUserSelf]
    serializer_class = UserSerializer


class UserArticleView(generics.RetrieveAPIView):
    permission_classes = [
        IsAdminOrUserSelf,
    ]
    queryset = get_user_model().objects.all()
    serializer_class = UserArticleSerializer
