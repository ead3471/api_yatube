from django.shortcuts import render
from posts.models import Post, Group, Comment
from rest_framework import viewsets
from .serializers import PostSerializer, GroupSerializer, CommentSerializer
from django.core.exceptions import PermissionDenied

# Create your views here.
class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    def perform_destroy(self, post_object: Post):
        if self.request.user != post_object.author:
            raise PermissionDenied('Изменение чужого контента запрещено!')
        super(PostViewSet, self).perform_destroy(post_object)
    
    def perform_update(self, serializer: PostSerializer):
        #print(serializer.instance)
        if self.request.user != serializer.instance.author:
            raise PermissionDenied('Изменение чужого контента запрещено!')
        super(PostViewSet, self).perform_update(serializer)

class GroupViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Group.objects.all()
    serializer_class =GroupSerializer

class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    def get_queryset(self):
        post_id = self.kwargs['post_id']
        return Comment.objects.filter(post=post_id).all()

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    def perform_destroy(self, comment_object: Comment):
        if self.request.user != comment_object.author:
            raise PermissionDenied('Изменение чужого контента запрещено!')
        super(CommentViewSet, self).perform_destroy(comment_object)
    
    def perform_update(self, serializer: CommentSerializer):
        if self.request.user != serializer.instance.author:
            raise PermissionDenied('Изменение чужого контента запрещено!')
        super(CommentViewSet, self).perform_update(serializer)