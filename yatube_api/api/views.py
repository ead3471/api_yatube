from posts.models import Post, Group, Comment
from rest_framework import viewsets
from .serializers import PostSerializer, GroupSerializer, CommentSerializer
from django.core.exceptions import PermissionDenied
from django.contrib.auth.models import AnonymousUser
from rest_framework.permissions import BasePermission, IsAuthenticated


class IsOwnerOrReadOnly(BasePermission):
    message = "Изменение чужого контента запрещено!"
    def has_object_permission(self, request, view:viewsets.ModelViewSet, obj):
        return obj.author == request.user

class PostViewSet(viewsets.ModelViewSet):
    permission_classes = [IsOwnerOrReadOnly, IsAuthenticated]
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

class GroupViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Group.objects.all()
    serializer_class =GroupSerializer

class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]

    def get_queryset(self):
        post_id = self.kwargs['post_id']
        return Comment.objects.filter(post=post_id).all()

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)