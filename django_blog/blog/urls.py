from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from .views import (
    PostListView,
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView,
)
urlpatterns = [
    path('', views.home, name='home'),
     path('register/', views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='blog/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='blog/logout.html'), name='logout'),
    path('profile/', views.profile, name='profile'),
       # List & Detail
    path('posts/', PostListView.as_view(), name='post-list'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),

    # Create
    path('post/new/', PostCreateView.as_view(), name='post-create'),

    # Update
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),

    # Delete
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
]

