"""exam URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from account import views as a_views
from news import views as n_views
from rest_framework.authtoken.views import obtain_auth_token

news = DefaultRouter()
news.register('', n_views.NewsViewSet, basename='news')
comment = DefaultRouter()
comment.register('comment', n_views.CommentViewSet, basename='comment')
status_news = DefaultRouter()
status_news.register('status', n_views.StatusNewsViewSet, basename='news_status')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/auth/', include('rest_framework.urls')),
    path('api/account/token/', obtain_auth_token),
    path('api/account/register/', a_views.AuthorRegisterAPIView.as_view(
        {'get': 'list',
         'post': 'create'})),
    path('api/news/', include(news.urls)),
    path('api/status/', n_views.StatusListCreateViewSet.as_view()),
    path('api/news/<int:news_id>/', include(comment.urls)),
    path('api/news/<slug:slug>/status/', n_views.StatusNewsViewSet.as_view()),
]
