from rest_framework import serializers
from posts.models import Post, Group, Comment


class GroupSerializers(serializers.ModelSerializer):
    class Meta:
        fields = ('id', 'title', 'slug', 'description')
        model = Group


class PostSerializers(serializers.ModelSerializer):
    author = serializers.PrimaryKeyRelatedField(
        read_only=True,
        default=serializers.CurrentUserDefault()
    )

    class Meta:
        fields = ('id', 'text', 'author', 'image', 'group', 'pub_date')
        model = Post


class CommentSerializers(serializers.ModelSerializer):
    author = serializers.StringRelatedField(read_only=True)

    class Meta:
        fields = ('id', 'author', 'post', 'text', 'text', 'created')
        model = Comment
        read_only_fields = ('post',)
