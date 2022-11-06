from rest_framework import serializers


# TODO Сериалайзеры. Предлагаем Вам такую структуру, однако вы вправе использовать свою
from ads.models import Comment, Ad
from users.models import User


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['pk', 'text', 'author_id', 'created_at', 'ad_id', 'author_id']


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'first_name', 'last_name', 'phone']


class AdDetailSerializer(serializers.ModelSerializer):
    author_id = serializers.IntegerField(source='author.id')
    author_first_name = serializers.CharField(source='author.first_name')
    author_last_name = serializers.CharField(source='author.last_name')

    class Meta:
        model = Ad
        fields = ['pk', 'image', 'title', 'price', 'description', 'author_first_name', 'author_last_name', 'author_id']


class AdListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ad
        fields = ['pk', 'image', 'title', 'price', 'description']


class AdCreateSerializer(serializers.ModelSerializer):
    author_id = serializers.IntegerField(source='author.id', default='1')
    author_first_name = serializers.CharField(source='author.first_name', default='V')
    author_last_name = serializers.CharField(source='author.last_name', default='V')
    phone = serializers.CharField(source='author.phone', default='123')

    class Meta:
        model = Ad
        fields = ['pk', 'image', 'title', 'price', 'phone', 'description', 'author_first_name', 'author_last_name', 'author_id']


class CommentAdSerializer(serializers.ModelSerializer):
    author_id = serializers.IntegerField(source='author.id', default=1)
    author_image = serializers.ImageField(source='author.image', default='')
    author_first_name = serializers.CharField(source='author.first_name', default='')
    author_last_name = serializers.CharField(source='author.last_name',default='')
    ad_id = serializers.IntegerField(source='ad.id', default=1)

    class Meta:
        model = Comment
        fields = ['pk', 'text', 'author_id', 'created_at', 'author_first_name', 'author_last_name', 'ad_id', 'author_image']
