from rest_framework import serializers

from .models import NewsModel


class NewsSerializer(serializers.ModelSerializer):
    """Сериализатор для таблицы News"""
    class Meta:
        model = NewsModel
        fields = '__all__'
        lookup_field = 'slug'
        # extra_kwargs = {
        #     'url': {'lookup_field': 'slug'}
        # }

