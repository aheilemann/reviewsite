from rest_framework import serializers
from rest_framework.settings import api_settings
from .models import Review, Category
from ..users.models import User


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = [
            "id",
            "created",
            "modified",
            "title",
            "description",
            "hotscore",
            "author",
            "author_url",
            "url",
            "category",
            "vote_score",
        ]

    created = serializers.DateTimeField()
    url = serializers.URLField(source="get_complete_url", read_only=True)
    category = serializers.StringRelatedField()
    author = serializers.StringRelatedField(source='get_author_name')  # author.name returns blank if no name
    author_url = serializers.URLField(source="get_author_url", read_only=True)
    hotscore = serializers.FloatField(read_only=True)

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = [
            "name",
            "reviews",
        ]
        depth = 1

    name = serializers.CharField(max_length=100, required=True)
    reviews = serializers.StringRelatedField(many=True, read_only=True)

class UserSerializer(serializers.Serializer):
    class Meta:
        model = User
        fields = [
            "id",
            "username",
            "name",
            "user_url",
        ]

    id = serializers.IntegerField()
    username = serializers.CharField()
    name = serializers.CharField()
    user_url = serializers.URLField(source="get_absolute_url")


class GetFullUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'is_superuser', 'first_name', 'last_name')


class UserSerializerWithToken(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    token = serializers.SerializerMethodField()
    def get_token(self, obj):
        jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
        jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER
        payload = jwt_payload_handler(obj)
        token = jwt_encode_handler(payload)
        return token
    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data['username'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user

    class Meta:
        model = User
        fields = ('token', 'username', 'password', 'first_name', 'last_name')
