# Created by SezerBozkir<admin@sezerbozkir.com> at 10/23/2020
from django.contrib.auth.models import User

from restApi.models import Article
from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['username']


class ArticleSerializer(serializers.HyperlinkedModelSerializer):
    author = UserSerializer()

    class Meta:
        model = Article
        fields = [
            'title',
            'image1_url',
            'description',
            'video_link',
            'content',
            'lang',
            'category',
            'author']
