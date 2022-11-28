from posts.models import Post, Group, Comment
from rest_framework import serializers

class PostSerializer(serializers.ModelSerializer):
    group = serializers.SlugRelatedField(required=False, queryset = Group.objects.all(), slug_field='slug')
    image = serializers.ImageField(required=False)
    author =serializers.StringRelatedField(read_only=True)
    pub_date = serializers.DateTimeField(read_only=True)

    class Meta:
        model = Post
        fields=('id', 'author', 'text', 'group', 'image', 'pub_date')

class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields =('id','title', 'slug', 'description')
        read_only_fields = ('id',)

class CommentSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField(read_only = True)
    class Meta:
        model = Comment
        fields = '__all__'


