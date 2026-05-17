from rest_framework import serializers

import datetime as dt

from posts.models import Post, Comment, Group, User



class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('username',)


class PostSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Post
        fields = ('id', 'text', 'author', 'image', 'group', 'pub_date')


class GroupSerializer(serializers.ModelSerializer):

    class Meta:
        model = Group
        fields = ('id', 'title', 'slug', 'description', 'posts')
