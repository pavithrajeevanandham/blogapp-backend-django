from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Blog
from .serializer import BlogSerializer


# Create your views here.
@api_view(['GET'])
def home(request):
    routes = [
            {
            'End Point': '/blogs/',
            'method': 'GET',
            'description': 'returns array of blogs'
        },
        {
            'End Point': '/blogs/id',
            'method': 'GET',
            'description': 'returns a single blog object'
        },
        {
            'End Point': '/blogs/create',
            'method': 'POST',
            'description': 'creates new blog with data sent in request'
        },
        {
            'End Point': '/blogs/id/update',
            'method': 'PUT',
            'description': 'updates existing blog'
        },
        {
            'End Point': '/blogs/id/delete',
            'method': 'DELETE',
            'description': 'deletes an existing blog'
        },
    ]
    return Response(routes)


@api_view(['GET'])
def getBlogs(request):
    blogs = Blog.objects.all()
    serializer = BlogSerializer(blogs, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def getBlog(request, pk):
    blog = Blog.objects.get(id=pk)
    serializer = BlogSerializer(blog, many= False)
    return Response(serializer.data)


@api_view(['PUT'])
def updateBlog(request, pk):
    blog = Blog.objects.get(id=pk)
    serializer = BlogSerializer(instance=blog, data= request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['DELETE'])
def deleteBlog(request, pk):
    Blog.objects.get(id=pk).delete()
    return Response("Blog Was Deleted Successfully")


@api_view(['POST'])
def createBlog(request):
    serializer = BlogSerializer(data= request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)