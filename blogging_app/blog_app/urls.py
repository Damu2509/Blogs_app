from django.urls import path
from . import views
from django.contrib import admin
from .views import PostListView, PostDetailView , PostCreateView

urlpatterns = [

    path('', views.home,name='home'),
    path('about/', views.about,name='blog-about'),
    path('post/', PostListView.as_view(),name='post'),
    path('post/<int:pk>/', PostDetailView.as_view(),name='post-detail'),
    path('post/new/', PostCreateView.as_view(),name='post-create'),



]
