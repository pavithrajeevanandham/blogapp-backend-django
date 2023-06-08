from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('blogs/', views.getBlogs, name='blogs'),
    path('blogs/create', views.createBlog, name='create'),
    path('blogs/<str:pk>/update', views.updateBlog, name='update'),
    path('blogs/<str:pk>/delete', views.deleteBlog, name='delete'),
    path('blogs/<str:pk>/', views.getBlog, name='blog')
]