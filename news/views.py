from django.shortcuts import render
from rest_framework import generics, viewsets

from .models import News, Comment, Status, NewsStatus, CommentStatus
from .serializiers import NewsAPISerializer, CommentApiSerializer, StatusSerializer,\
    NewsStatusSerializer
from .permission import NewsPermission


class NewsViewSet(viewsets.ModelViewSet):
    queryset = News.objects.all()
    serializer_class = NewsAPISerializer
    permission_classes = [NewsPermission, ]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user.author)


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentApiSerializer
    permission_classes = [NewsPermission, ]

    def get_queryset(self):
        return super().get_queryset().filter(news_id=self.kwargs.get('news_id'))

    def perform_create(self, serializer):
        serializer.save(
            author=self.request.user.author,
            news_id=self.kwargs.get('news_id')
        )


class StatusListCreateViewSet(generics.ListCreateAPIView):
    queryset = Status.objects.all()
    serializer_class = StatusSerializer


class StatusNewsViewSet(generics.CreateAPIView):
    queryset = NewsStatus.objects.all()
    serializer_class = NewsStatusSerializer

    def get_queryset(self):
        return super().get_queryset().filter(news_id=self.kwargs.get('slug'))

    def perform_create(self, serializer):
        serializer.save(
            author=self.request.user.author,
            news_id=self.kwargs.get('slug')
        )

