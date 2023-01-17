from django.db import IntegrityError
from rest_framework import serializers
from rest_framework.generics import get_object_or_404

from .models import News, Comment, Status, NewsStatus, CommentStatus


class NewsAPISerializer(serializers.ModelSerializer):
    statuses = serializers.ReadOnlyField(source='get_status')

    class Meta:
        model = News
        fields = '__all__'
        read_only_fields = ['author', ]


class CommentApiSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'
        read_only_fields = ['author', 'news']


class StatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Status
        fields = '__all__'


class NewsStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewsStatus
        fields = ['status']

    def create(self, validated_data):
        status_type = validated_data['status']
        validated_data.pop('status')
        validated_data['status'] = status_type
        try:
            instance = super().create(validated_data)
        except IntegrityError:
            status_tweet = NewsStatus.objects.filter(**validated_data).first()
            if status_tweet:
                status_tweet.delete()
                raise serializers.ValidationError('У данного поста есть статус, текущий статус удален!')
            else:
                status_type = validated_data.pop('status')
                status_tweet = NewsStatus.objects.get(**validated_data)
                status_tweet.status = status_type
                status_tweet.save()
                instance = status_tweet
        return instance
