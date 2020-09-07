from rest_framework import serializers
from .models import Review, Category


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = [
            "created",
            "modified",
            "title",
            "description",
            "hotscore",
            "author",
            "author_url",
            "url",
            "category",
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
