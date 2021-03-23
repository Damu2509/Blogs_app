from django.urls import path
from . import views
from django.contrib import admin
from .views import PostListView, PostDetailView , PostCreateView , PostUpdateView,  PostDeleteView, UserPostListView

urlpatterns = [

    path('', views.home,name='home'),
    path('about/', views.about,name='blog-about'),
    path('post/', PostListView.as_view(),name='post'),
    path('user/<str:username>', UserPostListView.as_view(),name='user-posts'),
    path('post/<int:pk>/', PostDetailView.as_view(),name='post-detail'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(),name='post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(),name='post-delete'),

    path('post/new/', PostCreateView.as_view(),name='post-create'),



]
