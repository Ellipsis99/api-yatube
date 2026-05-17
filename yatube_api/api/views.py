from rest_framework import viewsets
from rest_framework import generics
import datetime as dt

from posts.models import Post, User

from .serializers import PostSerializer, UserSerializer


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


#ListApiView для Group -> GroupList