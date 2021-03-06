from django.urls import path
from .views import (
    PostListView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView,
    PostDetailView,
)
from . import views
from django.views.decorators.csrf import csrf_exempt



app_name = 'blog'


urlpatterns = [
    path('', PostListView.as_view(), name='home'),
    path('search/', views.search, name='search-results'),
    path('a_search/', csrf_exempt(views.ajax_search), name='a-search-results'),
    path('user/<int:pk>/', views.user_posts_view, name='user-posts'),
    path('post/<slug:slug>/', PostDetailView.as_view(), name='post-detail'),
    # path('post/<slug:slug>/', views.post_detail_view, name='post-detail'),
    path('create/new/', PostCreateView.as_view(), name='create-new-blog'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='blog-update'),
    # path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),

    path('delete/<int:pk>/', views.delete_post, name='blog-delete'),
    path('about/', views.about, name='blog-about'),

    path('like/post/', views.like_post, name='like-post'),
    path('dislike/post/', views.dislike_post, name='dislike-post'),
]
