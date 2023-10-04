from rest_framework import serializers
from django.contrib.auth import get_user_model

from articles.serializers import ArticleSerializer


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = (
            "username",
            "email",
            "city",
        )


class UserArticleSerializer(serializers.ModelSerializer):
    articles = ArticleSerializer(many=True)

    class Meta:
        model = get_user_model()
        fields = (
            "id",
            "username",
            "email",
            "city",
            "articles",
        )
